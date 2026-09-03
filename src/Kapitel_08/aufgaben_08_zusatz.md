
# Zusätzliche Übungsaufgaben zum Kapitel 08: Objektorientierung – Objekte, Klassen, Assoziationen & Module
*(Gesamtzeit: ca. 90-120 Min)*

Diese Aufgaben ergänzen die regulären Übungen zu Kapitel 08. Du übst Klassen, Konstruktoren, Methoden, Dunder-Methoden, Properties und Vererbung in neuen, praxisnahen Szenarien.

#### Aufgaben zu Kapitel 08 - Zusatz
- [ ] Aufgabe 08-Z1
- [ ] Aufgabe 08-Z2
- [ ] Aufgabe 08-Z3
- [ ] Aufgabe 08-Z4
- [ ] Aufgabe 08-Z5
- [ ] Aufgabe 08-Z6

---

## Aufgabe 08-Z1: Erste Klasse – Buch
*(ca. 10 Minuten)*

**Nutze die Datei `src/kapitel_08/aufgabe_08-Z1.py` für Deine Lösung.**

**Aufgabenstellung:**
Definiere eine Klasse `Buch` mit folgenden Attributen im Konstruktor: `titel`, `autor` und `seiten`. Implementiere außerdem eine `__str__`-Methode, die eine lesbare Darstellung des Buches zurückgibt.

Erzeuge anschließend zwei Buch-Objekte und gib sie mit `print()` aus. Greife dann auf einzelne Attribute beider Objekte zu.

**Lernziele:**
- Eine eigene Klasse mit `__init__` und `self` definieren.
- Den Unterschied zwischen Klasse (Bauplan) und Objekt (Instanz) praktisch erleben.
- `__str__` implementieren, damit `print()` eine lesbare Ausgabe liefert.

**Erwartetes Ergebnis:**

```
'Der Herr der Ringe' von Tolkien (1178 Seiten)
'Clean Code' von Robert C. Martin (464 Seiten)
Titel des ersten Buches: Der Herr der Ringe
Autor des zweiten Buches: Robert C. Martin
```

---

## Aufgabe 08-Z2: Methoden und Validierung
*(ca. 15 Minuten)*

**Nutze die Datei `src/kapitel_08/aufgabe_08-Z2.py` für Deine Lösung.**

**Aufgabenstellung:**
Erweitere die Klasse `Buch` aus Aufgabe 08-Z1 um eine Verwaltungsfunktion für Ausleihen. Füge folgende Methoden hinzu:

1. `ausleihen(nutzername)`: Markiert das Buch als ausgeliehen (speichere den Nutzernamen und setze ein `ist_ausgeliehen`-Flag auf `True`). Gibt eine Fehlermeldung aus, wenn das Buch schon ausgeliehen ist.
2. `zurueckgeben()`: Setzt das Buch wieder als verfügbar (setzt `ist_ausgeliehen` auf `False` und `ausgeliehen_von` auf `None`). Gibt eine Fehlermeldung aus, wenn das Buch gar nicht ausgeliehen ist.
3. `status()`: Gibt einen String zurück, der den aktuellen Ausleihstatus beschreibt.

**Lernziele:**
- Methoden mit Zustandsverwaltung implementieren.
- `self` nutzen, um Attribute innerhalb von Methoden zu lesen und zu schreiben.
- Einfache Validierungslogik innerhalb von Methoden umsetzen.

**Erwartetes Ergebnis:**

```
Status: Verfügbar
'Clean Code' wurde an Alice ausgeliehen.
Status: Ausgeliehen von Alice
'Clean Code' ist bereits ausgeliehen!
'Clean Code' wurde zurückgegeben.
Status: Verfügbar
Das Buch ist nicht ausgeliehen.
```

---

## Aufgabe 08-Z3: __repr__ und __eq__
*(ca. 15 Minuten)*

**Nutze die Datei `src/kapitel_08/aufgabe_08-Z3.py` für Deine Lösung.**

**Aufgabenstellung:**
Definiere eine Klasse `Koordinate` mit den Attributen `x` und `y` (beide `float`). Implementiere:

1. `__str__`: Lesbare Darstellung, z.B. `"Punkt(3.0, 4.0)"`.
2. `__repr__`: Eindeutige, reproduzierbare Darstellung, z.B. `"Koordinate(3.0, 4.0)"`.
3. `__eq__`: Zwei Koordinaten gelten als gleich, wenn sowohl `x` als auch `y` übereinstimmen.
4. Eine Methode `abstand_zum_ursprung()`: Gibt den Abstand zum Ursprung (0, 0) zurück. Formel: `sqrt(x**2 + y**2)` (nutze `import math`).

Erzeuge zwei identische und ein verschiedenes Koordinaten-Objekt und teste alle Methoden.

**Lernziele:**
- Den Unterschied zwischen `__str__` (Endnutzer) und `__repr__` (Entwickler) in der Praxis umsetzen.
- `__eq__` definieren, um inhaltliche Gleichheit statt Identität zu prüfen.
- Eine Methode mit einer mathematischen Berechnung implementieren.

**Erwartetes Ergebnis:**

```
str:  Punkt(3.0, 4.0)
repr: Koordinate(3.0, 4.0)
Abstand zum Ursprung: 5.0

a == b: True
a == c: False
a is b: False
```

---

## Aufgabe 08-Z4: Property und Validierung
*(ca. 20 Minuten)*

**Nutze die Datei `src/kapitel_08/aufgabe_08-Z4.py` für Deine Lösung.**

**Aufgabenstellung:**
Definiere eine Klasse `Temperatur`, die eine Temperatur in Celsius speichert und folgende Anforderungen erfüllt:

1. Das Attribut `celsius` soll über eine `@property` mit Getter und Setter gesichert werden. Der Setter soll Temperaturen unter -273.15°C (absoluter Nullpunkt) ablehnen und eine Fehlermeldung ausgeben.
2. Eine Property `fahrenheit` (nur Getter, kein Setter), die die Temperatur in Fahrenheit zurückgibt. Formel: `F = C * 9/5 + 32`.
3. Eine `__str__`-Methode: `"Temperatur: 20.0°C (68.0°F)"`.

Teste die Klasse mit gültigen und ungültigen Werten.

**Lernziele:**
- `@property` und `@attribut.setter` für kontrollierten Zugriff implementieren.
- Eine berechnete Property (nur Getter) definieren.
- Den absoluten Nullpunkt als Validierungsgrenze einsetzen.

***Hinweise:***
- Das interne Attribut heißt per Konvention `_celsius`.
- Im `__init__` rufst du `self.celsius = wert` auf, damit der Setter direkt greift.

**Erwartetes Ergebnis:**

```
Temperatur: 20.0°C (68.0°F)
Temperatur: -10.0°C (14.0°F)
Fehler: -300.0°C liegt unter dem absoluten Nullpunkt (-273.15°C).
Temperatur: -10.0°C (14.0°F)
Temperatur in Fahrenheit: 14.0°F
```

---

## Aufgabe 08-Z5: Vererbung – Fahrzeuge
*(ca. 20 Minuten)*

**Nutze die Datei `src/kapitel_08/aufgabe_08-Z5.py` für Deine Lösung.**

**Aufgabenstellung:**
Modelliere eine kleine Fahrzeug-Hierarchie:

1. Basisklasse `Fahrzeug` mit Attributen `marke` und `baujahr` sowie einer Methode `beschreibung()`, die einen Basis-String zurückgibt.
2. Subklasse `Auto(Fahrzeug)` mit dem zusätzlichen Attribut `tueren` (Anzahl Türen). Überschreibe `beschreibung()`, nutze `super()` um die Basis-Beschreibung einzubeziehen.
3. Subklasse `Motorrad(Fahrzeug)` mit dem zusätzlichen Attribut `hat_beiwagen` (Boolean). Überschreibe `beschreibung()` ebenfalls mit `super()`.

Erzeuge je ein Objekt pro Klasse und gib `beschreibung()` aus. Zeige außerdem, dass Subklassen-Objekte auf Attribute der Basisklasse zugreifen können.

**Lernziele:**
- Eine Vererbungshierarchie mit `class Subklasse(Basisklasse)` aufbauen.
- `super().__init__()` im Konstruktor der Subklasse aufrufen.
- `super().methode()` nutzen, um Methoden der Basisklasse zu erweitern statt zu ersetzen.

**Erwartetes Ergebnis:**

```
Fahrzeug: BMW, Baujahr 2020
Auto: Toyota, Baujahr 2022, 5 Türen
Motorrad: Harley-Davidson, Baujahr 2019, Beiwagen: Nein

Baujahr des Autos (aus Basisklasse): 2022
```

---

## Aufgabe 08-Z6: Bibliotheksverwaltung
*(Integrationsaufgabe, ca. 30 Minuten)*

**Nutze die Datei `src/kapitel_08/aufgabe_08-Z6.py` für Deine Lösung.**

**Aufgabenstellung:**
Baue eine kleine Bibliotheksverwaltung mit zwei Klassen:

**Klasse `Buch`:**
- Attribute: `titel`, `autor`, `isbn`
- `__str__`: `"'Titel' von Autor (ISBN: 000)"`
- `__eq__`: Zwei Bücher gelten als gleich, wenn ihre ISBN übereinstimmt.

**Klasse `Bibliothek`:**
- Attribut: `buecher` (leere Liste im Konstruktor)
- `buch_hinzufuegen(buch)`: Fügt ein Buch hinzu. Gibt eine Meldung aus, wenn ein Buch mit derselben ISBN schon vorhanden ist (nutze `in` und `__eq__`).
- `buch_suchen(titel)`: Gibt das erste Buch zurück, dessen Titel den Suchbegriff enthält (Groß-/Kleinschreibung egal). Gibt `None` zurück, wenn nichts gefunden.
- `alle_buecher()`: Gibt alle Bücher nummeriert aus.
- `anzahl()`: Gibt die Anzahl der Bücher zurück.

Teste die Bibliothek mit mindestens 3 Büchern, einer doppelten ISBN und einer Suche.

**Lernziele:**
- Zwei Klassen entwerfen und über eine Assoziation (Liste von Objekten) verbinden.
- `__eq__` für eine inhaltliche Gleichheitsprüfung in einer realen Anwendung einsetzen.
- Methoden mit Suche und Validierung implementieren.

**Erwartetes Ergebnis:**

```
'Der Herr der Ringe' von Tolkien (ISBN: 978-0-261-10235-4) hinzugefügt.
'Clean Code' von Robert C. Martin (ISBN: 978-0-13-235088-4) hinzugefügt.
'Python Crashkurs' von Eric Matthes (ISBN: 978-1-59327-603-4) hinzugefügt.
Fehler: Buch mit ISBN 978-0-261-10235-4 ist bereits vorhanden.

--- Alle Bücher ---
1. 'Der Herr der Ringe' von Tolkien (ISBN: 978-0-261-10235-4)
2. 'Clean Code' von Robert C. Martin (ISBN: 978-0-13-235088-4)
3. 'Python Crashkurs' von Eric Matthes (ISBN: 978-1-59327-603-4)
Gesamt: 3 Bücher

Suche nach 'clean':
Gefunden: 'Clean Code' von Robert C. Martin (ISBN: 978-0-13-235088-4)

Suche nach 'Java':
Nicht gefunden.
```
