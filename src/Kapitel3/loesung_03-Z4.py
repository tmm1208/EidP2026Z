# Aufgabe 03-Z4: Versandkostenrechner
# Musterlösung

VERSAND_KOSTENLOS = 0.00
VERSAND_GUENSTIG = 2.99
VERSAND_TEUER = 4.99
SCHWELLE_KOSTENLOS = 50
SCHWELLE_GUENSTIG = 20

bestellwert = float(input("Bestellwert (Euro): "))
ist_premium = input("Premium-Mitglied (ja/nein): ") == "ja"

if ist_premium:
    versandkosten = VERSAND_KOSTENLOS
else:
    if bestellwert > SCHWELLE_KOSTENLOS:
        versandkosten = VERSAND_KOSTENLOS
    elif bestellwert >= SCHWELLE_GUENSTIG:
        versandkosten = VERSAND_GUENSTIG
    else:
        versandkosten = VERSAND_TEUER

print(f"Bestellwert:    {bestellwert:.2f} Euro")
print(f"Versandkosten:   {versandkosten:.2f} Euro")
