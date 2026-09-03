# Aufgabe 06-Z3: Häufigkeitszähler
# Musterlösung

text = "die katze sitzt auf der matte die matte ist weich die katze auch"

woerter = text.split()
haeufigkeit = {}

for wort in woerter:
    haeufigkeit[wort] = haeufigkeit.get(wort, 0) + 1

print("Worthäufigkeiten:")
for wort, anzahl in haeufigkeit.items():
    print(f"{wort}: {anzahl}")
