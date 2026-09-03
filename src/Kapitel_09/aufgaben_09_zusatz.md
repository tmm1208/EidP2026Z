# Zusätzliche Übungsaufgaben zum Kapitel 09: Dateien und Fehlerbehandlung
*(Gesamtzeit: ca. 90-120 Min)*

Diese Aufgaben ergänzen die regulären Übungen zu Kapitel 09. Du übst Dateizugriff, CSV, JSON, pickle und Fehlerbehandlung in neuen, praxisnahen Szenarien.

#### Aufgaben zu Kapitel 09 - Zusatz
- [ ] Aufgabe 09-Z1
- [ ] Aufgabe 09-Z2
- [ ] Aufgabe 09-Z3
- [ ] Aufgabe 09-Z4
- [ ] Aufgabe 09-Z5
- [ ] Aufgabe 09-Z6

---

## Aufgabe 09-Z1: Textdatei schreiben und lesen
*(ca. 10 Minuten)*

**Nutze die Datei `src/kapitel_09/aufgabe_09-Z1.py` für Deine Lösung.**

**Aufgabenstellung:**
Schreibe ein Programm, das:
1. Eine Liste von fünf Städtenamen direkt im Code definiert.
2. Die Liste mit `with open()` im Modus `"w"` in eine Datei `staedte.txt` schreibt – jede Stadt in einer eigenen Zeile.
3. Die Datei anschließend mit `with open()` im Modus `"r"` liest und jede Zeile bereinigt (`.strip()`) ausgibt.

**Lernziele:**
- `with open()` zum Schreiben und zum Lesen einsetzen.
- `\n` als expliziten Zeilenumbruch in `.write()` verwenden.
- `.strip()` zum Entfernen von Zeilenumbrüchen beim Lesen nutzen.
- `encoding="utf-8"` konsequent angeben.

**Erwartetes Ergebnis:**

```
Datei 'staedte.txt' geschrieben.

Inhalt von 'staedte.txt':
Berlin
Hamburg
München
Wismar
Rostock
```

---

## Aufgabe 09-Z2: Anhängen mit Append-Modus
*(ca. 15 Minuten)*

**Nutze die Datei `src/kapitel_09/aufgabe_09-Z2.py` für Deine Lösung.**

**Aufgabenstellung:**
Erweitere das Logbuch-Konzept: Schreibe ein Programm, das:
1. Beim ersten Start eine neue Datei `notizen.txt` erstellt und einen ersten Eintrag schreibt.
2. Beim zweiten Start denselben Code ausführt – diesmal soll der neue Eintrag angehängt werden, nicht die Datei überschrieben.
3. Am Ende den gesamten Inhalt der Datei ausgibt.

Nutze zuerst `"w"` für den ersten Eintrag, dann `"a"` für den zweiten.

**Lernziele:**
- Den Unterschied zwischen `"w"` (überschreiben) und `"a"` (anhängen) gezielt einsetzen.
- Verstehen, warum `"a"` wichtig ist, wenn bestehende Daten erhalten bleiben sollen.

***Hinweise:***
- Führe das Programm einmal aus, schau in die Datei, ändere dann `"w"` zu `"a"` und führe es erneut aus.

**Erwartetes Ergebnis:**

- Nach dem ersten Start (mit `"w"`):
```
notizen.txt nach erstem Eintrag:
Eintrag 1: Python macht Spaß.
```
- Nach dem zweiten Start (mit `"a"`):
```
notizen.txt nach zweitem Eintrag:
Eintrag 1: Python macht Spaß.
Eintrag 2: Dateien zu schreiben ist einfach.
```

---

## Aufgabe 09-Z3: CSV lesen und auswerten
*(ca. 15 Minuten)*

**Nutze die Datei `src/kapitel_09/aufgabe_09-Z3.py` für Deine Lösung.**

**Aufgabenstellung:**
Erstelle zunächst im Code eine CSV-Datei `produkte.csv` mit folgendem Inhalt:

```
name,kategorie,preis
Laptop,Elektronik,999.99
Maus,Elektronik,29.99
Schreibtisch,Möbel,349.00
Stuhl,Möbel,189.00
Kopfhörer,Elektronik,149.99
```

Lese die Datei anschließend mit `csv.DictReader` ein und:
1. Gib alle Produkte mit Name und Preis aus.
2. Berechne und gib den Durchschnittspreis aller Produkte aus.
3. Gib nur die Elektronik-Produkte aus.

**Lernziele:**
- Eine CSV-Datei programmatisch erzeugen und anschließend mit `csv.DictReader` einlesen.
- Auf Werte in einem Dictionary über Spaltennamen zugreifen.
- Daten aus einer CSV-Datei filtern und auswerten.

***Hinweise:***
- `float(row["preis"])` konvertiert den gelesenen String in eine Zahl.

**Erwartetes Ergebnis:**

```
--- Alle Produkte ---
Laptop: 999.99 Euro
Maus: 29.99 Euro
Schreibtisch: 349.0 Euro
Stuhl: 189.0 Euro
Kopfhörer: 149.99 Euro

Durchschnittspreis: 343.59 Euro

--- Nur Elektronik ---
Laptop: 999.99 Euro
Maus: 29.99 Euro
Kopfhörer: 149.99 Euro
```

---

## Aufgabe 09-Z4: JSON – Konfiguration speichern und laden
*(ca. 20 Minuten)*

**Nutze die Datei `src/kapitel_09/aufgabe_09-Z4.py` für Deine Lösung.**

**Aufgabenstellung:**
Schreibe ein Programm, das eine Anwendungskonfiguration als Dictionary verwaltet:

1. Erstelle ein Dictionary `konfig` mit mindestens den Schlüsseln `"benutzername"`, `"sprache"`, `"benachrichtigungen"` (Boolean) und `"max_eintraege"` (Integer).
2. Serialisiere das Dictionary mit `json.dump()` in eine Datei `konfig.json` (mit `indent=4`).
3. Lade die Datei mit `json.load()` zurück und gib alle Schlüssel-Wert-Paare aus.
4. Ändere einen Wert im geladenen Dictionary und speichere es erneut.

**Lernziele:**
- `json.dump()` mit `indent=4` für menschenlesbare Ausgabe einsetzen.
- `json.load()` zum Einlesen einer JSON-Datei nutzen.
- Den JSON-Roundtrip (Python → JSON → Python) vollständig durchführen.
- Verstehen, dass Python-Typen (bool, int, str) beim JSON-Roundtrip erhalten bleiben.

**Erwartetes Ergebnis:**

```
Konfiguration gespeichert.

Geladene Konfiguration:
  benutzername: Tim
  sprache: de
  benachrichtigungen: True
  max_eintraege: 50

Konfiguration nach Änderung erneut gespeichert.
```

---

## Aufgabe 09-Z5: Fehlerbehandlung mit LBYL und EAFP
*(ca. 20 Minuten)*

**Nutze die Datei `src/kapitel_09/aufgabe_09-Z5.py` für Deine Lösung.**

**Aufgabenstellung:**
Schreibe zwei Funktionen, die beide versuchen, eine Datei zu lesen – eine mit dem LBYL-Ansatz, eine mit dem EAFP-Ansatz:

1. `lese_datei_lbyl(dateiname)`: Prüft mit `os.path.exists()` ob die Datei existiert, bevor sie geöffnet wird. Gibt den Inhalt zurück oder `None`.
2. `lese_datei_eafp(dateiname)`: Verwendet `try/except FileNotFoundError`, um den Fehler abzufangen. Gibt den Inhalt zurück oder `None`.

Teste beide Funktionen mit einer existierenden Datei (erstelle sie vorher im Code) und einer nicht existierenden Datei.

**Lernziele:**
- Den LBYL-Ansatz mit `os.path.exists()` implementieren.
- Den EAFP-Ansatz mit `try/except FileNotFoundError` implementieren.
- Beide Ansätze direkt vergleichen und ihren Effekt im gleichen Programm erleben.

**Erwartetes Ergebnis:**

```
--- LBYL ---
Datei 'test.txt' gefunden: Hallo aus der Testdatei!
Datei 'nicht_da.txt' nicht gefunden.

--- EAFP ---
Datei 'test.txt' gelesen: Hallo aus der Testdatei!
Fehler: Datei 'nicht_da.txt' nicht gefunden.
```

---

## Aufgabe 09-Z6: Objekt-Persistenz mit JSON und pickle
*(Integrationsaufgabe, ca. 30 Minuten)*

**Nutze die Datei `src/kapitel_09/aufgabe_09-Z6.py` für Deine Lösung.**

**Aufgabenstellung:**
Definiere eine Klasse `Kontakt` mit den Attributen `name`, `email` und `telefon`. Implementiere:

1. Eine Methode `to_dict()`, die die Attribute als Dictionary zurückgibt.
2. Eine Funktion `kontakt_from_dict(data)`, die aus einem Dictionary ein `Kontakt`-Objekt erstellt.
3. Eine Funktion `speichere_kontakte_json(kontakte, dateiname)`, die eine Liste von `Kontakt`-Objekten als JSON speichert (nutze `to_dict()`).
4. Eine Funktion `lade_kontakte_json(dateiname)`, die die JSON-Datei lädt und eine Liste von `Kontakt`-Objekten zurückgibt (nutze `kontakt_from_dict()`). Fange einen `FileNotFoundError` ab.
5. Speichere dieselbe Liste zusätzlich mit `pickle` und lade sie wieder.

Erzeuge drei Kontakt-Objekte, speichere und lade sie mit beiden Methoden und vergleiche die Ergebnisse.

**Lernziele:**
- `to_dict()` und eine Factory-Funktion für den JSON-Roundtrip eigener Objekte implementieren.
- `pickle` als einfachere Alternative für Python-interne Persistenz einsetzen.
- Fehlerbehandlung mit `try/except FileNotFoundError` in einer Ladefunktion integrieren.
- Die Vor- und Nachteile beider Ansätze durch direkten Vergleich erleben.

**Erwartetes Ergebnis:**

```
3 Kontakte als JSON gespeichert.
JSON geladen – 3 Kontakte:
  Ada Lovelace | ada@example.com | 0123-456789
  Alan Turing | alan@example.com | 0987-654321
  Grace Hopper | grace@example.com | 0111-222333

3 Kontakte mit pickle gespeichert.
Pickle geladen – 3 Kontakte:
  Ada Lovelace | ada@example.com | 0123-456789
  Alan Turing | alan@example.com | 0987-654321
  Grace Hopper | grace@example.com | 0111-222333
```
