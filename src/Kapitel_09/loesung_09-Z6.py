# Aufgabe 09-Z6: Objekt-Persistenz mit JSON und pickle
# Musterlösung

import json
import pickle


class Kontakt:
    def __init__(self, name, email, telefon):
        self.name = name
        self.email = email
        self.telefon = telefon

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "telefon": self.telefon
        }

    def __str__(self):
        return f"{self.name} | {self.email} | {self.telefon}"


def kontakt_from_dict(data):
    return Kontakt(data["name"], data["email"], data["telefon"])


def speichere_kontakte_json(kontakte, dateiname):
    daten = [k.to_dict() for k in kontakte]
    with open(dateiname, "w", encoding="utf-8") as f:
        json.dump(daten, f, indent=4)
    print(f"{len(kontakte)} Kontakte als JSON gespeichert.")


def lade_kontakte_json(dateiname):
    try:
        with open(dateiname, "r", encoding="utf-8") as f:
            daten = json.load(f)
        return [kontakt_from_dict(d) for d in daten]
    except FileNotFoundError:
        print(f"Datei '{dateiname}' nicht gefunden.")
        return []


# Kontakte erstellen
kontakte = [
    Kontakt("Ada Lovelace", "ada@example.com", "0123-456789"),
    Kontakt("Alan Turing", "alan@example.com", "0987-654321"),
    Kontakt("Grace Hopper", "grace@example.com", "0111-222333"),
]

# JSON
speichere_kontakte_json(kontakte, "kontakte.json")
geladene_json = lade_kontakte_json("kontakte.json")
print(f"JSON geladen – {len(geladene_json)} Kontakte:")
for k in geladene_json:
    print(f"  {k}")

print()

# pickle
with open("kontakte.pkl", "wb") as f:
    pickle.dump(kontakte, f)
print(f"{len(kontakte)} Kontakte mit pickle gespeichert.")

with open("kontakte.pkl", "rb") as f:
    geladene_pkl = pickle.load(f)
print(f"Pickle geladen – {len(geladene_pkl)} Kontakte:")
for k in geladene_pkl:
    print(f"  {k}")
