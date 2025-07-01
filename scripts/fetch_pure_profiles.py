#!/usr/bin/env python3
"""
Fetch team profiles from Pure Research Portal
Pure API documentation: https://doc.pure.elsevier.com/display/PureClient/Pure+Web+Services

This script can fetch researcher profiles from Pure and update the _data/team.yml file
"""

import requests
import yaml
import json
from typing import Dict, List, Optional

# Configuration
PURE_BASE_URL = "https://pure.port.ac.uk"
PURE_API_KEY = "YOUR_API_KEY_HERE"  # Request from Pure administrators
# Adjust based on Pure structure
ICG_ORG_ID = "/en/organisations/dd37446e-3631-4f43-9ad4-e7fa2a9ed93a"

def fetch_pure_profiles(org_id: str) -> List[Dict]:
    """
    Fetch researcher profiles from Pure API

    Pure typically offers several endpoints:
    - /ws/api/persons - List all persons
    - /ws/api/organisations/{id}/persons - List persons in organization
    - OAI-PMH endpoint for harvesting
    """

    # Method 1: Try Pure Web Service API (requires API key)
    headers = {
        "Accept": "application/json",
        "api-key": PURE_API_KEY
    }

    try:
        # Try the persons endpoint filtered by organization
        response = requests.get(
            f"{PURE_BASE_URL}/ws/api/persons",
            headers=headers,
            params={
                "organisationalUnits.id": org_id,
                "size": 100
            }
        )

        if response.status_code == 200:
            return parse_pure_api_response(response.json())
    except Exception as e:
        print(f"API method failed: {e}")

    # Method 2: Try OAI-PMH (often publicly available)
    try:
        oai_url = f"{PURE_BASE_URL}/ws/oai"
        response = requests.get(oai_url, params={
            "verb": "ListRecords",
            "metadataPrefix": "mods",
            "set": f"organisations:{org_id}"
        })

        if response.status_code == 200:
            return parse_oai_response(response.text)
    except Exception as e:
        print(f"OAI-PMH method failed: {e}")

    # Method 3: Web scraping fallback (check robots.txt first!)
    print("Note: Could not access Pure API. You may need to:")
    print("1. Request an API key from Pure administrators")
    print("2. Check if OAI-PMH is enabled")
    print("3. Manually add team members to _data/team.yml")

    return []

def parse_pure_api_response(data: Dict) -> List[Dict]:
    """Parse Pure API JSON response"""
    members = []

    for item in data.get("items", []):
        member = {
            "name": item.get("name", {}).get("text", ""),
            "role": item.get("staffOrganisationAssociations", [{}])[0].get("jobTitle", ""),
            "email": item.get("emails", [{}])[0].get("value", ""),
            "pure_id": item.get("pureId", ""),
            "pure_url": f"{PURE_BASE_URL}/en/persons/{item.get('uuid', '')}",
            "orcid": item.get("orcid", ""),
            "research_interests": [
                keyword.get("text", "")
                for keyword in item.get("keywordGroups", [{}])[0].get("keywords", [])
            ],
            "bio": item.get("profileInformation", {}).get("text", "")
        }
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
        with open("_data/team.yml", "r") as f:
            data = yaml.safe_load(f) or {"members": []}
    except:
        data = {"members": []}

    # Update with new members
    data["members"] = members

    # Save back
    with open("_data/team.yml", "w") as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False)

    print(f"Updated _data/team.yml with {len(members)} team members")

def main():
    """Main function"""
    print("Fetching team profiles from Pure...")

    # Fetch profiles
    members = fetch_pure_profiles(ICG_ORG_ID)

    if members:
        update_team_yml(members)
    else:
        print("\nManual configuration needed:")
        print("1. Add your Pure API key to this script")
        print("2. Or manually add team members to _data/team.yml")
        print("3. Each member needs: name, role, email, pure_url")

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
