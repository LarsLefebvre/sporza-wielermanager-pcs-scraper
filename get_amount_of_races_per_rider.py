import time
from procyclingstats import RaceStartlist
from collections import Counter

# List of race URLs for 2025 (replace with actual race URLs)
races_2025 = [
    "race/omloop-het-nieuwsblad/2025/startlist/startlist",
    "race/kuurne-brussel-kuurne/2025/startlist/startlist",
    "race/gp-samyn/2025/startlist/startlist",
    "race/strade-bianche/2025/startlist/startlist",
    "race/nokere-koers/2025/startlist/startlist",
    "race/bredene-koksijde-classic/2025/startlist/startlist",
    "race/milano-sanremo/2025/startlist/startlist",
    "race/classic-brugge-de-panne/2025/startlist/startlist",
    "race/e3-harelbeke/2025/startlist/startlist",
    "race/gent-wevelgem/2025/startlist/startlist",
    "race/dwars-door-vlaanderen/2025/startlist/startlist",
    "race/scheldeprijs/2025/startlist/startlist",
    "race/ronde-van-vlaanderen/2025/startlist/startlist",
    "race/paris-roubaix/2025/startlist/startlist",
    "race/ronde-van-limburg/2025/startlist/startlist",
    "race/brabantse-pijl/2025/startlist/startlist",
    "race/amstel-gold-race/2025/startlist/startlist",
    "race/la-fleche-wallone/2025/startlist/startlist",
    "race/liege-bastogne-liege/2025/startlist/startlist",

]

# Dictionary to count the number of races each cyclist is in
cyclist_counts = Counter()

# Loop through each race and get the start list
for race_url in races_2025:
    try:
        print(f"Fetching start list for {race_url}...")

        
        # Create a RaceStartlist object for the given race
        race_startlist = RaceStartlist(race_url)
        
        # Get the full startlist using the `parse()` method
        race_data = race_startlist.parse()
        
        # Extract the list of riders from the parsed data
        riders = [rider['rider_name'] for rider in race_data['startlist']]
        
        # Count each rider's participation
        cyclist_counts.update(riders)
        
        # Delay to avoid getting blocked
        time.sleep(1)  # Adjust if needed

    except Exception as e:
        # If there's an issue with fetching data for a race, log the error and continue
        print(f"Error fetching data for {race_url}: {e}")

# Sort cyclists by the number of races they are participating in (from most to least)
sorted_cyclists = cyclist_counts.most_common()

# Display only the top 100 cyclists
top_100_cyclists = sorted_cyclists[:100]

# Print the top 100 cyclists and their race count
print("\nTop 100 cyclists who will participate in the most races in 2025 for the Sporza Wielermanager:\n")
for i, (cyclist, count) in enumerate(top_100_cyclists, 1):
    print(f"{i}. {cyclist}: {count} races")