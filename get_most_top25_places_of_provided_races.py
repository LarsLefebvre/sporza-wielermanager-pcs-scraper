from collections import Counter
from procyclingstats import RaceStartlist
import time

races = [
    "race/omloop-het-nieuwsblad/2022",
    "race/kuurne-brussel-kuurne/2022",
    "race/gp-samyn/2022",
    "race/strade-bianche/2022",
    "race/nokere-koers/2022",
    "race/bredene-koksijde-classic/2022",
    "race/milano-sanremo/2022",
    "race/classic-brugge-de-panne/2022",
    "race/e3-harelbeke/2022",
    "race/gent-wevelgem/2022",
    "race/dwars-door-vlaanderen/2022",
    "race/scheldeprijs/2022",
    "race/ronde-van-vlaanderen/2022",
    "race/paris-roubaix/2022",
    "race/ronde-van-limburg/2022",
    "race/brabantse-pijl/2022",
    "race/amstel-gold-race/2022",
    "race/la-fleche-wallone/2022",
    "race/liege-bastogne-liege/2022", 
    "race/omloop-het-nieuwsblad/2023",
    "race/kuurne-brussel-kuurne/2023",
    "race/gp-samyn/2023",
    "race/strade-bianche/2023",
    "race/nokere-koers/2023",
    "race/bredene-koksijde-classic/2023",
    "race/milano-sanremo/2023",
    "race/classic-brugge-de-panne/2023",
    "race/e3-harelbeke/2023",
    "race/gent-wevelgem/2023",
    "race/dwars-door-vlaanderen/2023",
    "race/scheldeprijs/2023",
    "race/ronde-van-vlaanderen/2023",
    "race/paris-roubaix/2023",
    "race/ronde-van-limburg/2023",
    "race/brabantse-pijl/2023",
    "race/amstel-gold-race/2023",
    "race/la-fleche-wallone/2023",
    "race/liege-bastogne-liege/2023", 
    "race/omloop-het-nieuwsblad/2024",
    "race/kuurne-brussel-kuurne/2024",
    "race/gp-samyn/2024",
    "race/strade-bianche/2024",
    "race/nokere-koers/2024",
    "race/bredene-koksijde-classic/2024",
    "race/milano-sanremo/2024",
    "race/classic-brugge-de-panne/2024",
    "race/e3-harelbeke/2024",
    "race/gent-wevelgem/2024",
    "race/dwars-door-vlaanderen/2024",
    "race/scheldeprijs/2024",
    "race/ronde-van-vlaanderen/2024",
    "race/paris-roubaix/2024",
    "race/ronde-van-limburg/2024",
    "race/brabantse-pijl/2024",
    "race/amstel-gold-race/2024",
    "race/la-fleche-wallone/2024",
    "race/liege-bastogne-liege/2024", 
    # Add more race URLs here...
]

def get_top_25_riders_from_race(race_url):
    """
    Fetches the top 25 riders for a specific race.
    """
    try:
        # Fetch the race startlist
        race_startlist = RaceStartlist(race_url)
        riders = race_startlist.startlist()

        # Extract top 25 riders' names
        top_25_riders = [rider['rider_name'] for rider in riders[:25]]
        return top_25_riders
    except Exception as e:
        print(f"Error fetching top 25 for {race_url}: {e}")
        return []

# Dictionary to track appearances of each rider in the top 25
rider_appearance_counter = Counter()

# Loop through all races and collect the top 25 riders
for race_url in races:
    print(f"Processing race: {race_url}")
    top_25_riders = get_top_25_riders_from_race(race_url)
    
    # Update the counter with riders who appeared in the top 25
    rider_appearance_counter.update(top_25_riders)
    
    # Add a small delay to avoid overwhelming the server
    time.sleep(1)

# Now we have the count of appearances for each rider in the top 25 across all races
top_riders = rider_appearance_counter.most_common()

# Print the top riders with the most appearances
print("\nTop Riders in the Top 25 across the races included in Sporza Wielermanager since 2022:")
for rank, (rider_name, appearances) in enumerate(top_riders[:25], 1):  # Display top 25
    print(f"{rank}. {rider_name} - {appearances} appearances")