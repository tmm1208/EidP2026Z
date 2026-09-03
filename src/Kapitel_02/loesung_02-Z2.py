# Aufgabe 02-Z2: Kinoticket-Preisrechner
# Musterlösung

PREIS_PRO_TICKET = 12.50

anzahl = int(input("Anzahl Tickets: "))
gesamtpreis = anzahl * PREIS_PRO_TICKET
ueber_50 = gesamtpreis > 50

print(f"Anzahl:        {anzahl} Ticket(s)")
print(f"Preis pro Ticket: {PREIS_PRO_TICKET:.2f} Euro")
print(f"Gesamtpreis:   {gesamtpreis:.2f} Euro")
print(f"Über 50 Euro?  {ueber_50}")
