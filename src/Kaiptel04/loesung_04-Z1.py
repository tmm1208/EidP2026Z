# Aufgabe 04-Z1: Multiplikationstabelle
# Musterlösung

zahl = int(input("Zahl: "))

print(f"\nMultiplikationstabelle für {zahl}:")
for i in range(1, 11):
    ergebnis = zahl * i
    print(f"{zahl} x {i:2} = {ergebnis:2}")
