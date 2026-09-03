# Aufgabe 04-Z2: Eingabe-Validierung mit while
# Musterlösung

zahl = 0
while zahl < 1 or zahl > 100:
    zahl = int(input("Bitte eine Zahl zwischen 1 und 100 eingeben: "))
    if zahl < 1 or zahl > 100:
        print("Ungültige Eingabe! Bitte erneut versuchen.")

print(f"Gültige Eingabe: {zahl}")
