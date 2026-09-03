# Aufgabe 10-Z5: Pandas – CSV laden und auswerten
# Musterlösung

import pandas as pd

url = ("https://raw.githubusercontent.com/allisonhorst/"
       "palmerpenguins/main/inst/extdata/penguins.csv")

try:
    df = pd.read_csv(url)

    print(f"Form: {df.shape}")
    print(f"Spalten: {df.columns.tolist()}")
    print()

    print("Anzahl pro Art:")
    print(df["species"].value_counts())
    print()

    print("Mittlere Körpermasse pro Art (g):")
    print(df.groupby("species")["body_mass_g"].mean())

except Exception as e:
    print(f"Fehler beim Laden der Daten: {e}")
