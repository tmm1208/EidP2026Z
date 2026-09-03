# Aufgabe 08-Z5: Vererbung – Fahrzeuge
# Musterlösung

class Fahrzeug:
    def __init__(self, marke, baujahr):
        self.marke = marke
        self.baujahr = baujahr

    def beschreibung(self):
        return f"Fahrzeug: {self.marke}, Baujahr {self.baujahr}"


class Auto(Fahrzeug):
    def __init__(self, marke, baujahr, tueren):
        super().__init__(marke, baujahr)
        self.tueren = tueren

    def beschreibung(self):
        basis = super().beschreibung().replace("Fahrzeug", "Auto")
        return f"{basis}, {self.tueren} Türen"


class Motorrad(Fahrzeug):
    def __init__(self, marke, baujahr, hat_beiwagen):
        super().__init__(marke, baujahr)
        self.hat_beiwagen = hat_beiwagen

    def beschreibung(self):
        basis = super().beschreibung().replace("Fahrzeug", "Motorrad")
        beiwagen = "Ja" if self.hat_beiwagen else "Nein"
        return f"{basis}, Beiwagen: {beiwagen}"


fahrzeug = Fahrzeug("BMW", 2020)
auto = Auto("Toyota", 2022, 5)
motorrad = Motorrad("Harley-Davidson", 2019, False)

print(fahrzeug.beschreibung())
print(auto.beschreibung())
print(motorrad.beschreibung())
print()
print(f"Baujahr des Autos (aus Basisklasse): {auto.baujahr}")
