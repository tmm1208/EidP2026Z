# Aufgabe 03-Z1: Ampelsteuerung
# Musterlösung

farbe = input("Ampelfarbe: ")

if farbe == "rot":
    print("Anhalten!")
elif farbe == "gelb":
    print("Achtung – bitte bremsen!")
elif farbe == "gruen":
    print("Fahrt frei!")
else:
    print("Unbekannte Ampelfarbe.")
