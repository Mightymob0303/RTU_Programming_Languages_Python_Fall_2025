"""
Lab 3.1 – Simple Datasets and Aggregates

Goals:
- Create and manipulate Python lists and dictionaries.
- Compute aggregates such as sum, average, max, and min.

Instructions:
1. Create a list `temperatures` with daily temperatures for one week.
2. Create a dictionary `city_population` with at least 5 cities and their populations.
3. Compute:
   - The average temperature.
   - The maximum and minimum population.
   - The total population of all cities.
4. Print your results in a clear, formatted way.
"""

temperatures = [72, 75, 68, 80, 77, 74, 79]
city_population = {
    "New York": 8419000,
    "Los Angeles": 3980000,
    "Chicago": 2716000,
    "Houston": 2328000,
    "Phoenix": 1680000
}

# Compute aggregates
average_temperature = sum(temperatures) / len(temperatures)

# Find max and min populations
largest_population = max(city_population.values())
smallest_population = min(city_population.values())

# Find corresponding cities
largest_city = ""
smallest_city = ""
for city, population in city_population.items():
    if population == largest_population:
        largest_city = city
    if population == smallest_population:
        smallest_city = city

total_population = sum(city_population.values())

# Print results
print("=== Weather Data ===")
print(f"Daily temperatures: {temperatures}")
print(f"Average temperature: {average_temperature:.1f}°F")
print()

print("=== Population Data ===")
print("City populations:")
for city, population in city_population.items():
    print(f"  {city}: {population:,}")
print()

print("=== Aggregates ===")
print(f"Average temperature: {average_temperature:.1f}°F")
print(f"Largest city: {largest_city} - {largest_population:,} people")
print(f"Smallest city: {smallest_city} - {smallest_population:,} people")
print(f"Total population: {total_population:,} people")