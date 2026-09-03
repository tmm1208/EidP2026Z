# Aufgabe 04-Z3: Summen mit range() und Schrittweite
# Musterlösung

# Summe gerader Zahlen von 2 bis 100
summe_gerade = 0
for i in range(2, 101, 2):
    summe_gerade += i

# Summe ungerader Zahlen von 1 bis 99
summe_ungerade = 0
for i in range(1, 100, 2):
    summe_ungerade += i

# Summe durch 5 teilbarer Zahlen von 5 bis 50
summe_fuenfer = 0
for i in range(5, 51, 5):
    summe_fuenfer += i

print(f"Summe gerader Zahlen (2-100):    {summe_gerade}")
print(f"Summe ungerader Zahlen (1-99):   {summe_ungerade}")
print(f"Summe durch 5 teilbar (5-50):     {summe_fuenfer}")
