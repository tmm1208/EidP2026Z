# Aufgabe 10-Z1: HTTP-Anfrage und Statuscode
# Musterlösung

import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=53.89&longitude=11.45&current_weather=true"

try:
    response = requests.get(url)
    print(f"Statuscode: {response.status_code}")
    response.raise_for_status()

    daten = response.json()
    wetter = daten.get("current_weather", {})
    temperatur = wetter.get("temperature")
    windgeschwindigkeit = wetter.get("windspeed")

    print("Aktuelles Wetter in Wismar:")
    print(f"  Temperatur: {temperatur}°C")
    print(f"  Wind: {windgeschwindigkeit} km/h")

except requests.exceptions.RequestException as e:
    print(f"Ein Fehler ist aufgetreten: {e}")
