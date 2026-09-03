# Aufgabe 07-Z4: Rekursion – Summe und Potenz
# Musterlösung

def summe_bis(n):
    """Berechnet die Summe aller ganzen Zahlen von 1 bis n rekursiv."""
    if n == 0:
        return 0
    return n + summe_bis(n - 1)

def potenz(basis, exponent):
    """Berechnet basis hoch exponent rekursiv, ohne den **-Operator."""
    if exponent == 0:
        return 1
    return basis * potenz(basis, exponent - 1)

print(f"Summe 1 bis 5:  {summe_bis(5)}")
print(f"Summe 1 bis 10: {summe_bis(10)}")
print()
print(f"2 hoch 8:   {potenz(2, 8)}")
print(f"3 hoch 4:    {potenz(3, 4)}")
