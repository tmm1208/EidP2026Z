# Aufgabe 10-Z6: API-Daten in Pandas analysieren
# Musterlösung

import requests
import pandas as pd

staedte = [
    {"name": "Wismar",  "lat": 53.89, "lon": 11.45},
    {"name": "Hamburg", "lat": 53.57, "lon": 10.02},
    {"name": "Berlin",  "lat": 52.52, "lon": 13.41},
    {"name": "München", "lat": 48.14, "lon": 11.58},
    {"name": "Rostock", "lat": 54.09, "lon": 12.10},
]

ergebnisse = []

for stadt in staedte:
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={stadt['lat']}&longitude={stadt['lon']}&current_weather=true"
    )
    try:
        response = requests.get(url)
        response.raise_for_status()
        wetter = response.json().get("current_weather", {})
        ergebnisse.append({
            "stadt":               stadt["name"],
            "temperatur":          wetter.get("temperature"),
            "windgeschwindigkeit": wetter.get("windspeed"),
        })
    except requests.exceptions.RequestException as e:
        print(f"Fehler bei {stadt['name']}: {e}")
        continue

if ergebnisse:
    df = pd.DataFrame(ergebnisse)

    print("--- Wetterübersicht ---")
    print(df.to_string(index=False))
    print()

    waermste = df.loc[df["temperatur"].idxmax(), "stadt"]
    kaelteste = df.loc[df["temperatur"].idxmin(), "stadt"]
    mittlerer_wind = df["windgeschwindigkeit"].mean()

    waermste_temp = df["temperatur"].max()
    kaelteste_temp = df["temperatur"].min()

    print(f"Wärmste Stadt:        {waermste} ({waermste_temp}°C)")
    print(f"Kälteste Stadt:       {kaelteste} ({kaelteste_temp}°C)")
    print(f"Mittlere Windstärke:  {mittlerer_wind:.1f} km/h")
else:
    print("Keine Daten konnten abgerufen werden.")
