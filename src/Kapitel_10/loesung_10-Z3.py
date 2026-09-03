# Aufgabe 10-Z3: NumPy – Vektorisierung erleben
# Musterlösung

import numpy as np

# Teil A: Celsius -> Fahrenheit (vektorisiert)
celsius = np.array([-10, 0, 20, 37, 100])
fahrenheit = celsius * 9 / 5 + 32

print(f"Celsius:    {celsius}")
print(f"Fahrenheit: {fahrenheit}")
print()

# Teil B: Elementweise Operationen
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

print(f"a + b: {a + b}")
print(f"a - b: {a - b}")
print(f"a * b: {a * b}")
print()

# Teil C: Aggregationen auf range 1-100
zahlen = np.arange(1, 101)
print(f"Summe 1-100:    {np.sum(zahlen)}")
print(f"Mittelwert:     {np.mean(zahlen)}")
print(f"Maximum:        {np.max(zahlen)}")
