# Aufgabe 09-Z1: Textdatei schreiben und lesen
# Musterlösung

staedte = ["Berlin", "Hamburg", "München", "Wismar", "Rostock"]

with open("staedte.txt", "w", encoding="utf-8") as f:
    for stadt in staedte:
        f.write(f"{stadt}\n")

print("Datei 'staedte.txt' geschrieben.")
print()
print("Inhalt von 'staedte.txt':")

with open("staedte.txt", "r", encoding="utf-8") as f:
    for zeile in f:
        print(zeile.strip())
