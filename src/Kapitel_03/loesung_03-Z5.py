# Aufgabe 03-Z5: Noten-Umrechner mit ternärem Operator
# Musterlösung

punkte = int(input("Punkte (0-100): "))

# Note per if-elif-else ermitteln
if punkte >= 90:
    note = 1
elif punkte >= 75:
    note = 2
elif punkte >= 60:
    note = 3
elif punkte >= 50:
    note = 4
elif punkte >= 25:
    note = 5
else:
    note = 6

# Bestanden/Nicht bestanden per ternärem Operator
status = "bestanden" if punkte >= 50 else "nicht bestanden"

print(f"Note:     {note}")
print(f"Status:   {status}")
