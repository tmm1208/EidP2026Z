# Aufgabe 05-Z5: List Comprehensions
# Musterlösung

# Teilaufgabe A: Celsius -> Fahrenheit
temperaturen_celsius = [0, 20, 37, 100, -10]
temperaturen_fahrenheit = [c * 9/5 + 32 for c in temperaturen_celsius]

print(f"Celsius:    {temperaturen_celsius}")
print(f"Fahrenheit: {temperaturen_fahrenheit}")
print()

# Teilaufgabe B: Lange Wörter filtern
woerter = ["Hallo", "Welt", "Python", "ist", "toll", "super"]
lange_woerter = [w for w in woerter if len(w) > 4]

print(f"Alle Wörter:   {woerter}")
print(f"Lange Wörter:  {lange_woerter}")
print()

# Teilaufgabe C: Quadrate ungerader Zahlen 1-20
quadratzahlen = [i * i for i in range(1, 21) if i % 2 != 0]
print(f"Quadrate ungerader Zahlen (1-20): {quadratzahlen}")
