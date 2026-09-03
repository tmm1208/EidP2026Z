# Aufgabe 04-Z4: Wörter filtern mit continue und break
# Musterlösung

woerter = ["Hallo", "Hi", "Python", "ist", "cool", "stopp", "das", "kommt", "nicht", "mehr"]

for wort in woerter:
    if wort == "stopp":
        print("Schleife durch 'stopp' beendet.")
        break
    if len(wort) < 4:
        continue
    print(wort)
