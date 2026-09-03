# Aufgabe 05-Z2: Slicing – Wochentage aufteilen
# Musterlösung

wochentage = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]

werktage = wochentage[:5]
wochenende = wochentage[5:]
wochenmitte = wochentage[1:4]
jeden_zweiten = wochentage[::2]
umgekehrt = wochentage[::-1]

print(f"Werktage:          {werktage}")
print(f"Wochenende:        {wochenende}")
print(f"Wochenmitte:       {wochenmitte}")
print(f"Jeden zweiten Tag: {jeden_zweiten}")
print(f"Umgekehrt:         {umgekehrt}")
