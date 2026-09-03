
# Zusätzliche Übungsaufgaben zum Kapitel 06: Datenstrukturen – Dictionaries und Sets
*(Gesamtzeit: ca. 90-120 Min)*

Diese Aufgaben ergänzen die regulären Übungen zu Kapitel 06. Du übst Dictionaries, Sets und Mengenoperationen in neuen, praxisnahen Szenarien.

#### Aufgaben zu Kapitel 06 - Zusatz
- [ ] Aufgabe 06-Z1
- [ ] Aufgabe 06-Z2
- [ ] Aufgabe 06-Z3
- [ ] Aufgabe 06-Z4
- [ ] Aufgabe 06-Z5
- [ ] Aufgabe 06-Z6

---

## Aufgabe 06-Z1: Steckbrief als Dictionary
*(ca. 10 Minuten)*

**Nutze die Datei `src/kapitel_06/aufgabe_06-Z1.py` für Deine Lösung.**

**Aufgabenstellung:**
Erstelle ein Dictionary `person` mit den Schlüsseln `"name"`, `"alter"`, `"stadt"` und `"beruf"` und befülle es mit eigenen Werten. Führe dann folgende Operationen durch und gib die Liste nach jeder Änderung aus:

1. Gib den Namen und die Stadt per Schlüsselzugriff aus.
2. Ändere den Beruf auf einen neuen Wert.
3. Füge den Schlüssel `"sprachen"` mit einer Liste aus zwei Sprachen hinzu.
4. Lösche den Schlüssel `"alter"` mit `del`.
5. Gib zum Abschluss alle Schlüssel-Wert-Paare mit `.items()` in einer `for`-Schleife aus.

**Lernziele:**
- Ein Dictionary-Literal erstellen und befüllen.
- Per Schlüssel lesen, schreiben und löschen.
- `.items()` für die Iteration über Schlüssel-Wert-Paare nutzen.

**Erwartetes Ergebnis:**

```
Name: Ada Lovelace | Stadt: London
Nach Änderung: {'name': 'Ada Lovelace', 'alter': 36, 'stadt': 'London', 'beruf': 'Mathematikerin'}
Nach append: {'name': 'Ada Lovelace', 'alter': 36, 'stadt': 'London', 'beruf': 'Mathematikerin', 'sprachen': ['Englisch', 'Französisch']}
Nach del: {'name': 'Ada Lovelace', 'stadt': 'London', 'beruf': 'Mathematikerin', 'sprachen': ['Englisch', 'Französisch']}

--- Alle Einträge ---
name: Ada Lovelace
stadt: London
beruf: Mathematikerin
sprachen: ['Englisch', 'Französisch']
```

---

## Aufgabe 06-Z2: Sicherer Zugriff mit .get()
*(ca. 15 Minuten)*

**Nutze die Datei `src/kapitel_06/aufgabe_06-Z2.py` für Deine Lösung.**

**Aufgabenstellung:**
Gegeben ist folgendes Dictionary direkt im Code:

```python
produkt = {
    "name": "Laptop",
    "preis": 999.99,
    "lagerbestand": 42
}
```

1. Greife auf `"name"` und `"preis"` sicher mit `[]` zu und gib sie aus.
2. Versuche, auf den nicht vorhandenen Schlüssel `"rabatt"` mit `[]` zuzugreifen. Kommentiere diese Zeile danach aus und erkläre im Kommentar, was passiert.
3. Greife auf `"rabatt"` mit `.get()` zu (ohne Standardwert) und gib das Ergebnis aus.
4. Greife auf `"rabatt"` mit `.get()` und dem Standardwert `0.0` zu und gib das Ergebnis aus.

**Lernziele:**
- Den Unterschied zwischen `[]`-Zugriff (KeyError) und `.get()` (None/Standardwert) verstehen.
- `.get()` mit und ohne Standardwert einsetzen.
- Laufzeitfehler erkennen und durch sicheren Zugriff vermeiden.

**Erwartetes Ergebnis:**

```
Name: Laptop
Preis: 999.99 Euro
# Zeile mit [] auskommentiert – würde KeyError auslösen

Rabatt (get ohne Default): None
Rabatt (get mit Default):  0.0
```

---

## Aufgabe 06-Z3: Häufigkeitszähler
*(ca. 15 Minuten)*

**Nutze die Datei `src/kapitel_06/aufgabe_06-Z3.py` für Deine Lösung.**

**Aufgabenstellung:**
Schreibe ein Programm, das in einem vorgegebenen Text die Häufigkeit jedes Wortes zählt und das Ergebnis als Dictionary ausgibt. Nutze `.get()` mit einem Standardwert, um den Zähler elegant zu erhöhen.

**Vorgegebener Text – direkt im Code definieren:**
```python
text = "die katze sitzt auf der matte die matte ist weich die katze auch"
```

**Lernziele:**
- Ein Dictionary dynamisch als Zähler aufbauen.
- `.get()` mit Standardwert als elegante Alternative zur `if`-Prüfung einsetzen.
- Über eine Liste mit `for` iterieren und dabei ein Dictionary befüllen.

***Hinweise:***
- Teile den Text mit `.split()` in eine Liste von Wörtern auf.
- `haeufigkeit[wort] = haeufigkeit.get(wort, 0) + 1` erhöht den Zähler elegant.

**Erwartetes Ergebnis:**

```
Worthäufigkeiten:
die: 3
katze: 2
sitzt: 1
auf: 1
der: 1
matte: 2
ist: 1
weich: 1
auch: 1
```

---

## Aufgabe 06-Z4: Duplikate entfernen und Mengen vergleichen
*(ca. 20 Minuten)*

**Nutze die Datei `src/kapitel_06/aufgabe_06-Z4.py` für Deine Lösung.**

**Aufgabenstellung:**
Gegeben sind zwei Listen mit Teilnehmern zweier Veranstaltungen direkt im Code:

```python
veranstaltung_a = ["Alice", "Bob", "Charlie", "Alice", "David", "Bob"]
veranstaltung_b = ["Charlie", "David", "Eva", "Frank", "Alice"]
```

1. Wandle beide Listen in Sets um und gib die einzigartigen Teilnehmer beider Veranstaltungen aus.
2. Berechne und gib aus: alle Teilnehmer zusammen (Vereinigung).
3. Berechne und gib aus: Teilnehmer, die beide Veranstaltungen besucht haben (Schnittmenge).
4. Berechne und gib aus: Teilnehmer, die nur Veranstaltung A besucht haben (Differenz).
5. Berechne und gib aus: Teilnehmer, die genau eine Veranstaltung besucht haben (Symmetrische Differenz).

**Lernziele:**
- Listen mit `set()` in Sets umwandeln, um Duplikate zu entfernen.
- Die vier Mengenoperationen `|`, `&`, `-`, `^` anwenden.
- Den praktischen Nutzen von Mengenoperationen in einem realen Szenario erleben.

**Erwartetes Ergebnis:**

```
Einzigartige Teilnehmer A: {'Alice', 'Bob', 'Charlie', 'David'}
Einzigartige Teilnehmer B: {'Alice', 'Charlie', 'David', 'Eva', 'Frank'}

Alle Teilnehmer (Vereinigung):       {'Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'}
Beide Veranstaltungen (Schnittmenge): {'Alice', 'Charlie', 'David'}
Nur Veranstaltung A (Differenz):     {'Bob'}
Genau eine Veranstaltung (Sym. Diff.): {'Bob', 'Eva', 'Frank'}
```

*(Hinweis: Die Reihenfolge der Elemente in einem Set ist nicht garantiert – deine Ausgabe kann abweichen.)*

---

## Aufgabe 06-Z5: Telefonbuch
*(ca. 20 Minuten)*

**Nutze die Datei `src/kapitel_06/aufgabe_06-Z5.py` für Deine Lösung.**

**Aufgabenstellung:**
Schreibe ein interaktives Telefonbuch als Dictionary. Der Benutzer kann in einer `while`-Schleife folgende Befehle eingeben:

- `add`: Name und Nummer abfragen, ins Dictionary eintragen.
- `search`: Name abfragen, Nummer mit `.get()` suchen und ausgeben (oder Hinweis, wenn nicht gefunden).
- `delete`: Name abfragen, Eintrag mit `del` löschen (prüfe vorher mit `in`, ob er existiert).
- `show`: Alle Einträge mit `.items()` ausgeben.
- `quit`: Programm beenden.

**Lernziele:**
- Ein Dictionary interaktiv und dynamisch verwalten.
- Den `in`-Operator zur sicheren Existenzprüfung vor `del` einsetzen.
- `.get()` für eine fehlertolerante Suche nutzen.
- `.items()` für die Ausgabe aller Einträge nutzen.

**Erwartetes Ergebnis:**

```
Befehl (add/search/delete/show/quit): add
Name: Ada
Nummer: 0123-456789
Befehl (add/search/delete/show/quit): add
Name: Alan
Nummer: 0987-654321
Befehl (add/search/delete/show/quit): search
Name: Ada
Ada: 0123-456789
Befehl (add/search/delete/show/quit): search
Name: Linus
'Linus' nicht im Telefonbuch.
Befehl (add/search/delete/show/quit): show
Ada: 0123-456789
Alan: 0987-654321
Befehl (add/search/delete/show/quit): quit
Tschüss!
```

---

## Aufgabe 06-Z6: Kursverwaltung mit Dicts und Sets
*(Integrationsaufgabe, ca. 30 Minuten)*

**Nutze die Datei `src/kapitel_06/aufgabe_06-Z6.py` für Deine Lösung.**

**Aufgabenstellung:**
Gegeben sind zwei Kurse mit ihren Teilnehmern als Dictionaries direkt im Code:

```python
kurs_python = {
    "titel": "Python Grundlagen",
    "dozent": "Prof. Pieper",
    "teilnehmer": {"Anna", "Ben", "Clara", "David", "Eva"}
}

kurs_datenbanken = {
    "titel": "Datenbanken",
    "dozent": "Prof. Müller",
    "teilnehmer": {"Clara", "David", "Frank", "Grace", "Ben"}
}
```

Führe folgende Auswertungen durch und gib sie formatiert aus:

1. Gib Titel und Dozent beider Kurse aus.
2. Gib die Anzahl der Teilnehmer pro Kurs aus.
3. Welche Studierenden belegen beide Kurse? (Schnittmenge)
4. Welche Studierenden belegen mindestens einen Kurs? (Vereinigung)
5. Welche Studierenden belegen nur Python, aber nicht Datenbanken? (Differenz)
6. Wie viele einzigartige Studierende gibt es insgesamt?

**Lernziele:**
- Dictionaries und Sets kombiniert in einer realen Datenstruktur einsetzen.
- Auf Werte eines Dictionaries zugreifen und damit weiterrechnen.
- Alle vier Mengenoperationen in einer sinnvollen Anwendung nutzen.
- `len()` auf Sets anwenden.

**Erwartetes Ergebnis:**

```
--- Kursübersicht ---
Kurs 1: Python Grundlagen (Dozent: Prof. Pieper, Teilnehmer: 5)
Kurs 2: Datenbanken (Dozent: Prof. Müller, Teilnehmer: 5)

--- Auswertung ---
Belegen beide Kurse:          {'Ben', 'Clara', 'David'}
Belegen mind. einen Kurs:     {'Anna', 'Ben', 'Clara', 'David', 'Eva', 'Frank', 'Grace'}
Nur Python (nicht Datenbank): {'Anna', 'Eva'}
Einzigartige Studierende gesamt: 7
```

*(Hinweis: Die Reihenfolge der Elemente in einem Set ist nicht garantiert – deine Ausgabe kann abweichen.)*
