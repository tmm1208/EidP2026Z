# Aufgabe 02-Z3: Kilometerrechner
# Musterlösung

METER_PRO_KM = 1000
MEILEN_PRO_KM = 0.621371
SEEMEILEN_PRO_KM = 0.539957

km = float(input("Entfernung in km: "))

meter = km * METER_PRO_KM
meilen = km * MEILEN_PRO_KM
seemeilen = km * SEEMEILEN_PRO_KM

print()
print("--- Umrechnung ---")
print(f"{km} km = {meter} m")
print(f"{km} km = {meilen:.4f} Meilen")
print(f"{km} km = {seemeilen:.4f} Seemeilen")
