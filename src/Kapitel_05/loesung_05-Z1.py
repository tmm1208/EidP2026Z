# Aufgabe 05-Z1: Listenoperationen erkunden
# Musterlösung

plaene = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag"]

print(f"Erstes Element: {plaene[0]}")
print(f"Letztes Element: {plaene[-1]}")

plaene[2] = "Frei"
print(f"Nach Änderung: {plaene}")

plaene.append("Samstag")
print(f"Nach append: {plaene}")

del plaene[1]
print(f"Nach del: {plaene}")

print(f"Länge: {len(plaene)}")
