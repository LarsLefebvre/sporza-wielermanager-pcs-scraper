from procyclingstats import Ranking

def get_top_riders(year: str):
    """
    Fetch the top 100 riders for a specific year.
    """
    try:
        # Create a Ranking object to fetch the individual ranking for the given year
        ranking = Ranking(f"rankings/{year}/individual")  # Use the year dynamically
        ranking_data = ranking.individual_ranking()  # Fetch individual rankings
        
        # Extract the top 100 riders from the ranking data
        top_riders = []
        
        for rider in ranking_data[:100]:  # Only get the top 100 riders
            rider_name = rider['rider_name']
            rank = rider['rank']
            points = rider['points']
            team_name = rider['team_name']
            
            # Collect rider details
            top_riders.append({
                'rank': rank,
                'rider_name': rider_name,
                'points': points,
                'team_name': team_name,
            })
        
        return top_riders

    except Exception as e:
        print(f"Error fetching top riders for {year}: {e}")
        return []

# Fetch top riders for both 2024 and 2025
top_riders_2024 = get_top_riders("2022")
top_riders_2024 = get_top_riders("2023")
top_riders_2025 = get_top_riders("2024")

# Display top riders for 2022
print("\nTop 100 Riders for 2022:")
for rider in top_riders_2024:
    print(f"Rank {rider['rank']}: {rider['rider_name']} - {rider['team_name']} (Points: {rider['points']})")

# Display top riders for 2023
print("\nTop 100 Riders for 2023:")
for rider in top_riders_2024:
    print(f"Rank {rider['rank']}: {rider['rider_name']} - {rider['team_name']} (Points: {rider['points']})")

# Display top riders for 2024
print("\nTop 100 Riders for 2024:")
for rider in top_riders_2025:
    print(f"Rank {rider['rank']}: {rider['rider_name']} - {rider['team_name']} (Points: {rider['points']})")
