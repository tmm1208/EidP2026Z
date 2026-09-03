# Aufgabe 03-Z3: Jahreszeitenfinder
# Musterlösung

monat = int(input("Monat: "))

# Lösung mit if-elif-else
if monat == 3 or monat == 4 or monat == 5:
    print("Jahreszeit: Frühling")
elif monat == 6 or monat == 7 or monat == 8:
    print("Jahreszeit: Sommer")
elif monat == 9 or monat == 10 or monat == 11:
    print("Jahreszeit: Herbst")
elif monat == 12 or monat == 1 or monat == 2:
    print("Jahreszeit: Winter")
else:
    print("Ungültige Monatsnummer.")

# Lösung mit match-case (alternativ)
# match monat:
#     case 3 | 4 | 5:
#         print("Jahreszeit: Frühling")
#     case 6 | 7 | 8:
#         print("Jahreszeit: Sommer")
#     case 9 | 10 | 11:
#         print("Jahreszeit: Herbst")
#     case 12 | 1 | 2:
#         print("Jahreszeit: Winter")
#     case _:
#         print("Ungültige Monatsnummer.")
