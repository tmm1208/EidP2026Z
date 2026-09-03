# Aufgabe 07-Z5: Type Hints, lambda und map/filter
# Musterlösung

# --- Teil A: Type Hints ---
def berechne_bmi(gewicht_kg: float, groesse_m: float) -> float:
    """
    Berechnet den Body-Mass-Index (BMI).

    Parameter:
        gewicht_kg (float): Gewicht in Kilogramm.
        groesse_m (float): Körpergröße in Metern.

    Rückgabe:
        float: Der berechnete BMI-Wert.
    """
    return gewicht_kg / groesse_m ** 2

bmi = berechne_bmi(70, 1.75)
print(f"BMI (70kg, 1.75m): {bmi:.2f}")
print()

# --- Teil B: lambda und sorted() ---
produkte = [
    {"name": "Maus", "preis": 29.99},
    {"name": "Tastatur", "preis": 79.99},
    {"name": "Monitor", "preis": 349.99},
    {"name": "Kabel", "preis": 9.99},
]

produkte.sort(key=lambda p: p["preis"])

print("Produkte nach Preis:")
for p in produkte:
    print(f"  {p['name']}: {p['preis']:.2f} Euro")
print()

# --- Teil C: map() und filter() ---
temperaturen = [22.5, -3.0, 18.0, -10.5, 35.0, 0.0, 28.5]

positive = list(filter(lambda t: t > 0, temperaturen))
gerundet = list(map(lambda t: round(t, 1), temperaturen))

print(f"Positive Temperaturen:  {positive}")
print(f"Gerundete Temperaturen: {gerundet}")
