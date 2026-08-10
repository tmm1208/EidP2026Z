# Aufgabe 02-Z5: Brutto-Netto-Rechner
# Musterlösung

UST_ERMAESSIGT = 0.07
UST_REGULAER = 0.19

netto = float(input("Netto-Preis (Euro): "))

steuer_7 = netto * UST_ERMAESSIGT
brutto_7 = netto * (1 + UST_ERMAESSIGT)

steuer_19 = netto * UST_REGULAER
brutto_19 = netto * (1 + UST_REGULAER)

print()
print("--- Preisübersicht ---")
print(f"Netto:                    {netto:.2f} Euro")
print()
print("Mit 7% MwSt. (ermäßigt):")
print(f"  Steuer:                   {steuer_7:.2f} Euro")
print(f"  Brutto:                 {brutto_7:.2f} Euro")
print()
print("Mit 19% MwSt. (regulär):")
print(f"  Steuer:                  {steuer_19:.2f} Euro")
print(f"  Brutto:                 {brutto_19:.2f} Euro")
