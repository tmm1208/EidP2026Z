# Aufgabe 03-Z6: Fahrpreisrechner
# Musterlösung

PREIS_PRO_KM = 0.15
BAHNCARD_RABATT = 0.25

alter = int(input("Alter: "))
strecke = int(input("Strecke (km): "))
hat_bahncard = input("Bahncard (ja/nein): ") == "ja"

print()
print("--- Fahrpreisberechnung ---")

if alter < 6:
    altersgruppe = "Kind (unter 6, kostenlos)"
    basispreis = 0.00
elif alter <= 14:
    altersgruppe = "Kind (6-14, halber Preis)"
    basispreis = strecke * PREIS_PRO_KM * 0.5
elif alter >= 65:
    altersgruppe = "Senior (ab 65, halber Preis)"
    basispreis = strecke * PREIS_PRO_KM * 0.5
else:
    altersgruppe = "Erwachsener (voller Preis)"
    basispreis = strecke * PREIS_PRO_KM

print(f"Altersgruppe:  {altersgruppe}")

if basispreis == 0.00:
    print(f"Endpreis:      {basispreis:.2f} Euro")
else:
    print(f"Basispreis:    {basispreis:.2f} Euro")
    if hat_bahncard:
        rabatt = basispreis * BAHNCARD_RABATT
        endpreis = basispreis - rabatt
        print(f"Bahncard-Rabatt: -{rabatt:.2f} Euro")
    else:
        endpreis = basispreis
    print(f"Endpreis:      {endpreis:.2f} Euro")
