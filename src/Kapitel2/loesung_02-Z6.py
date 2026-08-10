# Aufgabe 02-Z6: Variablen tauschen und Zuweisungsoperatoren
# Musterlösung

# --- Teil A: Variablen tauschen ---
punkte_spieler_a = int(input("Punkte Spieler A: "))
punkte_spieler_b = int(input("Punkte Spieler B: "))

print()
print("Vor dem Tausch:")
print(f"  Spieler A: {punkte_spieler_a}")
print(f"  Spieler B: {punkte_spieler_b}")

# Elegantes Tauschen in Python ohne Hilfsvariable
punkte_spieler_a, punkte_spieler_b = punkte_spieler_b, punkte_spieler_a

print()
print("Nach dem Tausch:")
print(f"  Spieler A: {punkte_spieler_a}")
print(f"  Spieler B: {punkte_spieler_b}")

# --- Teil B: Zuweisungsoperatoren ---
print()
print("--- Punktestand-Simulation ---")
punkte = 0
print(f"Start:              {punkte}")

punkte += 50
print(f"Nach += 50:        {punkte}")

punkte *= 3
print(f"Nach *= 3:        {punkte}")

punkte -= 30
print(f"Nach -= 30:       {punkte}")

punkte /= 2
print(f"Nach /= 2:         {punkte}")
