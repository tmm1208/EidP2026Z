# Zusätzliche Übungsaufgaben zum Kapitel 02: Variablen, Objekte, Operatoren und erste Datentypen
*(Gesamtzeit: ca. 90-120 Min)*

Diese Aufgaben ergänzen die regulären Übungen zu Kapitel 02. Du übst Variablen, Datentypen, Operatoren und Typkonvertierung in neuen, praxisnahen Szenarien.

#### Aufgaben zu Kapitel 02 - Zusatz
- [ ] Aufgabe 02-Z1
- [ ] Aufgabe 02-Z2
- [ ] Aufgabe 02-Z3
- [ ] Aufgabe 02-Z4
- [ ] Aufgabe 02-Z5
- [ ] Aufgabe 02-Z6

---

## Aufgabe 02-Z1: Datentypen erkunden
*(ca. 10 Minuten)*

**Nutze die Datei `src/kapitel_02/aufgabe_02-Z1.py` für Deine Lösung.**

**Aufgabenstellung:**
Lege vier Variablen an – eine für jeden der vier grundlegenden Datentypen `int`, `float`, `bool` und `str`. Wähle dabei Variablennamen, die inhaltlich Sinn ergeben. Gib anschließend für jede Variable ihren Wert und ihren Datentyp mit `type()` aus.

**Lernziele:**
- Die vier grundlegenden Datentypen `int`, `float`, `bool` und `str` in der Praxis einsetzen.
- Aussagekräftige Variablennamen nach der `snake_case`-Konvention wählen.
- Die eingebaute Funktion `type()` zur Typprüfung nutzen.
- Variablenwerte und Typen mit f-Strings formatiert ausgeben.

***Hinweise:***
- Wähle sinnvolle Namen, z.B. `alter`, `temperatur`, `ist_eingeschrieben`, `studiengang`.
- `type()` gibt den Typ eines Objekts zurück, z.B. `<class 'int'>`.

**Erwartetes Ergebnis:**

```
Wert: 22       | Typ: <class 'int'>
Wert: 36.6     | Typ: <class 'float'>
Wert: True     | Typ: <class 'bool'>
Wert: Informatik | Typ: <class 'str'>
```

---

## Aufgabe 02-Z2: Kinoticket-Preisrechner
*(ca. 15 Minuten)*

**Nutze die Datei `src/kapitel_02/aufgabe_02-Z2.py` für Deine Lösung.**

**Aufgabenstellung:**
Ein Kino verkauft Tickets für 12.50 Euro. Schreibe ein Programm, das die Anzahl der gewünschten Tickets als Text-Eingabe entgegennimmt, den Gesamtpreis berechnet und formatiert ausgibt. Gib außerdem aus, ob der Gesamtpreis über 50 Euro liegt.

**Lernziele:**
- Eine `input()`-Eingabe mit `int()` in eine Zahl konvertieren, um damit rechnen zu können.
- Einen `float`-Wert mit einer bestimmten Anzahl von Nachkommastellen in einem f-String formatieren (`:`.2f`).
- Einen booleschen Ausdruck berechnen und ausgeben.

***Hinweise:***
- Eingaben über `input()` sind immer vom Typ `str` – konvertiere die Eingabe mit `int()` bevor du rechnest.
- Für zwei Nachkommastellen in einem f-String schreibe: `f"{wert:.2f}"`.
- Ein Vergleich wie `gesamtpreis > 50` ergibt `True` oder `False`.

**Erwartetes Ergebnis:**

- bei Eingabe von `3`

```
Anzahl Tickets: 3
Anzahl:        3 Ticket(s)
Preis pro Ticket: 12.50 Euro
Gesamtpreis:   37.50 Euro
Über 50 Euro?  False
```

- bei Eingabe von `5`

```
Anzahl Tickets: 5
Anzahl:        5 Ticket(s)
Preis pro Ticket: 12.50 Euro
Gesamtpreis:   62.50 Euro
Über 50 Euro?  True
```

---

## Aufgabe 02-Z3: Kilometerrechner
*(ca. 15 Minuten)*

**Nutze die Datei `src/kapitel_02/aufgabe_02-Z3.py` für Deine Lösung.**

**Aufgabenstellung:**
Schreibe ein Programm, das eine Entfernung in Kilometern als Eingabe entgegennimmt und diese in drei weitere Einheiten umrechnet: Meter, Meilen und Seemeilen. Nutze dafür Konstanten für die Umrechnungsfaktoren.

**Umrechnungsfaktoren:**
- 1 km = 1000 m
- 1 km = 0.621371 Meilen
- 1 km = 0.539957 Seemeilen

**Lernziele:**
- `float()`-Konvertierung für Kommazahlen-Eingaben nutzen.
- Konstanten nach der Python-Konvention in `GROSSBUCHSTABEN` definieren.
- Mehrere Berechnungen mit denselben Ausgangsdaten durchführen und formatiert ausgeben.

***Hinweise:***
- Definiere die Umrechnungsfaktoren als Konstanten direkt am Anfang der Datei, z.B. `METER_PRO_KM = 1000`.
- Für sinnvolle Nachkommastellen nutze `:.4f` im f-String.

**Erwartetes Ergebnis:**

- bei Eingabe von `42`

```
Entfernung in km: 42

--- Umrechnung ---
42.0 km = 42000.0 m
42.0 km = 26.0976 Meilen
42.0 km = 22.6782 Seemeilen
```

---

## Aufgabe 02-Z4: Ganzzahldivision und Modulo – Zeitrechner
*(ca. 20 Minuten)*

**Nutze die Datei `src/kapitel_02/aufgabe_02-Z4.py` für Deine Lösung.**

**Aufgabenstellung:**
Schreibe ein Programm, das eine Anzahl von Minuten als Eingabe entgegennimmt und diese in Stunden und verbleibende Minuten aufteilt. Nutze dafür die Ganzzahldivision `//` und den Modulo-Operator `%`.

**Lernziele:**
- Den Ganzzahldivisions-Operator `//` zur Berechnung ganzer Anteile einsetzen.
- Den Modulo-Operator `%` zur Berechnung von Resten einsetzen.
- Den Zusammenhang zwischen `//` und `%` verstehen und praktisch anwenden.

***Hinweise:***
- `stunden = minuten_gesamt // 60` ergibt die Anzahl der vollen Stunden.
- `rest_minuten = minuten_gesamt % 60` ergibt die übrigen Minuten.

**Erwartetes Ergebnis:**

- bei Eingabe von `137`

```
Minuten gesamt: 137
137 Minuten sind:
2 Stunden und 17 Minuten.
```

- bei Eingabe von `60`

```
Minuten gesamt: 60
60 Minuten sind:
1 Stunden und 0 Minuten.
```

---

## Aufgabe 02-Z5: Brutto-Netto-Rechner
*(ca. 20 Minuten)*

**Nutze die Datei `src/kapitel_02/aufgabe_02-Z5.py` für Deine Lösung.**

**Aufgabenstellung:**
Schreibe ein Programm, das einen Netto-Preis als Eingabe entgegennimmt und daraus drei Ausgaben berechnet: den Brutto-Preis mit 7% MwSt. (ermäßigt, z.B. für Lebensmittel), den Brutto-Preis mit 19% MwSt. (regulär) und die jeweilige Steuer in Euro. Nutze Konstanten für die Steuersätze.

**Lernziele:**
- Konstanten sinnvoll einsetzen, um "Magic Numbers" im Code zu vermeiden.
- Mehrere Berechnungen auf Basis derselben Eingabe durchführen.
- Ergebnisse mit `:`.2f` auf zwei Nachkommastellen formatiert ausgeben.
- Den Unterschied zwischen Netto-, Steuer- und Brutto-Betrag programmatisch abbilden.

***Hinweise:***
- Definiere `UST_ERMAESSIGT = 0.07` und `UST_REGULAER = 0.19` als Konstanten.
- Die Steuer ergibt sich aus `netto * ust_satz`, der Brutto-Preis aus `netto * (1 + ust_satz)`.

**Erwartetes Ergebnis:**

- bei Eingabe von `100`

```
Netto-Preis (Euro): 100

--- Preisübersicht ---
Netto:                    100.00 Euro

Mit 7% MwSt. (ermäßigt):
  Steuer:                   7.00 Euro
  Brutto:                 107.00 Euro

Mit 19% MwSt. (regulär):
  Steuer:                  19.00 Euro
  Brutto:                 119.00 Euro
```

---

## Aufgabe 02-Z6: Variablen tauschen und Zuweisungsoperatoren
*(Integrationsaufgabe, ca. 30 Minuten)*

**Nutze die Datei `src/kapitel_02/aufgabe_02-Z6.py` für Deine Lösung.**

**Aufgabenstellung:**
Diese Aufgabe besteht aus zwei Teilen:

**Teil A – Variablen tauschen:**
Lass zwei Variablen `punkte_spieler_a` und `punkte_spieler_b` mit vom Benutzer eingegebenen Werten befüllen. Tausche anschließend die Werte der beiden Variablen (ohne eine dritte Hilfsvariable zu nutzen – Python erlaubt elegantes Tauschen!). Gib die Werte vor und nach dem Tausch aus.

**Teil B – Zuweisungsoperatoren:**
Starte mit einem Punktestand `punkte = 0` und wende dann nacheinander folgende Operationen mit den kombinierten Zuweisungsoperatoren an:
1. Addiere 50 Punkte (`+=`)
2. Multipliziere mit 3 (`*=`)
3. Subtrahiere 30 Punkte (`-=`)
4. Dividiere durch 2 (`/=`)
5. Gib nach jedem Schritt den aktuellen Punktestand aus.

**Lernziele:**
- Python-spezifisches simultanes Tauschen von Variablen (`a, b = b, a`) verstehen und einsetzen.
- Alle kombinierten Zuweisungsoperatoren (`+=`, `-=`, `*=`, `/=`) in der Praxis anwenden.
- Schrittweise Veränderungen einer Variablen nachvollziehen und ausgeben.

***Hinweise:***
- In Python kann man zwei Variablen elegant ohne Hilfsvariable tauschen: `a, b = b, a`
- Die kombinierten Zuweisungsoperatoren sind Kurzformen: `x += 5` ist dasselbe wie `x = x + 5`.

**Erwartetes Ergebnis:**

- bei Eingabe von `42` und `99`

```
Punkte Spieler A: 42
Punkte Spieler B: 99

Vor dem Tausch:
  Spieler A: 42
  Spieler B: 99

Nach dem Tausch:
  Spieler A: 99
  Spieler B: 42

--- Punktestand-Simulation ---
Start:              0
Nach += 50:        50
Nach *= 3:        150
Nach -= 30:       120
Nach /= 2:         60.0
```
