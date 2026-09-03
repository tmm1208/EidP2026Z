# Aufgabe 09-Z2: Anhängen mit Append-Modus
# Musterlösung

# Erster Eintrag – Datei wird neu erstellt (oder überschrieben)
with open("notizen.txt", "w", encoding="utf-8") as f:
    f.write("Eintrag 1: Python macht Spaß.\n")

print("notizen.txt nach erstem Eintrag:")
with open("notizen.txt", "r", encoding="utf-8") as f:
    print(f.read().strip())

print()

# Zweiter Eintrag – wird ans Ende angehängt
with open("notizen.txt", "a", encoding="utf-8") as f:
    f.write("Eintrag 2: Dateien zu schreiben ist einfach.\n")

print("notizen.txt nach zweitem Eintrag:")
with open("notizen.txt", "r", encoding="utf-8") as f:
    print(f.read().strip())
