# Aufgabe 06-Z6: Kursverwaltung mit Dicts und Sets
# Musterlösung

kurs_python = {
    "titel": "Python Grundlagen",
    "dozent": "Prof. Pieper",
    "teilnehmer": {"Anna", "Ben", "Clara", "David", "Eva"}
}

kurs_datenbanken = {
    "titel": "Datenbanken",
    "dozent": "Prof. Müller",
    "teilnehmer": {"Clara", "David", "Frank", "Grace", "Ben"}
}

print("--- Kursübersicht ---")
print(f"Kurs 1: {kurs_python['titel']} (Dozent: {kurs_python['dozent']}, Teilnehmer: {len(kurs_python['teilnehmer'])})")
print(f"Kurs 2: {kurs_datenbanken['titel']} (Dozent: {kurs_datenbanken['dozent']}, Teilnehmer: {len(kurs_datenbanken['teilnehmer'])})")

tp = kurs_python["teilnehmer"]
td = kurs_datenbanken["teilnehmer"]

print()
print("--- Auswertung ---")
print(f"Belegen beide Kurse:          {tp & td}")
print(f"Belegen mind. einen Kurs:     {tp | td}")
print(f"Nur Python (nicht Datenbank): {tp - td}")
print(f"Einzigartige Studierende gesamt: {len(tp | td)}")
