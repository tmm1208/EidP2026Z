
# Zusätzliche Übungsaufgaben zum Kapitel 07: Eigene Funktionen, Type Hints & Funktionale Programmierung
*(Gesamtzeit: ca. 90-120 Min)*

Diese Aufgaben ergänzen die regulären Übungen zu Kapitel 07. Du übst eigene Funktionen, Rückgabewerte, Default-Werte, *args/**kwargs, Rekursion, Type Hints sowie lambda, map() und filter() in neuen, praxisnahen Szenarien.

#### Aufgaben zu Kapitel 07 - Zusatz
- [ ] Aufgabe 07-Z1
- [ ] Aufgabe 07-Z2
- [ ] Aufgabe 07-Z3
- [ ] Aufgabe 07-Z4
- [ ] Aufgabe 07-Z5
- [ ] Aufgabe 07-Z6

---

## Aufgabe 07-Z1: Funktionen mit return
*(ca. 10 Minuten)*

**Nutze die Datei `src/kapitel_07/aufgabe_07-Z1.py` für Deine Lösung.**

**Aufgabenstellung:**
Schreibe drei separate Funktionen:

1. `berechne_flaeche(breite, hoehe)` – gibt die Fläche eines Rechtecks zurück.
2. `berechne_umfang(breite, hoehe)` – gibt den Umfang eines Rechtecks zurück.
3. `ist_quadrat(breite, hoehe)` – gibt `True` zurück, wenn Breite und Höhe gleich sind, sonst `False`.

Rufe alle drei Funktionen mit `breite = 5` und `hoehe = 8` auf und gib die Ergebnisse aus.

**Lernziele:**
- Einfache Funktionen mit `def` und `return` definieren.
- Den Rückgabewert einer Funktion in einer Variablen speichern und weiterverarbeiten.
- Boolesche Rückgabewerte aus einer Funktion nutzen.

***Hinweise:***
- Fläche: `breite * hoehe`
- Umfang: `2 * (breite + hoehe)`
- Für `ist_quadrat` reicht ein Vergleich mit `==` als Rückgabewert.

**Erwartetes Ergebnis:**

```
Fläche:    40
Umfang:    26
Quadrat?:  False
```

---

## Aufgabe 07-Z2: Default-Werte und Docstrings
*(ca. 15 Minuten)*

**Nutze die Datei `src/kapitel_07/aufgabe_07-Z2.py` für Deine Lösung.**

**Aufgabenstellung:**
Schreibe eine Funktion `erstelle_email(empfaenger, betreff, signatur="Mit freundlichen Grüßen")`, die eine einfache E-Mail als mehrzeiligen String zurückgibt und ausgibt. Die Signatur soll einen Standardwert haben, damit sie optional ist.

Rufe die Funktion zweimal auf:
1. Ohne eigene Signatur (Standardwert soll greifen).
2. Mit eigener Signatur `"Viele Grüße"`.

Versehe die Funktion außerdem mit einem aussagekräftigen **Docstring**.

**Lernziele:**
- Einen optionalen Parameter mit Default-Wert definieren.
- Einen Docstring korrekt anlegen (dreifache Anführungszeichen).
- Den Unterschied zwischen einem Aufruf mit und ohne optionales Argument erleben.

**Erwartetes Ergebnis:**

- Erster Aufruf (ohne Signatur):
```
An: max.mustermann@example.com
Betreff: Testmail

Hallo!

Mit freundlichen Grüßen
```
- Zweiter Aufruf (mit Signatur):
```
An: erika.muster@example.com
Betreff: Hallo!

Hallo!

Viele Grüße
```

---

## Aufgabe 07-Z3: *args und **kwargs
*(ca. 15 Minuten)*

**Nutze die Datei `src/kapitel_07/aufgabe_07-Z3.py` für Deine Lösung.**

**Aufgabenstellung:**
Schreibe eine Funktion `erstelle_rechnung(kunde, *artikel, **extras)`, die:
- `kunde`: den Namen des Kunden als normalen Parameter nimmt.
- `*artikel`: eine beliebige Anzahl von Artikelnamen als Tupel sammelt.
- `**extras`: optionale Zusatzinfos als Dictionary sammelt (z.B. `rabatt`, `versand`).

Die Funktion soll eine formatierte Rechnung ausgeben.

Rufe die Funktion zweimal auf:
1. Mit einem Kunden, drei Artikeln, ohne Extras.
2. Mit einem Kunden, zwei Artikeln und den Extras `rabatt="10%"` und `versand="kostenlos"`.

**Lernziele:**
- `*args` zum Sammeln beliebig vieler positionaler Argumente einsetzen.
- `**kwargs` zum Sammeln beliebig vieler Keyword-Argumente einsetzen.
- Die korrekte Reihenfolge der Parametertypen in der Funktionsdefinition anwenden.

**Erwartetes Ergebnis:**

- Erster Aufruf:
```
--- Rechnung für: Anna ---
Artikel:
  - Laptop
  - Maus
  - Tastatur
```
- Zweiter Aufruf:
```
--- Rechnung für: Ben ---
Artikel:
  - Monitor
  - Kabel
Extras:
  rabatt: 10%
  versand: kostenlos
```

---

## Aufgabe 07-Z4: Rekursion – Summe und Potenz
*(ca. 20 Minuten)*

**Nutze die Datei `src/kapitel_07/aufgabe_07-Z4.py` für Deine Lösung.**

**Aufgabenstellung:**
Schreibe zwei rekursive Funktionen:

1. `summe_bis(n)` – gibt die Summe aller ganzen Zahlen von 1 bis n zurück (rekursiv).
   - Basisfall: `summe_bis(0)` gibt `0` zurück.
   - Rekursiver Schritt: `n + summe_bis(n - 1)`.

2. `potenz(basis, exponent)` – berechnet `basis ** exponent` rekursiv, ohne den `**`-Operator zu nutzen.
   - Basisfall: `potenz(basis, 0)` gibt `1` zurück.
   - Rekursiver Schritt: `basis * potenz(basis, exponent - 1)`.

Rufe beide Funktionen mit sinnvollen Werten auf und gib die Ergebnisse aus.

**Lernziele:**
- Basisfall und rekursiven Schritt einer eigenen Rekursion korrekt definieren.
- Erkennen, wie das Problem bei jedem Schritt kleiner wird.
- Den Rückgabewert eines rekursiven Aufrufs weiterverarbeiten.

***Hinweise:***
- Teste `summe_bis(5)` – das Ergebnis sollte 15 sein (1+2+3+4+5).
- Teste `potenz(2, 8)` – das Ergebnis sollte 256 sein.

**Erwartetes Ergebnis:**

```
Summe 1 bis 5:  15
Summe 1 bis 10: 55

2 hoch 8:   256
3 hoch 4:    81
```

---

## Aufgabe 07-Z5: Type Hints, lambda und map/filter
*(ca. 20 Minuten)*

**Nutze die Datei `src/kapitel_07/aufgabe_07-Z5.py` für Deine Lösung.**

**Aufgabenstellung:**
Löse alle drei Teilaufgaben:

**Teil A – Type Hints:**
Schreibe eine Funktion `berechne_bmi(gewicht_kg: float, groesse_m: float) -> float`, die den BMI berechnet und zurückgibt (Formel: `gewicht / groesse ** 2`). Füge einen Docstring hinzu.

**Teil B – lambda und sorted():**
Gegeben ist diese Liste direkt im Code:
```python
produkte = [
    {"name": "Maus", "preis": 29.99},
    {"name": "Tastatur", "preis": 79.99},
    {"name": "Monitor", "preis": 349.99},
    {"name": "Kabel", "preis": 9.99},
]
```
Sortiere die Liste mit `.sort()` und einer `lambda`-Funktion nach dem Preis (aufsteigend) und gib sie aus.

**Teil C – map() und filter():**
Gegeben ist `temperaturen = [22.5, -3.0, 18.0, -10.5, 35.0, 0.0, 28.5]`.
- Nutze `filter()` und `lambda`, um nur positive Temperaturen zu behalten.
- Nutze `map()` und `lambda`, um alle Temperaturen (der Originallist) auf eine Nachkommastelle zu runden.

**Lernziele:**
- Type Hints für Parameter und Rückgabewert korrekt schreiben.
- Eine `lambda`-Funktion als `key`-Argument für `.sort()` einsetzen.
- `map()` und `filter()` mit `lambda`-Funktionen kombinieren und das Ergebnis mit `list()` materialisieren.

**Erwartetes Ergebnis:**

```
BMI (70kg, 1.75m): 22.86

Produkte nach Preis:
  Kabel:     9.99 Euro
  Maus:     29.99 Euro
  Tastatur: 79.99 Euro
  Monitor: 349.99 Euro

Positive Temperaturen:  [22.5, 18.0, 35.0, 28.5]
Gerundete Temperaturen: [22.5, -3.0, 18.0, -10.5, 35.0, 0.0, 28.5]
```

---

## Aufgabe 07-Z6: Taschenrechner mit Funktionen
*(Integrationsaufgabe, ca. 30 Minuten)*

**Nutze die Datei `src/kapitel_07/aufgabe_07-Z6.py` für Deine Lösung.**

**Aufgabenstellung:**
Schreibe einen interaktiven Taschenrechner, der vier Rechenoperationen als eigene Funktionen kapselt und über ein Menü in einer `while`-Schleife bedienbar ist.

1. Definiere vier Funktionen mit Type Hints und Docstrings:
   - `addiere(a: float, b: float) -> float`
   - `subtrahiere(a: float, b: float) -> float`
   - `multipliziere(a: float, b: float) -> float`
   - `dividiere(a: float, b: float) -> float` — gibt `None` zurück und gibt eine Fehlermeldung aus, wenn `b == 0`.

2. Erstelle ein Dictionary `operationen`, das Befehlsnamen (`"add"`, `"sub"`, `"mul"`, `"div"`) auf die jeweiligen Funktionen mappt.

3. Der Benutzer gibt den Befehl und zwei Zahlen ein. Das Dictionary wird genutzt, um die passende Funktion aufzurufen.

4. Die Schleife endet bei Eingabe von `"quit"`.

**Lernziele:**
- Mehrere Funktionen mit Type Hints und Docstrings definieren.
- Funktionen als Werte in einem Dictionary speichern und aus diesem aufrufen.
- Alle Konzepte des Kapitels (Funktionsdefinition, `return`, Type Hints) in einer Anwendung kombinieren.

***Hinweise:***
- `operationen["add"]` gibt die Funktion `addiere` zurück.
- `operationen["add"](3, 5)` ruft `addiere(3, 5)` auf.

**Erwartetes Ergebnis:**

```
Operation (add/sub/mul/div/quit): add
Zahl 1: 10
Zahl 2: 5
Ergebnis: 15.0

Operation (add/sub/mul/div/quit): div
Zahl 1: 10
Zahl 2: 0
Fehler: Division durch null nicht erlaubt.

Operation (add/sub/mul/div/quit): quit
Tschüss!
```
