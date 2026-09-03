# Aufgabe 06-Z2: Sicherer Zugriff mit .get()
# Musterlösung

produkt = {
    "name": "Laptop",
    "preis": 999.99,
    "lagerbestand": 42
}

print(f"Name: {produkt['name']}")
print(f"Preis: {produkt['preis']} Euro")

# Der folgende Zugriff würde einen KeyError auslösen, da "rabatt"
# nicht im Dictionary existiert. [] wirft immer einen Fehler bei
# einem fehlenden Schlüssel – daher ist .get() die sichere Alternative.
# print(produkt["rabatt"])  # => KeyError: 'rabatt'

rabatt_ohne_default = produkt.get("rabatt")
print(f"\nRabatt (get ohne Default): {rabatt_ohne_default}")

rabatt_mit_default = produkt.get("rabatt", 0.0)
print(f"Rabatt (get mit Default):  {rabatt_mit_default}")
