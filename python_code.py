import requests
para = {"name":"Berlin"}
data = requests.get('https://geocoding-api.open-meteo.com/v1/search', params=para,timeout=10)
result = data.json()
latitude,longitude = result["results"][0]["latitude"] , result["results"][0]["longitude"]

params = {
    "latitude": latitude,
    "longitude": longitude,
    "current": "temperature_2m,relative_humidity_2m"
}

data1 = requests.get('https://api.open-meteo.com/v1/forecast', params=params)
result1 = data1.json()
print(f"Temperature::{result1["current"]["temperature_2m"]}°C")
print("Humidity:",result1["current"]["relative_humidity_2m"],"%")
