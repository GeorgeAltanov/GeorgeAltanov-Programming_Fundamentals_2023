countries = input().split(", ")
capitals = input().split(", ")

# information = {countries[name]: capitals[name] for name in range(len(countries))}
information = dict(zip(countries, capitals))
for country, capital in information.items():
    print(f"{country} -> {capital}")