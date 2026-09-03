# Aufgabe 08-Z2: Methoden und Validierung
# Musterlösung

class Buch:
    def __init__(self, titel, autor, seiten):
        self.titel = titel
        self.autor = autor
        self.seiten = seiten
        self.ist_ausgeliehen = False
        self.ausgeliehen_von = None

    def __str__(self):
        return f"'{self.titel}' von {self.autor} ({self.seiten} Seiten)"

    def ausleihen(self, nutzername):
        if self.ist_ausgeliehen:
            print(f"'{self.titel}' ist bereits ausgeliehen!")
        else:
            self.ist_ausgeliehen = True
            self.ausgeliehen_von = nutzername
            print(f"'{self.titel}' wurde an {nutzername} ausgeliehen.")

    def zurueckgeben(self):
        if not self.ist_ausgeliehen:
            print("Das Buch ist nicht ausgeliehen.")
        else:
            self.ist_ausgeliehen = False
            self.ausgeliehen_von = None
            print(f"'{self.titel}' wurde zurückgegeben.")

    def status(self):
        if self.ist_ausgeliehen:
            return f"Ausgeliehen von {self.ausgeliehen_von}"
        return "Verfügbar"


buch = Buch("Clean Code", "Robert C. Martin", 464)
print(f"Status: {buch.status()}")
buch.ausleihen("Alice")
print(f"Status: {buch.status()}")
buch.ausleihen("Bob")
buch.zurueckgeben()
print(f"Status: {buch.status()}")
buch.zurueckgeben()
