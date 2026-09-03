# Aufgabe 04-Z6: Einkaufslisten-Assistent
# Musterlösung

einkaufsliste = []

while True:
    artikel = input("Artikel eingeben (oder 'fertig' zum Beenden): ")
    if artikel == "fertig":
        break
    if len(artikel) < 2:
        print("Zu kurz – Artikel wird ignoriert.")
        continue
    einkaufsliste.append(artikel)

print()
print("--- Deine Einkaufsliste ---")
for i in range(len(einkaufsliste)):
    print(f"{i + 1}. {einkaufsliste[i]}")
print("---------------------------")
print(f"Insgesamt {len(einkaufsliste)} Artikel.")
