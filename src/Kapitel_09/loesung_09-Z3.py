# Aufgabe 09-Z3: CSV lesen und auswerten
# Musterlösung

import csv

# CSV-Datei erstellen
with open("produkte.csv", "w", newline="", encoding="utf-8") as f:
    f.write("name,kategorie,preis\n")
    f.write("Laptop,Elektronik,999.99\n")
    f.write("Maus,Elektronik,29.99\n")
    f.write("Schreibtisch,Möbel,349.00\n")
    f.write("Stuhl,Möbel,189.00\n")
    f.write("Kopfhörer,Elektronik,149.99\n")

# CSV einlesen
produkte = []
with open("produkte.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        row["preis"] = float(row["preis"])
        produkte.append(row)

# Alle Produkte ausgeben
print("--- Alle Produkte ---")
for p in produkte:
    print(f"{p['name']}: {p['preis']} Euro")

# Durchschnittspreis
durchschnitt = sum(p["preis"] for p in produkte) / len(produkte)
print(f"\nDurchschnittspreis: {durchschnitt:.2f} Euro")

# Nur Elektronik
print("\n--- Nur Elektronik ---")
for p in produkte:
    if p["kategorie"] == "Elektronik":
        print(f"{p['name']}: {p['preis']} Euro")
