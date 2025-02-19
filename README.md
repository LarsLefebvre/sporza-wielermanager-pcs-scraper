# ProCyclingStats Scraper

The **ProCyclingStats Scraper** is designed for performing data analysis programmatically for the **Sporza Wielermanager** competition. This repository provides various Python scripts that utilize the ProCyclingStats API to extract and analyze cycling data effectively. Additionally, it includes a CSV file that maps Sporza Wielermanager costs per cyclist to their corresponding PCS names for streamlined data analysis.

![alt text](pcs-scraper.jpeg)


## Use Cases

This project includes the following examples of data analysis:

1. **Get All Riders**: Retrieve a comprehensive list of all cyclists participating in the races.
2. **Get Amount of Races Per Rider**: Calculate how many races each cyclist will participate in for the specified races in the 'Sporza Wielermanager.
3. **Get Most Top 10 Places of Provided Races**: Analyze and identify which cyclists have achieved the most top 10 placements in a given list of races.
4. **Get Most Top 25 Places of Provided Races**: Similar to the top 10 analysis, this function identifies cyclists with the most top 25 placements.
5. **Get Top Riders Per Year**: Fetch and analyze ranking data to identify the top riders for each year.
6. **Sporza to PCS Names**: Map names from Sporza Wielermanager to their corresponding PCS names using a provided CSV file.

## Getting Started

### Prerequisites

- Python
- Required libraries: `procyclingstats`, `requests`, `pandas`. You can install them using pip:

```bash
pip install procyclingstats requests pandas
```

### Example of running a Python 'script'
```bash
python get_amount_of_races_per_rider.py

(venv) larslefebvre@MacBook-Pro-van-Lars sporza-wielermanager-pcs-scraper % python get_amount_of_races_per_rider.py 
Fetching start list for race/omloop-het-nieuwsblad/2025/startlist/startlist...
Fetching start list for race/kuurne-brussel-kuurne/2025/startlist/startlist...
Fetching start list for race/gp-samyn/2025/startlist/startlist...
....

Top 100 cyclists who will participate in the most races in 2025 for the Sporza Wielermanager:

1. LAPORTE Christophe: 10 races
2. MEEUS Jordi: 9 races
3. BENOOT Tiesj: 9 races
4. MOHORIČ Matej: 9 races
5. RENARD Alexis: 9 races
6. REINDERS Elmar: 9 races
7. NARVÁEZ Jhonatan: 9 races
8. BALLERINI Davide: 9 races
9. SHEEHAN Riley: 9 races
10. DE LIE Arnaud: 9 races
.....
```


### Additional Notes:
The project is far from perfect. It just gives you some examples to kickstart your scraping journey to gather information from procyclingstates in a programmatic way. In this way you can use the data to do proper data analysis on who to select for your 'Sporza Wielermanager' team for 2025, or even let an AI decide for you 😀

