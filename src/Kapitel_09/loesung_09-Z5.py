# Aufgabe 09-Z5: Fehlerbehandlung mit LBYL und EAFP
# Musterlösung

import os

# Testdatei erstellen
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("Hallo aus der Testdatei!")


def lese_datei_lbyl(dateiname):
    """Liest eine Datei mit dem LBYL-Ansatz (Look Before You Leap)."""
    if os.path.exists(dateiname):
        with open(dateiname, "r", encoding="utf-8") as f:
            return f.read().strip()
    return None


def lese_datei_eafp(dateiname):
    """Liest eine Datei mit dem EAFP-Ansatz (try/except)."""
    try:
        with open(dateiname, "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None


print("--- LBYL ---")
inhalt = lese_datei_lbyl("test.txt")
if inhalt:
    print(f"Datei 'test.txt' gefunden: {inhalt}")
else:
    print("Datei 'test.txt' nicht gefunden.")

inhalt = lese_datei_lbyl("nicht_da.txt")
if inhalt:
    print(f"Datei 'nicht_da.txt' gefunden: {inhalt}")
else:
    print("Datei 'nicht_da.txt' nicht gefunden.")

print()
print("--- EAFP ---")
inhalt = lese_datei_eafp("test.txt")
if inhalt:
    print(f"Datei 'test.txt' gelesen: {inhalt}")
else:
    print("Fehler: Datei 'test.txt' nicht gefunden.")

inhalt = lese_datei_eafp("nicht_da.txt")
if inhalt:
    print(f"Datei 'nicht_da.txt' gelesen: {inhalt}")
else:
    print("Fehler: Datei 'nicht_da.txt' nicht gefunden.")
