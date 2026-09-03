# Aufgabe 06-Z1: Steckbrief als Dictionary
# Musterlösung

person = {
    "name": "Ada Lovelace",
    "alter": 36,
    "stadt": "London",
    "beruf": "Programmiererin"
}

print(f"Name: {person['name']} | Stadt: {person['stadt']}")

person["beruf"] = "Mathematikerin"
print(f"Nach Änderung: {person}")

person["sprachen"] = ["Englisch", "Französisch"]
print(f"Nach append: {person}")

del person["alter"]
print(f"Nach del: {person}")

print()
print("--- Alle Einträge ---")
for key, value in person.items():
    print(f"{key}: {value}")
