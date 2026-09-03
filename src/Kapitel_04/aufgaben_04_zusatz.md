# Zusätzliche Übungsaufgaben zum Kapitel 04: Kontrollfluss – Schleifen und Iteration
*(Gesamtzeit: ca. 90-120 Min)*

Diese Aufgaben ergänzen die regulären Übungen zu Kapitel 04. Du übst while-Schleifen, for-Schleifen, range() sowie break und continue in neuen, praxisnahen Szenarien.

#### Aufgaben zu Kapitel 04 - Zusatz
- [ ] Aufgabe 04-Z1
- [ ] Aufgabe 04-Z2
- [ ] Aufgabe 04-Z3
- [ ] Aufgabe 04-Z4
- [ ] Aufgabe 04-Z5
- [ ] Aufgabe 04-Z6

---

## Aufgabe 04-Z1: Multiplikationstabelle
*(ca. 10 Minuten)*

**Nutze die Datei `src/kapitel_04/aufgabe_04-Z1.py` für Deine Lösung.**

**Aufgabenstellung:**
Schreibe ein Programm, das eine Zahl als Eingabe entgegennimmt und deren Multiplikationstabelle von 1 bis 10 ausgibt.

**Lernziele:**
- Eine `for`-Schleife mit `range()` aufbauen.
- Die Schleifenvariable in einer Berechnung innerhalb des Rumpfes nutzen.
- Ergebnisse mit f-Strings formatiert ausgeben.

***Hinweise:***
- `range(1, 11)` erzeugt die Zahlen 1 bis 10.

**Erwartetes Ergebnis:**

- bei Eingabe von `7`

```
Zahl: 7

Multiplikationstabelle für 7:
7 x  1 =  7
7 x  2 = 14
7 x  3 = 21
7 x  4 = 28
7 x  5 = 35
7 x  6 = 42
7 x  7 = 49
7 x  8 = 56
7 x  9 = 63
7 x 10 = 70
```

---

## Aufgabe 04-Z2: Eingabe-Validierung mit while
*(ca. 15 Minuten)*

**Nutze die Datei `src/kapitel_04/aufgabe_04-Z2.py` für Deine Lösung.**

**Aufgabenstellung:**
Schreibe ein Programm, das den Benutzer so lange nach einer Zahl zwischen 1 und 100 fragt, bis eine gültige Eingabe gemacht wurde. Erst dann gibt das Programm die Zahl und eine Bestätigung aus.

**Lernziele:**
- Eine `while`-Schleife als Eingabe-Validierungsschleife einsetzen.
- Die Bedingung der `while`-Schleife so formulieren, dass sie bei einer gültigen Eingabe endet.
- Verstehen, warum `while` hier besser geeignet ist als `for`.

***Hinweise:***
- Starte mit einem Startwert außerhalb des gültigen Bereichs, damit die Schleife mindestens einmal läuft.
- Alternativ kannst du mit `while True:` und `break` arbeiten.

**Erwartetes Ergebnis:**

- bei Eingaben `0`, dann `150`, dann `42`

```
Bitte eine Zahl zwischen 1 und 100 eingeben: 0
Ungültige Eingabe! Bitte erneut versuchen.
Bitte eine Zahl zwischen 1 und 100 eingeben: 150
Ungültige Eingabe! Bitte erneut versuchen.
Bitte eine Zahl zwischen 1 und 100 eingeben: 42
Gültige Eingabe: 42
```

---

## Aufgabe 04-Z3: Summen mit range() und Schrittweite
*(ca. 15 Minuten)*

**Nutze die Datei `src/kapitel_04/aufgabe_04-Z3.py` für Deine Lösung.**

**Aufgabenstellung:**
Schreibe ein Programm, das mithilfe einer `for`-Schleife und `range()` folgende drei Aufgaben löst:

1. Die Summe aller geraden Zahlen von 2 bis 100.
2. Die Summe aller ungeraden Zahlen von 1 bis 99.
3. Die Summe aller Zahlen, die durch 5 teilbar sind, von 5 bis 50.

**Lernziele:**
- `range()` mit Start-, Stop- und Schrittweiten-Argument (`step`) einsetzen.
- Einen Akkumulator (eine Variable, die schrittweise aufaddiert wird) in einer Schleife nutzen.
- Mehrere unabhängige Schleifen nacheinander ausführen.

***Hinweise:***
- `range(2, 101, 2)` erzeugt alle geraden Zahlen von 2 bis 100.
- Starte den Akkumulator vor jeder Schleife mit `summe = 0`.

**Erwartetes Ergebnis:**

```
Summe gerader Zahlen (2-100):    2550
Summe ungerader Zahlen (1-99):   2500
Summe durch 5 teilbar (5-50):     275
```

---

## Aufgabe 04-Z4: Wörter filtern mit continue und break
*(ca. 20 Minuten)*

**Nutze die Datei `src/kapitel_04/aufgabe_04-Z4.py` für Deine Lösung.**

**Aufgabenstellung:**
Schreibe ein Programm, das über eine vorgegebene Liste von Wörtern iteriert und dabei zwei Filterregeln anwendet:
1. Wörter mit weniger als 4 Buchstaben werden übersprungen (`continue`).
2. Sobald das Wort `"stopp"` auftaucht, wird die Schleife sofort beendet (`break`).

Alle anderen Wörter sollen ausgegeben werden.

**Vorgegebene Liste – direkt im Code definieren:**
```python
woerter = ["Hallo", "Hi", "Python", "ist", "cool", "stopp", "das", "kommt", "nicht", "mehr"]
```

**Lernziele:**
- `continue` zum Überspringen einzelner Iterationen einsetzen.
- `break` zum vorzeitigen Beenden der Schleife einsetzen.
- Den Unterschied zwischen `break` und `continue` im selben Programm erleben.

**Erwartetes Ergebnis:**

```
Hallo
Python
cool
Schleife durch 'stopp' beendet.
```

---

## Aufgabe 04-Z5: Rückwärtszähler und Quersumme
*(ca. 20 Minuten)*

**Nutze die Datei `src/kapitel_04/aufgabe_04-Z5.py` für Deine Lösung.**

**Aufgabenstellung:**
Schreibe ein Programm, das eine positive Ganzzahl als Eingabe entgegennimmt und:
1. Alle Zahlen von der Eingabe bis 1 rückwärts ausgibt (mit `while`-Schleife, alle in einer Zeile).
2. Danach `"Start!"` ausgibt.
3. Anschließend die Quersumme der eingegebenen Zahl berechnet und ausgibt (mit `for`-Schleife).

**Lernziele:**
- Eine `while`-Schleife mit abnehmender Zählervariable aufbauen.
- Über die Zeichen eines Strings mit einer `for`-Schleife iterieren.
- Einen String mit `str()` in ein iterierbares Objekt umwandeln und Ziffern mit `int()` konvertieren.
- Den `end`-Parameter von `print()` nutzen, um Ausgaben in einer Zeile zu halten.

***Hinweise:***
- `print(wert, end=" ")` gibt den Wert aus, ohne danach einen Zeilenumbruch zu machen.
- Um die Quersumme zu berechnen, iteriere über `str(zahl)` und konvertiere jede Ziffer mit `int()`.

**Erwartetes Ergebnis:**

- bei Eingabe von `5`

```
Zahl: 5
5 4 3 2 1 Start!
Quersumme von 5: 5
```

- bei Eingabe von `137`

```
Zahl: 137
137 136 135 134 ... 2 1 Start!
Quersumme von 137: 11
```

---

## Aufgabe 04-Z6: Einkaufslisten-Assistent
*(Integrationsaufgabe, ca. 30 Minuten)*

**Nutze die Datei `src/kapitel_04/aufgabe_04-Z6.py` für Deine Lösung.**

**Aufgabenstellung:**
Schreibe ein Programm, das als einfacher Einkaufslisten-Assistent funktioniert:

1. Der Benutzer wird in einer `while`-Schleife nach Artikeln gefragt, bis er `"fertig"` eingibt.
2. Jeder eingegebene Artikel wird einer Liste hinzugefügt (nutze `.append()`).
3. Artikel, die kürzer als 2 Zeichen sind, werden mit `continue` übersprungen und eine Hinweismeldung ausgegeben.
4. Nach Abschluss wird die Liste nummeriert mit einer `for`-Schleife ausgegeben.
5. Zum Schluss wird die Gesamtanzahl der Artikel ausgegeben.

**Lernziele:**
- Eine `while`-Schleife für eine dialogbasierte Eingabe einsetzen.
- Eine Liste dynamisch mit `.append()` befüllen.
- `continue` zur Filterung ungültiger Eingaben innerhalb der Schleife nutzen.
- Über eine Liste mit `for` und `range(len(...))` nummeriert iterieren.

***Hinweise:***
- `len(liste)` gibt die Anzahl der Elemente zurück.
- `range(len(einkaufsliste))` erzeugt Indizes von 0 bis zur letzten Position.
- Mit `einkaufsliste[i]` greifst du auf das Element an Position `i` zu.

**Erwartetes Ergebnis:**

- bei Eingaben `Milch`, `a`, `Brot`, `Eier`, `fertig`

```
Artikel eingeben (oder 'fertig' zum Beenden): Milch
Artikel eingeben (oder 'fertig' zum Beenden): a
Zu kurz – Artikel wird ignoriert.
Artikel eingeben (oder 'fertig' zum Beenden): Brot
Artikel eingeben (oder 'fertig' zum Beenden): Eier
Artikel eingeben (oder 'fertig' zum Beenden): fertig

--- Deine Einkaufsliste ---
1. Milch
2. Brot
3. Eier
---------------------------
Insgesamt 3 Artikel.
```
