# Aufgabe 07-Z6: Taschenrechner mit Funktionen
# Musterlösung

def addiere(a: float, b: float) -> float:
    """Addiert zwei Zahlen und gibt das Ergebnis zurück."""
    return a + b

def subtrahiere(a: float, b: float) -> float:
    """Subtrahiert b von a und gibt das Ergebnis zurück."""
    return a - b

def multipliziere(a: float, b: float) -> float:
    """Multipliziert zwei Zahlen und gibt das Ergebnis zurück."""
    return a * b

def dividiere(a: float, b: float) -> float:
    """
    Dividiert a durch b und gibt das Ergebnis zurück.
    Gibt None zurück und gibt eine Fehlermeldung aus, wenn b == 0.
    """
    if b == 0:
        print("Fehler: Division durch null nicht erlaubt.")
        return None
    return a / b

operationen = {
    "add": addiere,
    "sub": subtrahiere,
    "mul": multipliziere,
    "div": dividiere,
}

while True:
    befehl = input("Operation (add/sub/mul/div/quit): ")

    if befehl == "quit":
        print("Tschüss!")
        break

    if befehl not in operationen:
        print("Unbekannte Operation. Verfügbar: add, sub, mul, div, quit")
        continue

    a = float(input("Zahl 1: "))
    b = float(input("Zahl 2: "))

    ergebnis = operationen[befehl](a, b)
    if ergebnis is not None:
        print(f"Ergebnis: {ergebnis}")
    print()
