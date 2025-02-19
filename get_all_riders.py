import json
from procyclingstats import  Team
import json

# List of race URLs you want to collect riders from

# List of all WorldTour & ProTour team URLs for a specific year (e.g., 2024)
team_urls = [
    "team/alpecin-deceuninck-2025",
    "team/arkea-b-b-hotels-2025",
    "team/bahrain-victorious-2025",
    "team/burgos-burpellet-bh-2025",
    "team/caja-rural-seguros-rga-2025",
    "team/team/cofidis-2025",
    "team/decathlon-ag2r-la-mondiale-2025",
    "team/ef-education-easypost-2025",
    "team/euskaltel-euskadi-2025",
    "team/team-flanders-baloise-2025",
    "team/groupama-fdj-2025",
    "team/ineos-grenadiers-2025",
    "team/intermarche-wanty-2025",
    "team/israel-premier-tech-2025",
    "team/team-jayco-alula-2025",
    "team/equipo-kern-pharma-2025",
    "team/lidl-trek-2025",
    "team/lotto-2025",
    "team/movistar-team-2025",
    "team/team-novo-nordisk-2025",
    "team/team-picnic-postnl-2025",
    "team/team-polti-visitmalta-2025",
    "team/q365-pro-cycing-team-2025",
    "team/red-bull-bora-hansgrohe-2025",
    "team/team-solution-tech-vini-fantini-2025",
    "team/soudal-quick-step-2025",
    "team/tarteletto-isorex-2025",
    "team/team-totalenergies-2025",
    "team/tudor-pro-cycling-team-2025",
    "team/uae-team-emirates-xrg-2025",
    "team/unibet-tietema-rockets-2025",
    "team/uno-x-mobility-2025",
    "team/vf-group-bardiani-csf-faizane-2025",
    "team/team-visma-lease-a-bike-2025",
    "team/wagner-bazin-wb-2025",
    "team/xds-astana-team-2025",
]

# List to store all rider names
all_riders = []

# Loop through each team and collect rider names
for team_url in team_urls:
    try:
        team = Team(team_url)
        riders = team.riders()  # Fetch all riders
        
        for rider in riders:
            name = rider.get("rider_name")  # Extract name
            if name:
                all_riders.append(name)  # Add to list

    except Exception as e:
        print(f"Skipping team {team_url} due to error: {e}")

# Print the final JSON output
print(json.dumps(all_riders, indent=2, ensure_ascii=False))
