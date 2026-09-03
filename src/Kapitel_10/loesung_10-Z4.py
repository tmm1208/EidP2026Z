# Aufgabe 10-Z4: Pandas – DataFrame erkunden
# Musterlösung

import pandas as pd

daten = {
    "name":        ["Alice", "Bob", "Charlie", "Diana", "Eva"],
    "studiengang": ["Informatik", "BWL", "Informatik", "Medizin", "BWL"],
    "note":        [1.7, 2.3, 1.3, 2.0, 3.0],
    "semester":    [3, 5, 1, 7, 3]
}

df = pd.DataFrame(daten)

print("--- Erste 3 Zeilen ---")
print(df.head(3))
print()

print("--- Statistik ---")
print(df.describe())
print()

print("--- Nur Informatik ---")
informatik = df[df["studiengang"] == "Informatik"]
print(informatik)
print()

print("--- Notendurchschnitt pro Studiengang ---")
durchschnitt = df.groupby("studiengang")["note"].mean()
print(durchschnitt)
print()

print("--- Sortiert nach Note ---")
sortiert = df.sort_values("note")
print(sortiert)
