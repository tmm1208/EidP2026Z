# Aufgabe 08-Z3: __repr__ und __eq__
# Musterlösung

import math

class Koordinate:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Punkt({self.x}, {self.y})"

    def __repr__(self):
        return f"Koordinate({self.x}, {self.y})"

    def __eq__(self, other):
        if not isinstance(other, Koordinate):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def abstand_zum_ursprung(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)


a = Koordinate(3.0, 4.0)
b = Koordinate(3.0, 4.0)
c = Koordinate(1.0, 2.0)

print(f"str:  {str(a)}")
print(f"repr: {repr(a)}")
print(f"Abstand zum Ursprung: {a.abstand_zum_ursprung()}")
print()
print(f"a == b: {a == b}")
print(f"a == c: {a == c}")
print(f"a is b: {a is b}")
