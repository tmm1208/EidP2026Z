
# Zusätzliche Übungsaufgaben zum Kapitel 05: Datenstrukturen und Listenverarbeitung
*(Gesamtzeit: ca. 90-120 Min)*

Diese Aufgaben ergänzen die regulären Übungen zu Kapitel 05. Du übst Listen, Indizierung, Slicing, Tupel und List Comprehensions in neuen, praxisnahen Szenarien.

#### Aufgaben zu Kapitel 05 - Zusatz
- [ ] Aufgabe 05-Z1
- [ ] Aufgabe 05-Z2
- [ ] Aufgabe 05-Z3
- [ ] Aufgabe 05-Z4
- [ ] Aufgabe 05-Z5
- [ ] Aufgabe 05-Z6

---

## Aufgabe 05-Z1: Listenoperationen erkunden
*(ca. 10 Minuten)*

**Nutze die Datei `src/kapitel_05/aufgabe_05-Z1.py` für Deine Lösung.**

**Aufgabenstellung:**
Gegeben ist die folgende Liste direkt im Code:

```python
plaene = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag"]
```

Führe nacheinander folgende Operationen durch und gib die Liste nach jeder Operation aus:
1. Gib das erste und das letzte Element per Indizierung aus.
2. Ändere `"Mittwoch"` zu `"Frei"`.
3. Füge `"Samstag"` am Ende hinzu.
4. Lösche `"Dienstag"` über seinen Index.
5. Gib die Länge der aktuellen Liste aus.

**Lernziele:**
- Positive und negative Indizierung auf einer Liste anwenden.
- Elemente per Index überschreiben.
- `.append()` und `del` einsetzen.
- `len()` zur Längenbestimmung nutzen.

**Erwartetes Ergebnis:**

```
Erstes Element: Montag
Letztes Element: Freitag
Nach Änderung: ['Montag', 'Dienstag', 'Frei', 'Donnerstag', 'Freitag']
Nach append: ['Montag', 'Dienstag', 'Frei', 'Donnerstag', 'Freitag', 'Samstag']
Nach del: ['Montag', 'Frei', 'Donnerstag', 'Freitag', 'Samstag']
Länge: 5
```

---

## Aufgabe 05-Z2: Slicing – Wochentage aufteilen
*(ca. 15 Minuten)*

**Nutze die Datei `src/kapitel_05/aufgabe_05-Z2.py` für Deine Lösung.**

**Aufgabenstellung:**
Gegeben ist folgende Liste direkt im Code:

```python
wochentage = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
```

Extrahiere per Slicing:
1. Die Werktage (Mo–Fr).
2. Das Wochenende (Sa–So).
3. Die Wochenmitte (Di–Do).
4. Jeden zweiten Tag der ganzen Woche.
5. Die gesamte Woche in umgekehrter Reihenfolge.

**Lernziele:**
- Slicing mit Start-, Stop- und Schrittweiten-Argument anwenden.
- Einen negativen Schrittwert (`step = -1`) zum Umkehren nutzen.
- Verstehen, warum der Stop-Index exklusiv ist.

***Hinweise:***
- Eine Liste lässt sich mit `liste[::-1]` umkehren.
- Lässt man Start und Stop weg, erfasst der Slice die gesamte Liste.

**Erwartetes Ergebnis:**

```
Werktage:          ['Mo', 'Di', 'Mi', 'Do', 'Fr']
Wochenende:        ['Sa', 'So']
Wochenmitte:       ['Di', 'Mi', 'Do']
Jeden zweiten Tag: ['Mo', 'Mi', 'Fr', 'So']
Umgekehrt:         ['So', 'Sa', 'Fr', 'Do', 'Mi', 'Di', 'Mo']
```

---

## Aufgabe 05-Z3: Notenauswertung
*(ca. 15 Minuten)*

**Nutze die Datei `src/kapitel_05/aufgabe_05-Z3.py` für Deine Lösung.**

**Aufgabenstellung:**
Gegeben ist folgende Notenliste direkt im Code:

```python
noten = [2, 4, 1, 3, 5, 2, 1, 4, 3, 2]
```

Berechne und gib aus:
1. Die Anzahl der Noten mit `len()`.
2. Die beste Note (niedrigster Wert) mit `min()`.
3. Die schlechteste Note (höchster Wert) mit `max()`.
4. Den Notendurchschnitt (Summe aller Noten geteilt durch Anzahl). Nutze `sum()`.
5. Ob die Note `1` in der Liste enthalten ist (mit `in`).
6. An welchem Index die erste `1` steht (mit `.index()`).

**Lernziele:**
- Die eingebauten Funktionen `len()`, `min()`, `max()` und `sum()` auf Listen anwenden.
- Den `in`-Operator zur Zugehörigkeitsprüfung nutzen.
- Die Methode `.index()` zum Auffinden eines Elements einsetzen.

**Erwartetes Ergebnis:**

```
Anzahl Noten:     10
Beste Note:        1
Schlechteste Note: 5
Durchschnitt:      2.7
Note 1 vorhanden?: True
Erster Index von 1: 2
```

---

## Aufgabe 05-Z4: Tupel für Koordinaten
*(ca. 20 Minuten)*

**Nutze die Datei `src/kapitel_05/aufgabe_05-Z4.py` für Deine Lösung.**

**Aufgabenstellung:**
Du arbeitest mit GPS-Koordinaten, die als Tupel gespeichert werden. Gegeben sind folgende Koordinaten direkt im Code:

```python
wismar     = (53.8929, 11.4521)
rostock    = (54.0924, 12.0991)
hamburg    = (53.5753, 10.0153)
```

1. Gib für jede Stadt Name, Breitengrad (Index 0) und Längengrad (Index 1) formatiert aus.
2. Speichere alle drei Koordinaten in einer Liste `staedte`.
3. Gib aus, wie viele Städte in der Liste sind.
4. Versuche, den Breitengrad von Wismar zu ändern (z.B. `wismar[0] = 99`). Kommentiere danach den Versuch aus und erkläre in einem Kommentar, was passiert und warum.

**Lernziele:**
- Tupel als unveränderliche Datensätze einsetzen.
- Auf Tupel-Elemente per Indizierung zugreifen.
- Den `TypeError` bei einem Änderungsversuch verstehen und dokumentieren.
- Tupel in einer Liste organisieren.

**Erwartetes Ergebnis:**

```
Wismar:  Breite 53.8929 | Länge 11.4521
Rostock: Breite 54.0924 | Länge 12.0991
Hamburg: Breite 53.5753 | Länge 10.0153
Anzahl Städte in der Liste: 3
```

---

## Aufgabe 05-Z5: List Comprehensions
*(ca. 20 Minuten)*

**Nutze die Datei `src/kapitel_05/aufgabe_05-Z5.py` für Deine Lösung.**

**Aufgabenstellung:**
Löse alle drei Teilaufgaben ausschließlich mit List Comprehensions (keine for-Schleifen mit `.append()`):

**Teilaufgabe A:**
Gegeben ist `temperaturen_celsius = [0, 20, 37, 100, -10]`. Erstelle eine neue Liste `temperaturen_fahrenheit`, die alle Temperaturen in Fahrenheit enthält.

Formel: `F = C * 9/5 + 32`

**Teilaufgabe B:**
Gegeben ist `woerter = ["Hallo", "Welt", "Python", "ist", "toll", "super"]`. Erstelle eine neue Liste `lange_woerter`, die nur Wörter mit mehr als 4 Buchstaben enthält.

**Teilaufgabe C:**
Erstelle mit einer List Comprehension eine Liste `quadratzahlen`, die die Quadrate aller ungeraden Zahlen von 1 bis 20 enthält.

**Lernziele:**
- List Comprehensions mit einem Ausdruck (Transformation) aufbauen.
- List Comprehensions mit einer `if`-Bedingung (Filter) aufbauen.
- List Comprehensions mit `range()` kombinieren.

**Erwartetes Ergebnis:**

```
Celsius:    [0, 20, 37, 100, -10]
Fahrenheit: [32.0, 68.0, 98.6, 212.0, 14.0]

Alle Wörter:   ['Hallo', 'Welt', 'Python', 'ist', 'toll', 'super']
Lange Wörter:  ['Hallo', 'Python', 'super']

Quadrate ungerader Zahlen (1-20): [1, 9, 25, 49, 81, 121, 169, 225, 289, 361]
```

---

## Aufgabe 05-Z6: Playlist-Verwaltung
*(Integrationsaufgabe, ca. 30 Minuten)*

**Nutze die Datei `src/kapitel_05/aufgabe_05-Z6.py` für Deine Lösung.**

**Aufgabenstellung:**
Schreibe ein Programm, das eine einfache Playlist verwaltet. Der Benutzer kann in einer `while`-Schleife Befehle eingeben:

- `add`: Song zur Playlist hinzufügen (per `input()` abfragen, dann `.append()`).
- `remove`: Song über seinen Namen entfernen (prüfe zuerst mit `in`, ob er vorhanden ist, dann mit `.index()` und `del`).
- `show`: Aktuelle Playlist nummeriert ausgeben.
- `sort`: Playlist alphabetisch sortieren (mit `.sort()`).
- `quit`: Programm beenden.

Bei unbekannten Befehlen soll eine Hinweismeldung erscheinen.

**Lernziele:**
- Eine Liste dynamisch mit `.append()` und `del` verwalten.
- Den `in`-Operator zur sicheren Prüfung vor `.index()` einsetzen.
- `.sort()` in einer realen Anwendung nutzen.
- Alle Konzepte des Kapitels in einer interaktiven Anwendung kombinieren.

***Hinweise:***
- Prüfe vor dem Entfernen immer mit `if song in playlist:`, um einen `ValueError` zu vermeiden.
- `del playlist[playlist.index(song)]` entfernt das erste Vorkommen eines Elements.

**Erwartetes Ergebnis:**

```
Befehl (add/remove/show/sort/quit): add
Song: Bohemian Rhapsody
Befehl (add/remove/show/sort/quit): add
Song: Stairway to Heaven
Befehl (add/remove/show/sort/quit): show
1. Bohemian Rhapsody
2. Stairway to Heaven
Befehl (add/remove/show/sort/quit): sort
Playlist sortiert.
Befehl (add/remove/show/sort/quit): remove
Song: Stairway to Heaven
'Stairway to Heaven' entfernt.
Befehl (add/remove/show/sort/quit): show
1. Bohemian Rhapsody
Befehl (add/remove/show/sort/quit): quit
Tschüss!
```
