# Aufgabe 10-Z2: Mehrere API-Parameter nutzen
# Musterlösung

import requests

staedte = [
    {"name": "Wismar",  "lat": 53.89, "lon": 11.45},
    {"name": "Hamburg", "lat": 53.57, "lon": 10.02},
    {"name": "München", "lat": 48.14, "lon": 11.58},
]

for stadt in staedte:
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={stadt['lat']}&longitude={stadt['lon']}&current_weather=true"
    )
    try:
        response = requests.get(url)
        response.raise_for_status()
        wetter = response.json().get("current_weather", {})
        temp = wetter.get("temperature")
        wind = wetter.get("windspeed")
        print(f"{stadt['name']:8}: {temp}°C | Wind: {wind} km/h")
    except requests.exceptions.RequestException as e:
        print(f"{stadt['name']:8}: Fehler – {e}")
