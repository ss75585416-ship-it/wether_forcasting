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
import requests

city = input("Enter city name: ")
para = {"name": city}

try:
    data = requests.get(
        'https://geocoding-api.open-meteo.com/v1/search',
        params=para,
        timeout=10
    )

    data.raise_for_status()
    result = data.json()

    if not result.get("results"):
        raise ValueError("Invalid city name! City not found.")

    latitude, longitude = (
        result["results"][0]["latitude"],
        result["results"][0]["longitude"]
    )

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m"
    }

    data1 = requests.get(
        'https://api.open-meteo.com/v1/forecast',
        params=params,
        timeout=10
    )

    data1.raise_for_status()
    result1 = data1.json()

    print(f"Temperature: {result1['current']['temperature_2m']}°C")
    print(f"Humidity: {result1['current']['relative_humidity_2m']}%")

except ValueError as e:
    print("Input Error:", e)

except requests.exceptions.Timeout:
    print("Error: Request timed out!")

except requests.exceptions.ConnectionError:
    print("Error: Check your internet connection!")

except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)

except requests.exceptions.RequestException as e:
    print("Request Error:", e)

except (KeyError, IndexError):
    print("Error: Unexpected API response!")
data1 = requests.get('https://api.open-meteo.com/v1/forecast', params=params)
result1 = data1.json()
print(f"Temperature::{result1["current"]["temperature_2m"]}°C")
print("Humidity:",result1["current"]["relative_humidity_2m"],"%")
