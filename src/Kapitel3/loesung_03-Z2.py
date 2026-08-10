# Aufgabe 03-Z2: Fitnessstudio-Zugang
# Musterlösung

alter = int(input("Alter: "))
hat_mitgliedschaft = input("Mitgliedschaft (ja/nein): ") == "ja"
hat_tageskarte = input("Tageskarte (ja/nein): ") == "ja"

if (hat_mitgliedschaft and alter >= 16) or hat_tageskarte:
    print("Zutritt gewährt!")
else:
    print("Zutritt verweigert.")
