# Pure Research Portal Integration

This directory contains scripts for integrating with the University of Portsmouth Pure Research Portal.

## Setup

### Prerequisites
```bash
pip install requests pyyaml
```

### Configuration

1. **Get Pure API Access**: Contact your Pure administrators to request:
   - API key for web services access
   - Organization/department IDs for filtering
   - OAI-PMH endpoint information

2. **Set environment variables**:
   ```bash
   export PURE_API_KEY="your-api-key-here"
   export PURE_ORG_ID="/en/organisations/your-organization-id"
   ```

## Usage

### Method 1: Automated (with API access)
```bash
python3 scripts/fetch_pure_profiles.py
```

This will:
- Fetch team member profiles from Pure
- Update `_data/team.yml` automatically. If the file uses the `teams` structure, fetched members are written to the `rse` team by default. Set `PURE_TEAM_KEY` to target another team.
- Rebuild the site with current data

### Method 2: Manual
Edit `_data/team.yml` directly:
```yaml
members:
  - name: "Dr. Jane Smith"
    role: "Senior Research Software Engineer"
    email: "jane.smith@port.ac.uk"
    pure_url: "https://researchportal.port.ac.uk/en/persons/jane-smith"
    orcid: "0000-0000-0000-0000"
    research_interests:
      - "Machine Learning"
      - "Cosmological Simulations"
    bio: "Brief bio..."
    image: "/assets/images/team/jane.jpg"  # Optional
```

## Pure API Endpoints

Common Pure endpoints you might use:
- `/ws/api/persons` - All persons
- `/ws/api/organisations/{id}/persons` - Persons in organization
- `/ws/oai` - OAI-PMH harvesting endpoint

## Automation

You can set up automated updates using:
- GitHub Actions (run script on schedule)
- Cron job on your server
- Manual updates when team changes

## Troubleshooting

**403 Forbidden**: Pure portal may require:
- VPN access for API calls
- Proper authentication headers
- Whitelisted IP addresses

**No data returned**: Check:
- Organization ID is correct
- API key has proper permissions
- OAI-PMH is enabled for your content
