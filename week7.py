# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to calculate wind chill
def wind_chill(temp_f, wind_speed):
    return 35.74 + (0.6215 * temp_f) - (35.75 * (wind_speed ** 0.16)) + (0.4275 * temp_f * (wind_speed ** 0.16))

# Ask user for temperature
temperature = float(input("What is the temperature? "))
unit = input("Fahrenheit or Celsius (F/C)? ").strip().upper()

# Convert to Fahrenheit if needed
if unit == 'C':
    temperature = celsius_to_fahrenheit(temperature)

# Loop through wind speeds and display results
for speed in range(5, 65, 5):
    wc = wind_chill(temperature, speed)
    print(f"At temperature {temperature:.1f}F, and wind speed {speed} mph, the windchill is: {wc:.2f}F")
