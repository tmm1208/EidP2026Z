# Aufgabe 08-Z1: Erste Klasse – Buch
# Musterlösung

class Buch:
    def __init__(self, titel, autor, seiten):
        self.titel = titel
        self.autor = autor
        self.seiten = seiten

    def __str__(self):
        return f"'{self.titel}' von {self.autor} ({self.seiten} Seiten)"


buch1 = Buch("Der Herr der Ringe", "Tolkien", 1178)
buch2 = Buch("Clean Code", "Robert C. Martin", 464)

print(buch1)
print(buch2)
print(f"Titel des ersten Buches: {buch1.titel}")
print(f"Autor des zweiten Buches: {buch2.autor}")
