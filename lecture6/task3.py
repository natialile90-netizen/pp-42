locations = [ ("Tbilisi", 41.71, 44.82), ("Batumi", 41.64, 41.63), ("Kutaisi", 42.26, 42.71) ]

for city, latitude, longitude in locations:
    print(f"City: {city}, Latitude: {latitude}, Longitude: {longitude}")

city_names = [city for city, latitude, longitude in locations]

print(city_names)

