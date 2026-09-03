# Aufgabe 09-Z4: JSON – Konfiguration speichern und laden
# Musterlösung

import json

konfig = {
    "benutzername": "Tim",
    "sprache": "de",
    "benachrichtigungen": True,
    "max_eintraege": 50
}

# Speichern
with open("konfig.json", "w", encoding="utf-8") as f:
    json.dump(konfig, f, indent=4)

print("Konfiguration gespeichert.")
print()

# Laden
with open("konfig.json", "r", encoding="utf-8") as f:
    geladene_konfig = json.load(f)

print("Geladene Konfiguration:")
for key, value in geladene_konfig.items():
    print(f"  {key}: {value}")

# Wert ändern und erneut speichern
geladene_konfig["max_eintraege"] = 100

with open("konfig.json", "w", encoding="utf-8") as f:
    json.dump(geladene_konfig, f, indent=4)

print()
print("Konfiguration nach Änderung erneut gespeichert.")
