import requests

city = input("Enter your city: ")
geo_url = "https://geocoding-api.open-meteo.com/v1/search?name=" + city + "&count=1"
geo_response = requests.get(geo_url)
geo_data = geo_response.json()

lat = geo_data["results"][0]["latitude"]
lon = geo_data["results"][0]["longitude"]


response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=" + str(lat) + "&longitude=" + str(lon) + "&current_weather=true")
data = response.json()

print(f"weather in {city}:")
print("temperature:", data["current_weather"]["temperature"])
print("windspeed:", data["current_weather"]["windspeed"])