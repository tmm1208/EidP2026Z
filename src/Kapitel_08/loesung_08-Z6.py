# Aufgabe 08-Z6: Bibliotheksverwaltung
# Musterlösung

class Buch:
    def __init__(self, titel, autor, isbn):
        self.titel = titel
        self.autor = autor
        self.isbn = isbn

    def __str__(self):
        return f"'{self.titel}' von {self.autor} (ISBN: {self.isbn})"

    def __eq__(self, other):
        if not isinstance(other, Buch):
            return NotImplemented
        return self.isbn == other.isbn


class Bibliothek:
    def __init__(self):
        self.buecher = []

    def buch_hinzufuegen(self, buch):
        if buch in self.buecher:
            print(f"Fehler: Buch mit ISBN {buch.isbn} ist bereits vorhanden.")
        else:
            self.buecher.append(buch)
            print(f"{buch} hinzugefügt.")

    def buch_suchen(self, titel):
        for buch in self.buecher:
            if titel.lower() in buch.titel.lower():
                return buch
        return None

    def alle_buecher(self):
        print("--- Alle Bücher ---")
        for i, buch in enumerate(self.buecher):
            print(f"{i + 1}. {buch}")
        print(f"Gesamt: {self.anzahl()} Bücher")

    def anzahl(self):
        return len(self.buecher)


bibliothek = Bibliothek()

b1 = Buch("Der Herr der Ringe", "Tolkien", "978-0-261-10235-4")
b2 = Buch("Clean Code", "Robert C. Martin", "978-0-13-235088-4")
b3 = Buch("Python Crashkurs", "Eric Matthes", "978-1-59327-603-4")
b4 = Buch("Der Herr der Ringe – Sonderausgabe", "Tolkien", "978-0-261-10235-4")

bibliothek.buch_hinzufuegen(b1)
bibliothek.buch_hinzufuegen(b2)
bibliothek.buch_hinzufuegen(b3)
bibliothek.buch_hinzufuegen(b4)

print()
bibliothek.alle_buecher()

print()
print("Suche nach 'clean':")
ergebnis = bibliothek.buch_suchen("clean")
if ergebnis:
    print(f"Gefunden: {ergebnis}")
else:
    print("Nicht gefunden.")

print()
print("Suche nach 'Java':")
ergebnis = bibliothek.buch_suchen("Java")
if ergebnis:
    print(f"Gefunden: {ergebnis}")
else:
    print("Nicht gefunden.")
