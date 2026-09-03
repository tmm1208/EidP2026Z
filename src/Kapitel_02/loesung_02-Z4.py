# Aufgabe 02-Z4: Ganzzahldivision und Modulo – Zeitrechner
# Musterlösung

minuten_gesamt = int(input("Minuten gesamt: "))

stunden = minuten_gesamt // 60
rest_minuten = minuten_gesamt % 60

print(f"{minuten_gesamt} Minuten sind:")
print(f"{stunden} Stunden und {rest_minuten} Minuten.")
