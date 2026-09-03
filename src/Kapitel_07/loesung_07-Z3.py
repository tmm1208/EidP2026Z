# Aufgabe 07-Z3: *args und **kwargs
# Musterlösung

def erstelle_rechnung(kunde, *artikel, **extras):
    """Gibt eine formatierte Rechnung auf der Konsole aus."""
    print(f"--- Rechnung für: {kunde} ---")
    print("Artikel:")
    for a in artikel:
        print(f"  - {a}")
    if extras:
        print("Extras:")
        for key, value in extras.items():
            print(f"  {key}: {value}")

erstelle_rechnung("Anna", "Laptop", "Maus", "Tastatur")
print()
erstelle_rechnung("Ben", "Monitor", "Kabel", rabatt="10%", versand="kostenlos")
