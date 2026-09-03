# Aufgabe 04-Z5: Rückwärtszähler und Quersumme
# Musterlösung

zahl = int(input("Zahl: "))

# Rückwärtszähler mit while
counter = zahl
while counter >= 1:
    print(counter, end=" ")
    counter -= 1
print("Start!")

# Quersumme mit for
quersumme = 0
for ziffer in str(zahl):
    quersumme += int(ziffer)

print(f"Quersumme von {zahl}: {quersumme}")
