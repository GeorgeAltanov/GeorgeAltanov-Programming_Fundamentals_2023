# Using a dictionary comprehension, write a program that receives country names on the first line, separated by comma and space ", ", and their corresponding capital cities on the second line (again separated by comma and space ", ").
# Print each country with their capital on a separate line in the following format: "{country} -> {capital}".
# You could use the zip() method.


countries = input().split(", ")
capitals = input().split(", ")

# information = {countries[name]: capitals[name] for name in range(len(countries))}
information = dict(zip(countries, capitals))
for country, capital in information.items():
    print(f"{country} -> {capital}")
