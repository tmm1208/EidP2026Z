# Zusätzliche Übungsaufgaben zum Kapitel 03: Kontrollfluss – Logik und Verzweigungen
*(Gesamtzeit: ca. 90-120 Min)*

Diese Aufgaben ergänzen die regulären Übungen zu Kapitel 03. Du übst boolesche Ausdrücke, Vergleichsoperatoren, if-elif-else und logische Operatoren in neuen, praxisnahen Szenarien.

#### Aufgaben zu Kapitel 03 - Zusatz
- [ ] Aufgabe 03-Z1
- [ ] Aufgabe 03-Z2
- [ ] Aufgabe 03-Z3
- [ ] Aufgabe 03-Z4
- [ ] Aufgabe 03-Z5
- [ ] Aufgabe 03-Z6

---

## Aufgabe 03-Z1: Ampelsteuerung
*(ca. 10 Minuten)*

**Nutze die Datei `src/kapitel_03/aufgabe_03-Z1.py` für Deine Lösung.**

**Aufgabenstellung:**
Schreibe ein Programm, das eine Ampelfarbe als Texteingabe entgegennimmt (`rot`, `gelb` oder `gruen`) und die passende Anweisung für Autofahrer ausgibt. Nutze eine `if-elif-else`-Struktur. Für alle anderen Eingaben soll eine Fehlermeldung erscheinen.

**Lernziele:**
- Eine `if-elif-else`-Kette mit String-Vergleichen aufbauen.
- Einen sinnvollen `else`-Zweig als Auffangfall für unerwartete Eingaben nutzen.
- Den Unterschied zwischen `==` (Vergleich) und `=` (Zuweisung) sicher anwenden.

**Erwartetes Ergebnis:**

- bei Eingabe von `rot`
```
Ampelfarbe: rot
Anhalten!
```
- bei Eingabe von `gelb`
```
Ampelfarbe: gelb
Achtung – bitte bremsen!
```
- bei Eingabe von `gruen`
```
Ampelfarbe: gruen
Fahrt frei!
```
- bei Eingabe von `blau`
```
Ampelfarbe: blau
Unbekannte Ampelfarbe.
```

---

## Aufgabe 03-Z2: Fitnessstudio-Zugang
*(ca. 15 Minuten)*

**Nutze die Datei `src/kapitel_03/aufgabe_03-Z2.py` für Deine Lösung.**

**Aufgabenstellung:**
Ein Fitnessstudio gewährt Zugang nur unter bestimmten Bedingungen. Schreibe ein Programm, das prüft, ob eine Person Zutritt erhält:
- Die Person braucht eine gültige Mitgliedschaft (`hat_mitgliedschaft = True`) **und** muss mindestens 16 Jahre alt sein.
- Alternativ erhält auch eine Person ohne Mitgliedschaft Zutritt, wenn sie eine Tageskarte gekauft hat (`hat_tageskarte = True`).

Frage das Alter und die drei Boolean-Werte per `input()` ab (Eingabe: `ja` oder `nein`).

**Lernziele:**
- `and` und `or` kombinieren, um komplexe Zugangsbedingungen abzubilden.
- String-Eingaben (`"ja"` / `"nein"`) in boolesche Werte übersetzen.
- Logische Ausdrücke mit Klammern korrekt gruppieren.

***Hinweise:***
- `hat_mitgliedschaft = eingabe == "ja"` wandelt eine Texteingabe direkt in einen Boolean um.
- Denke an Klammern bei der Kombination von `and` und `or`, damit die Logik stimmt.

**Erwartetes Ergebnis:**

- bei Eingabe von Alter `20`, Mitgliedschaft `ja`, VIP `nein`, Tageskarte `nein`
```
Alter: 20
Mitgliedschaft (ja/nein): ja
Tageskarte (ja/nein): nein
Zutritt gewährt!
```
- bei Eingabe von Alter `14`, Mitgliedschaft `ja`, Tageskarte `nein`
```
Alter: 14
Mitgliedschaft (ja/nein): ja
Tageskarte (ja/nein): nein
Zutritt verweigert.
```
- bei Eingabe von Alter `30`, Mitgliedschaft `nein`, Tageskarte `ja`
```
Alter: 30
Mitgliedschaft (ja/nein): nein
Tageskarte (ja/nein): ja
Zutritt gewährt!
```

---

## Aufgabe 03-Z3: Jahreszeitenfinder
*(ca. 15 Minuten)*

**Nutze die Datei `src/kapitel_03/aufgabe_03-Z3.py` für Deine Lösung.**

**Aufgabenstellung:**
Schreibe ein Programm, das eine Monatsnummer (1–12) als Eingabe entgegennimmt und die zugehörige Jahreszeit ausgibt. Löse die Aufgabe einmal mit einer `if-elif-else`-Kette und einmal mit einer `match-case`-Anweisung (als Kommentarblock direkt darunter).

**Zuordnung:**
- Frühling: März (3), April (4), Mai (5)
- Sommer: Juni (6), Juli (7), August (8)
- Herbst: September (9), Oktober (10), November (11)
- Winter: Dezember (12), Januar (1), Februar (2)

**Lernziele:**
- Mehrere Werte pro Zweig mit `or` in einer `if-elif`-Kette prüfen.
- Mehrere Werte in einem `case`-Zweig mit `|` (Pipe) zusammenfassen.
- Den Unterschied zwischen `if-elif-else` und `match-case` im direkten Vergleich erleben.

***Hinweise:***
- In `match-case` kannst du mehrere Werte in einem `case` mit `|` trennen: `case 3 | 4 | 5:`.
- Für ungültige Monatsnummern soll eine Fehlermeldung erscheinen.

**Erwartetes Ergebnis:**

- bei Eingabe von `4`
```
Monat: 4
Jahreszeit: Frühling
```
- bei Eingabe von `13`
```
Monat: 13
Ungültige Monatsnummer.
```

---

## Aufgabe 03-Z4: Versandkostenrechner
*(ca. 20 Minuten)*

**Nutze die Datei `src/kapitel_03/aufgabe_03-Z4.py` für Deine Lösung.**

**Aufgabenstellung:**
Schreibe ein Programm, das Versandkosten anhand von zwei Kriterien berechnet: dem Bestellwert und ob der Kunde ein Premium-Mitglied ist. Die Regeln lauten:
- Premium-Mitglieder zahlen immer 0,00 € Versand.
- Nicht-Premium-Mitglieder zahlen:
  - 0,00 € bei einem Bestellwert über 50 €
  - 2,99 € bei einem Bestellwert von 20 € bis 50 €
  - 4,99 € bei einem Bestellwert unter 20 €

**Lernziele:**
- Verschachtelte `if-else`-Strukturen sinnvoll einsetzen.
- Mehrere Bedingungen mit `and` und Vergleichsoperatoren kombinieren.
- Konstanten für feste Werte (Schwellenwerte, Preise) einsetzen.

***Hinweise:***
- Prüfe zuerst den Premium-Status, dann die Bestellwert-Stufen.
- Definiere die Versandkosten-Werte als Konstanten am Anfang der Datei.

**Erwartetes Ergebnis:**

- bei Eingabe von Bestellwert `35` und Premium `nein`
```
Bestellwert (Euro): 35
Premium-Mitglied (ja/nein): nein
Bestellwert:    35.00 Euro
Versandkosten:   2.99 Euro
```
- bei Eingabe von Bestellwert `35` und Premium `ja`
```
Bestellwert (Euro): 35
Premium-Mitglied (ja/nein): ja
Bestellwert:    35.00 Euro
Versandkosten:   0.00 Euro
```

---

## Aufgabe 03-Z5: Noten-Umrechner mit ternärem Operator
*(ca. 20 Minuten)*

**Nutze die Datei `src/kapitel_03/aufgabe_03-Z5.py` für Deine Lösung.**

**Aufgabenstellung:**
Schreibe ein Programm, das eine Punktzahl (0–100) als Eingabe entgegennimmt und:
1. Die Schulnote (1–6) über eine `if-elif-else`-Kette ermittelt.
2. Mit dem **ternären Operator** in einer einzigen Zeile bestimmt, ob die Prüfung bestanden wurde (`>= 50 Punkte`).
3. Beide Ergebnisse formatiert ausgibt.

**Notenschlüssel:**
- 90–100 Punkte → Note 1
- 75–89 Punkte → Note 2
- 60–74 Punkte → Note 3
- 50–59 Punkte → Note 4
- 25–49 Punkte → Note 5
- 0–24 Punkte → Note 6

**Lernziele:**
- Eine mehrstufige `if-elif-else`-Kette mit Bereichsprüfungen aufbauen.
- Den ternären Operator für eine einfache Ja/Nein-Entscheidung sinnvoll einsetzen.
- Den Unterschied zwischen `if-elif-else` (Anweisung) und ternärem Operator (Ausdruck) verstehen.

***Hinweise:***
- Der ternäre Operator hat die Form: `wert_wenn_wahr if bedingung else wert_wenn_falsch`
- Für die Prüfung "bestanden": `status = "bestanden" if punkte >= 50 else "nicht bestanden"`

**Erwartetes Ergebnis:**

- bei Eingabe von `78`
```
Punkte (0-100): 78
Note:     2
Status:   bestanden
```
- bei Eingabe von `42`
```
Punkte (0-100): 42
Note:     5
Status:   nicht bestanden
```

---

## Aufgabe 03-Z6: Fahrpreisrechner
*(Integrationsaufgabe, ca. 30 Minuten)*

**Nutze die Datei `src/kapitel_03/aufgabe_03-Z6.py` für Deine Lösung.**

**Aufgabenstellung:**
Schreibe ein Programm, das den Fahrpreis für ein Verkehrsmittel berechnet. Der Preis hängt von drei Faktoren ab:
1. **Alter**: Kinder (unter 6) fahren kostenlos, Kinder (6–14) zahlen den halben Preis, Senioren (ab 65) zahlen den halben Preis, alle anderen den vollen Preis.
2. **Strecke in km**: Grundpreis 0,15 € pro km (voller Preis) bzw. 0,075 € pro km (halber Preis).
3. **Bahncard**: Wer eine Bahncard besitzt, erhält 25% Rabatt auf den berechneten Preis (nicht auf kostenlose Fahrten).

Das Programm soll Alter, Strecke und Bahncard-Besitz abfragen und den Endpreis formatiert ausgeben.

**Lernziele:**
- Alle Konzepte des Kapitels kombinieren: `if-elif-else`, `and`/`or`/`not`, Vergleichsoperatoren.
- Mehrere aufeinander aufbauende Berechnungsschritte strukturiert abbilden.
- Einen `bool`-Wert aus einer Texteingabe erzeugen und in der Logik einsetzen.

***Hinweise:***
- Definiere `PREIS_PRO_KM = 0.15` und `BAHNCARD_RABATT = 0.25` als Konstanten.
- Berechne zuerst den Basispreis (je nach Altersgruppe), dann ziehe ggf. den Bahncard-Rabatt ab.

**Erwartetes Ergebnis:**

- bei Eingabe von Alter `30`, Strecke `100`, Bahncard `ja`
```
Alter: 30
Strecke (km): 100
Bahncard (ja/nein): ja

--- Fahrpreisberechnung ---
Altersgruppe:  Erwachsener (voller Preis)
Basispreis:    15.00 Euro
Bahncard-Rabatt: -3.75 Euro
Endpreis:      11.25 Euro
```
- bei Eingabe von Alter `4`, Strecke `50`, Bahncard `nein`
```
Alter: 4
Strecke (km): 50
Bahncard (ja/nein): nein

--- Fahrpreisberechnung ---
Altersgruppe:  Kind (unter 6, kostenlos)
Endpreis:      0.00 Euro
```
