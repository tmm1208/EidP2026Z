
# Zusätzliche Übungsaufgaben zum Kapitel 10: Ausblick – Python in der Praxis
*(Gesamtzeit: ca. 90-120 Min)*

Diese Aufgaben ergänzen die regulären Übungen zu Kapitel 10. Du erkundest Web-APIs, die `requests`-Bibliothek, NumPy und Pandas in neuen, praxisnahen Szenarien.

> 💡 **Hinweis:** Für dieses Kapitel benötigst du externe Bibliotheken. Installiere sie im Terminal mit:
> ```
> uv add requests numpy pandas seaborn matplotlib
> ```

#### Aufgaben zu Kapitel 10 - Zusatz
- [ ] Aufgabe 10-Z1
- [ ] Aufgabe 10-Z2
- [ ] Aufgabe 10-Z3
- [ ] Aufgabe 10-Z4
- [ ] Aufgabe 10-Z5
- [ ] Aufgabe 10-Z6

---

## Aufgabe 10-Z1: HTTP-Anfrage und Statuscode
*(ca. 10 Minuten)*

**Nutze die Datei `src/kapitel_10/aufgabe_10-Z1.py` für Deine Lösung.**

**Aufgabenstellung:**
Schreibe ein Programm, das mit `requests.get()` eine Anfrage an die folgende URL stellt und den HTTP-Statuscode sowie einen Teil der Antwort ausgibt:

```
https://api.open-meteo.com/v1/forecast?latitude=53.89&longitude=11.45&current_weather=true
```

1. Gib den HTTP-Statuscode aus (`response.status_code`).
2. Prüfe mit `response.raise_for_status()`, ob die Anfrage erfolgreich war.
3. Wandle die Antwort mit `response.json()` in ein Dictionary um.
4. Gib die aktuelle Temperatur und Windgeschwindigkeit formatiert aus.
5. Fange mögliche Fehler mit `try/except requests.exceptions.RequestException` ab.

**Lernziele:**
- `requests.get()` für eine HTTP-GET-Anfrage einsetzen.
- Den Statuscode einer HTTP-Antwort auslesen und interpretieren.
- `raise_for_status()` zur automatischen Fehlerprüfung nutzen.
- `.json()` zum Parsen der JSON-Antwort in ein Python-Dictionary verwenden.
- Netzwerkfehler mit `requests.exceptions.RequestException` abfangen.

***Hinweise:***
- Die URL liefert Wetterdaten für Wismar (Breite 53.89, Länge 11.45).
- Die Temperaturdaten liegen unter `response_dict["current_weather"]["temperature"]`.

**Erwartetes Ergebnis:**

```
Statuscode: 200
Aktuelles Wetter in Wismar:
  Temperatur: X.X°C
  Wind: XX.X km/h
```

*(Die genauen Werte hängen vom aktuellen Wetter ab.)*

---

## Aufgabe 10-Z2: Mehrere API-Parameter nutzen
*(ca. 15 Minuten)*

**Nutze die Datei `src/kapitel_10/aufgabe_10-Z2.py` für Deine Lösung.**

**Aufgabenstellung:**
Erweitere Aufgabe 10-Z1: Rufe für **drei verschiedene Städte** Wetterdaten ab und gib sie vergleichend aus.

Koordinaten:
- Wismar: `latitude=53.89, longitude=11.45`
- Hamburg: `latitude=53.57, longitude=10.02`
- München: `latitude=48.14, longitude=11.58`

Speichere die Städte als Liste von Dictionaries direkt im Code und iteriere mit einer `for`-Schleife über sie.

**Lernziele:**
- Eine API mehrfach mit unterschiedlichen Parametern aufrufen.
- URL-Parameter dynamisch aus Variablen zusammenbauen (f-String).
- Mehrere API-Antworten strukturiert verarbeiten und vergleichen.

***Hinweise:***
- Baue die URL mit einem f-String: `f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"`
- Fange Fehler pro Schleifendurchlauf ab, damit ein Fehler nicht alle anderen Abfragen abbricht.

**Erwartetes Ergebnis:**

```
Wismar:  X.X°C | Wind: XX.X km/h
Hamburg: X.X°C | Wind: XX.X km/h
München: X.X°C | Wind: XX.X km/h
```

---

## Aufgabe 10-Z3: NumPy – Vektorisierung erleben
*(ca. 15 Minuten)*

**Nutze die Datei `src/kapitel_10/aufgabe_10-Z3.py` für Deine Lösung.**

**Aufgabenstellung:**
Löse alle drei Teilaufgaben mit NumPy, ohne Python-for-Schleifen zu verwenden:

**Teil A:** Gegeben ist ein Array von Temperaturen in Celsius:
```python
celsius = np.array([-10, 0, 20, 37, 100])
```
Wandle alle Werte in Fahrenheit um (Formel: `F = C * 9/5 + 32`) – vektorisiert in einer Zeile.

**Teil B:** Gegeben sind zwei Arrays:
```python
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])
```
Berechne die elementweise Summe, Differenz und das Produkt – jeweils in einer Zeile.

**Teil C:** Erzeuge mit `np.arange(1, 101)` ein Array der Zahlen 1 bis 100 und berechne:
- Die Summe aller Zahlen (`np.sum()`)
- Den Mittelwert (`np.mean()`)
- Den größten Wert (`np.max()`)

**Lernziele:**
- NumPy-Arrays erstellen und Grundoperationen darauf anwenden.
- Vektorisierung verstehen: Operationen gelten für alle Elemente gleichzeitig.
- NumPy-Aggregationsfunktionen (`sum`, `mean`, `max`) einsetzen.
- Den Vorteil gegenüber einer Python-Schleife erkennen (Kürze, Lesbarkeit).

**Erwartetes Ergebnis:**

```
Celsius:    [-10   0  20  37 100]
Fahrenheit: [ 14.  32.  68.  98.6 212. ]

a + b: [11 22 33 44 55]
a - b: [ -9 -18 -27 -36 -45]
a * b: [ 10  40  90 160 250]

Summe 1-100:    5050
Mittelwert:     50.5
Maximum:        100
```

---

## Aufgabe 10-Z4: Pandas – DataFrame erkunden
*(ca. 20 Minuten)*

**Nutze die Datei `src/kapitel_10/aufgabe_10-Z4.py` für Deine Lösung.**

**Aufgabenstellung:**
Erstelle direkt im Code einen Pandas DataFrame mit Studentendaten:

```python
import pandas as pd

daten = {
    "name":       ["Alice", "Bob", "Charlie", "Diana", "Eva"],
    "studiengang": ["Informatik", "BWL", "Informatik", "Medizin", "BWL"],
    "note":        [1.7, 2.3, 1.3, 2.0, 3.0],
    "semester":    [3, 5, 1, 7, 3]
}
```

Führe folgende Analysen durch:
1. Gib die ersten 3 Zeilen mit `.head(3)` aus.
2. Gib eine statistische Zusammenfassung mit `.describe()` aus.
3. Filtere alle Informatik-Studierenden.
4. Berechne den Notendurchschnitt pro Studiengang mit `.groupby()`.
5. Sortiere den DataFrame nach Note aufsteigend mit `.sort_values()`.

**Lernziele:**
- Einen Pandas DataFrame aus einem Dictionary erstellen.
- `.head()`, `.describe()` zur Datenübersicht einsetzen.
- Zeilen mit einer Bedingung filtern (`df[df["spalte"] == wert]`).
- `.groupby()` mit einer Aggregationsfunktion kombinieren.
- `.sort_values()` zur Sortierung des DataFrames verwenden.

**Erwartetes Ergebnis:**

```
--- Erste 3 Zeilen ---
      name studiengang  note  semester
0    Alice  Informatik   1.7         3
1      Bob         BWL   2.3         5
2  Charlie  Informatik   1.3         1

--- Statistik ---
       note  semester
...

--- Nur Informatik ---
      name studiengang  note  semester
0    Alice  Informatik   1.7         3
2  Charlie  Informatik   1.3         1

--- Notendurchschnitt pro Studiengang ---
studiengang
BWL           2.65
Informatik    1.50
Medizin       2.00

--- Sortiert nach Note ---
      name studiengang  note  semester
2  Charlie  Informatik   1.3         1
...
```

---

## Aufgabe 10-Z5: Pandas – CSV laden und auswerten
*(ca. 20 Minuten)*

**Nutze die Datei `src/kapitel_10/aufgabe_10-Z5.py` für Deine Lösung.**

**Aufgabenstellung:**
Lade den Palmer-Penguins-Datensatz direkt aus dem Internet und werte ihn aus:

```python
url = "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins.csv"
```

1. Lade den Datensatz mit `pd.read_csv(url)` in einen DataFrame.
2. Gib die Anzahl der Zeilen und Spalten aus (`df.shape`).
3. Gib die Spaltennamen aus (`df.columns`).
4. Gib aus, wie viele Pinguine jeder Art enthalten sind (`df["species"].value_counts()`).
5. Berechne die mittlere Körpermasse pro Art mit `groupby()`.
6. Fange einen möglichen Fehler beim Laden mit `try/except` ab.

**Lernziele:**
- Einen Datensatz direkt per URL mit `pd.read_csv()` laden.
- Die grundlegenden Eigenschaften eines DataFrames erkunden (`.shape`, `.columns`).
- `value_counts()` für eine schnelle Häufigkeitsauswertung einsetzen.
- `.groupby()` mit `.mean()` zur Gruppenauswertung kombinieren.
- Netzwerkfehler bei der Datenbeschaffung mit `try/except` abfangen.

**Erwartetes Ergebnis:**

```
Form: (344, 8)
Spalten: Index(['species', 'island', 'bill_length_mm', ...])

Anzahl pro Art:
Adelie       152
Gentoo        124
Chinstrap      68

Mittlere Körpermasse pro Art (g):
species
Adelie       3700.662252
Chinstrap    3733.088235
Gentoo       5076.016260
```

---

## Aufgabe 10-Z6: API-Daten in Pandas analysieren
*(Integrationsaufgabe, ca. 30 Minuten)*

**Nutze die Datei `src/kapitel_10/aufgabe_10-Z6.py` für Deine Lösung.**

**Aufgabenstellung:**
Kombiniere alle Konzepte des Kapitels: Rufe für mindestens fünf Städte Wetterdaten ab und analysiere sie mit Pandas.

1. Definiere eine Liste von mindestens 5 Städten mit Name, Breitengrad und Längengrad.
2. Rufe für jede Stadt die aktuelle Temperatur und Windgeschwindigkeit über die Open-Meteo-API ab.
3. Speichere die Ergebnisse in einer Liste von Dictionaries.
4. Erstelle aus der Liste einen Pandas DataFrame.
5. Gib den DataFrame tabellarisch aus.
6. Berechne und gib aus: die Stadt mit der höchsten Temperatur, die Stadt mit der niedrigsten Temperatur und die mittlere Windgeschwindigkeit aller Städte.

**Lernziele:**
- API-Aufrufe mit Schleifen und `requests` strukturiert durchführen.
- Ergebnisse mehrerer API-Aufrufe in einer Datenstruktur sammeln.
- Aus einer Liste von Dictionaries einen Pandas DataFrame erstellen.
- DataFrame-Methoden (`idxmax()`, `idxmin()`, `.mean()`) für eine einfache Auswertung einsetzen.
- Fehlerbehandlung für einzelne API-Aufrufe integrieren, sodass ein Fehler nicht das gesamte Programm abbricht.

***Hinweise:***
- `df.loc[df["temperatur"].idxmax(), "stadt"]` gibt den Namen der wärmsten Stadt zurück.
- Fange Fehler pro Schleifendurchlauf ab und überspringe fehlerhafte Städte mit `continue`.

**Erwartetes Ergebnis:**

```
--- Wetterübersicht ---
        stadt  temperatur  windgeschwindigkeit
0      Wismar        X.X                 XX.X
1     Hamburg        X.X                 XX.X
2      Berlin        X.X                 XX.X
3      München       X.X                 XX.X
4      Rostock       X.X                 XX.X

Wärmste Stadt:        München (X.X°C)
Kälteste Stadt:       Rostock (X.X°C)
Mittlere Windstärke:  XX.X km/h
```

*(Genaue Werte hängen vom aktuellen Wetter ab.)*
