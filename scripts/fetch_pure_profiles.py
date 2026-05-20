#!/usr/bin/env python3
"""
Fetch team profiles from Pure Research Portal
Pure API documentation: https://doc.pure.elsevier.com/display/PureClient/Pure+Web+Services

This script can fetch researcher profiles from Pure and update the _data/team.yml file
"""

import os
import re
from pathlib import Path
from typing import Any, Dict, List

import requests
import yaml

# Configuration
REPO_ROOT = Path(__file__).resolve().parents[1]
TEAM_DATA_PATH = REPO_ROOT / "_data" / "team.yml"
PURE_BASE_URL = os.environ.get("PURE_BASE_URL", "https://pure.port.ac.uk").rstrip("/")
PURE_API_KEY = os.environ.get("PURE_API_KEY")
# Adjust based on Pure structure
ICG_ORG_ID = os.environ.get("PURE_ORG_ID", "/en/organisations/dd37446e-3631-4f43-9ad4-e7fa2a9ed93a")
PURE_TEAM_KEY = os.environ.get("PURE_TEAM_KEY", "rse")
REQUEST_TIMEOUT = 20


def slugify(value: str) -> str:
    """Create a stable URL slug from a display name."""
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def fetch_pure_profiles(org_id: str) -> List[Dict]:
    """
    Fetch researcher profiles from Pure API

    Pure typically offers several endpoints:
    - /ws/api/persons - List all persons
    - /ws/api/organisations/{id}/persons - List persons in organization
    - OAI-PMH endpoint for harvesting
    """

    if PURE_API_KEY:
        headers = {
            "Accept": "application/json",
            "api-key": PURE_API_KEY,
        }

        try:
            # Try the persons endpoint filtered by organization
            response = requests.get(
                f"{PURE_BASE_URL}/ws/api/persons",
                headers=headers,
                params={
                    "organisationalUnits.id": org_id,
                    "size": 100,
                },
                timeout=REQUEST_TIMEOUT,
            )

            if response.status_code == 200:
                return parse_pure_api_response(response.json())

            print(f"API method returned HTTP {response.status_code}")
        except requests.RequestException as e:
            print(f"API method failed: {e}")
    else:
        print("Skipping Pure Web Services API: set PURE_API_KEY to enable it.")

    # Method 2: Try OAI-PMH (often publicly available)
    try:
        oai_url = f"{PURE_BASE_URL}/ws/oai"
        response = requests.get(
            oai_url,
            params={
                "verb": "ListRecords",
                "metadataPrefix": "mods",
                "set": f"organisations:{org_id}",
            },
            timeout=REQUEST_TIMEOUT,
        )

        if response.status_code == 200:
            return parse_oai_response(response.text)

        print(f"OAI-PMH method returned HTTP {response.status_code}")
    except requests.RequestException as e:
        print(f"OAI-PMH method failed: {e}")

    # Method 3: Web scraping fallback (check robots.txt first!)
    print("Note: Could not access Pure API. You may need to:")
    print("1. Request an API key from Pure administrators")
    print("2. Check if OAI-PMH is enabled")
    print("3. Manually add team members to _data/team.yml")

    return []

def first_dict(items: Any) -> Dict:
    """Return the first dictionary in a list-shaped API field."""
    if isinstance(items, list) and items and isinstance(items[0], dict):
        return items[0]
    return {}


def parse_pure_api_response(data: Dict) -> List[Dict]:
    """Parse Pure API JSON response"""
    members = []

    for item in data.get("items", []):
        name = (item.get("name") or {}).get("text", "")
        staff_association = first_dict(item.get("staffOrganisationAssociations", []))
        email = first_dict(item.get("emails", []))
        interests = []

        for group in item.get("keywordGroups", []) or []:
            for keyword in group.get("keywords", []) or []:
                text = keyword.get("text", "")
                if text:
                    interests.append(text)

        member = {
            "name": name,
            "slug": slugify(name),
            "role": staff_association.get("jobTitle", ""),
            "email": email.get("value", ""),
            "pure_id": item.get("pureId", ""),
            "pure_url": f"{PURE_BASE_URL}/en/persons/{item.get('uuid', '')}",
            "orcid": item.get("orcid", ""),
            "research_interests": interests,
            "bio": (item.get("profileInformation") or {}).get("text", ""),
        }

        if member["name"]:
            members.append(member)

    return members

def parse_oai_response(xml_data: str) -> List[Dict]:
    """Parse OAI-PMH XML response"""
    # This would require XML parsing - simplified for example
    print("OAI-PMH parsing not fully implemented")
    return []

def update_team_yml(members: List[Dict]):
    """Update the _data/team.yml file with fetched data"""

    # Load existing data
    try:
        with TEAM_DATA_PATH.open("r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {"members": []}
    except FileNotFoundError:
        data = {"members": []}
    except (OSError, yaml.YAMLError) as e:
        raise RuntimeError(f"Could not read {TEAM_DATA_PATH}: {e}") from e

    # Update with new members
    if isinstance(data.get("teams"), dict):
        team = data["teams"].setdefault(PURE_TEAM_KEY, {"name": PURE_TEAM_KEY, "members": []})
        team["members"] = members
        target = f"teams.{PURE_TEAM_KEY}.members"
    else:
        data["members"] = members
        target = "members"

    # Save back
    with TEAM_DATA_PATH.open("w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False)

    print(f"Updated {TEAM_DATA_PATH} {target} with {len(members)} team members")

def main():
    """Main function"""
    print("Fetching team profiles from Pure...")

    # Fetch profiles
    members = fetch_pure_profiles(ICG_ORG_ID)

    if members:
        update_team_yml(members)
    else:
        print("\nManual configuration needed:")
        print("1. Set PURE_API_KEY and PURE_ORG_ID in your environment")
        print("2. Or manually add team members to _data/team.yml")
        print("3. Each member needs: name, slug, role, email, pure_url")

        # Create example entry
        example = {
            "members": [{
                "name": "Dr. Jane Smith",
                "role": "Senior Research Software Engineer",
                "email": "jane.smith@port.ac.uk",
                "pure_url": "https://researchportal.port.ac.uk/en/persons/jane-smith",
                "research_interests": ["Machine Learning", "Cosmology", "HPC"],
                "bio": "Jane leads the ML initiatives in cosmological data analysis."
            }]
        }

        print("\nExample team.yml structure:")
        print(yaml.dump(example, default_flow_style=False))

if __name__ == "__main__":
    main()
