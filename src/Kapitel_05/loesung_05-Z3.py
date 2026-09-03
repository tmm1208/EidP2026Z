# Aufgabe 05-Z3: Notenauswertung
# Musterlösung

noten = [2, 4, 1, 3, 5, 2, 1, 4, 3, 2]

anzahl = len(noten)
beste = min(noten)
schlechteste = max(noten)
durchschnitt = sum(noten) / len(noten)
note_1_vorhanden = 1 in noten
erster_index_1 = noten.index(1)

print(f"Anzahl Noten:     {anzahl}")
print(f"Beste Note:        {beste}")
print(f"Schlechteste Note: {schlechteste}")
print(f"Durchschnitt:      {durchschnitt}")
print(f"Note 1 vorhanden?: {note_1_vorhanden}")
print(f"Erster Index von 1: {erster_index_1}")
