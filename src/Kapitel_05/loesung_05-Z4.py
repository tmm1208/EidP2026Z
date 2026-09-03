# Aufgabe 05-Z4: Tupel für Koordinaten
# Musterlösung

wismar  = (53.8929, 11.4521)
rostock = (54.0924, 12.0991)
hamburg = (53.5753, 10.0153)

print(f"Wismar:  Breite {wismar[0]} | Länge {wismar[1]}")
print(f"Rostock: Breite {rostock[0]} | Länge {rostock[1]}")
print(f"Hamburg: Breite {hamburg[0]} | Länge {hamburg[1]}")

staedte = [wismar, rostock, hamburg]
print(f"Anzahl Städte in der Liste: {len(staedte)}")

# Der folgende Versuch würde einen TypeError auslösen:
# wismar[0] = 99
# => TypeError: 'tuple' object does not support item assignment
# Tupel sind unveränderlich (immutable). Nach ihrer Erstellung
# können ihre Elemente nicht mehr verändert werden. Das ist
# beabsichtigt und schützt Daten wie Koordinaten vor versehentlichen Änderungen.
