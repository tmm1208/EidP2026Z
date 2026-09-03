# Aufgabe 08-Z4: Property und Validierung
# Musterlösung

ABSOLUTER_NULLPUNKT = -273.15

class Temperatur:
    def __init__(self, celsius: float):
        self._celsius = 0.0
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, wert: float):
        if wert < ABSOLUTER_NULLPUNKT:
            print(f"Fehler: {wert}°C liegt unter dem absoluten Nullpunkt ({ABSOLUTER_NULLPUNKT}°C).")
        else:
            self._celsius = wert

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    def __str__(self):
        return f"Temperatur: {self._celsius}°C ({self.fahrenheit}°F)"


t = Temperatur(20.0)
print(t)
t.celsius = -10.0
print(t)
t.celsius = -300.0
print(t)
print(f"Temperatur in Fahrenheit: {t.fahrenheit}°F")
