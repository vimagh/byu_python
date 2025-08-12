# Creative Additions:
# - User can enter a year to get avg, min, max life expectancy
# - User can enter a country to get avg, min, max life expectancy
# - Program finds the biggest drop in life expectancy for any country year-over-year

print("Welcome to the Life Expectancy Explorer!\n")

# Load and parse the file
file_path = "life-expectancy.csv"
file = open(file_path, "r")
lines = file.readlines()
file.close()

data = []

# Skip header
for line in lines[1:]:
    parts = line.strip().split(',')
    if len(parts) != 4:
        continue
    country = parts[0]
    year = int(parts[2])
    life_exp = float(parts[3])
    data.append((country, year, life_exp))

# Find lowest and highest life expectancy in dataset
min_val = float('inf')
max_val = float('-inf')
min_info = ()
max_info = ()

for entry in data:
    country, year, life_exp = entry
    if life_exp < min_val:
        min_val = life_exp
        min_info = (year, country, life_exp)
    if life_exp > max_val:
        max_val = life_exp
        max_info = (year, country, life_exp)

print("=== Overall Life Expectancy Stats ===")
print(f"📉 Lowest: {min_info[2]:.2f} in {min_info[1]} ({min_info[0]})")
print(f"📈 Highest: {max_info[2]:.2f} in {max_info[1]} ({max_info[0]})")

# User input: YEAR
try:
    year_input = int(input("\nEnter a year to analyze (e.g., 1990): "))
    total = 0
    count = 0
    min_year = None
    max_year = None

    for entry in data:
        country, year, life_exp = entry
        if year == year_input:
            total += life_exp
            count += 1
            if min_year is None or life_exp < min_year[2]:
                min_year = (country, year, life_exp)
            if max_year is None or life_exp > max_year[2]:
                max_year = (country, year, life_exp)

    if count > 0:
        avg = total / count
        print(f"\nIn {year_input}:")
        print(f"Average Life Expectancy: {avg:.2f}")
        print(f"Minimum: {min_year[2]:.2f} in {min_year[0]}")
        print(f"Maximum: {max_year[2]:.2f} in {max_year[0]}")
    else:
        print(f"No data found for year {year_input}")

except ValueError:
    print("Invalid year input.")

# User input: COUNTRY
country_input = input("\nEnter a country to analyze (e.g., Nigeria): ").strip().lower()
total = 0
count = 0
min_c = None
max_c = None

for entry in data:
    country, year, life_exp = entry
    if country.lower() == country_input:
        total += life_exp
        count += 1
        if min_c is None or life_exp < min_c:
            min_c = life_exp
        if max_c is None or life_exp > max_c:
            max_c = life_exp

if count > 0:
    avg = total / count
    print(f"\nStats for {country_input.title()}:")
    print(f"Average Life Expectancy: {avg:.2f}")
    print(f"Minimum: {min_c:.2f}")
    print(f"Maximum: {max_c:.2f}")
else:
    print("No data found for that country.")

# Largest year-over-year drop
print("\n🔍 Looking for largest drop in life expectancy...")

# Prepare data by country
countries = {}
for entry in data:
    country, year, life_exp = entry
    if country not in countries:
        countries[country] = []
    countries[country].append((year, life_exp))

largest_drop = 0
drop_info = ()

for country in countries:
    records = sorted(countries[country])
    for i in range(1, len(records)):
        prev_year, prev_val = records[i-1]
        curr_year, curr_val = records[i]
        drop = prev_val - curr_val
        if drop > largest_drop:
            largest_drop = drop
            drop_info = (country, prev_year, curr_year, prev_val, curr_val)

if drop_info:
    print(f"Largest drop: {largest_drop:.2f} in {drop_info[0]} from {drop_info[3]:.2f} to {drop_info[4]:.2f} between {drop_info[1]} and {drop_info[2]}")
