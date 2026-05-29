import requests

response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=6.5244&longitude=3.3792&current_weather=true")
data = response.json()

print("temperature:", data["current_weather"]["temperature"])
print("windspeed:", data["current_weather"]["windspeed"])