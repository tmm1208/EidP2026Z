# Aufgabe 07-Z1: Funktionen mit return
# Musterlösung

def berechne_flaeche(breite, hoehe):
    return breite * hoehe

def berechne_umfang(breite, hoehe):
    return 2 * (breite + hoehe)

def ist_quadrat(breite, hoehe):
    return breite == hoehe

breite = 5
hoehe = 8

print(f"Fläche:    {berechne_flaeche(breite, hoehe)}")
print(f"Umfang:    {berechne_umfang(breite, hoehe)}")
print(f"Quadrat?:  {ist_quadrat(breite, hoehe)}")
