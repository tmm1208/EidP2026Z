# Aufgabe 06-Z4: Duplikate entfernen und Mengen vergleichen
# Musterlösung

veranstaltung_a = ["Alice", "Bob", "Charlie", "Alice", "David", "Bob"]
veranstaltung_b = ["Charlie", "David", "Eva", "Frank", "Alice"]

set_a = set(veranstaltung_a)
set_b = set(veranstaltung_b)

print(f"Einzigartige Teilnehmer A: {set_a}")
print(f"Einzigartige Teilnehmer B: {set_b}")
print()
print(f"Alle Teilnehmer (Vereinigung):       {set_a | set_b}")
print(f"Beide Veranstaltungen (Schnittmenge): {set_a & set_b}")
print(f"Nur Veranstaltung A (Differenz):     {set_a - set_b}")
print(f"Genau eine Veranstaltung (Sym. Diff.): {set_a ^ set_b}")
