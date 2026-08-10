# Zusätzliche Übungsaufgaben zum Kapitel 01: Einführung und erste Schritte
*(Gesamtzeit: ca. 90-120 Min)*

Diese Aufgaben ergänzen die regulären Übungen zu Kapitel 01. Sie üben dieselben Grundkonzepte (print(), input(), Variablen, f-Strings) in neuen, praxisnahen Szenarien.

#### Aufgaben zu Kapitel 01 - Zusatz
- [ ] Aufgabe 01-Z1
- [ ] Aufgabe 01-Z2
- [ ] Aufgabe 01-Z3
- [ ] Aufgabe 01-Z4
- [ ] Aufgabe 01-Z5
- [ ] Aufgabe 01-Z6

---

## Aufgabe 01-Z1: Begrüßungsmaschine
*(ca. 10 Minuten)*

**Nutze die Datei `src/kapitel_01/aufgabe_01-Z1.py` für Deine Lösung.**

**Aufgabenstellung:**
Schreibe ein Programm, das den Benutzer nach seinem Vornamen und seinem Nachnamen fragt und ihn anschließend formal mit vollem Namen begrüßt.

**Lernziele:**
- Zwei separate `input()`-Anweisungen verwenden.
- Zwei Variablen sinnvoll benennen.
- Variablen in einem f-String kombinieren.

***Hinweise:***
- Speichere Vorname und Nachname in getrennten Variablen.
- Nutze einen f-String, um beide Variablen in einem Satz zu kombinieren.

**Erwartetes Ergebnis:**

- bei Eingabe von `Ada` und `Lovelace`

```
Bitte gib deinen Vornamen ein: Ada
Bitte gib deinen Nachnamen ein: Lovelace
Herzlich willkommen, Ada Lovelace!
```

---

## Aufgabe 01-Z2: Kassenbon
*(ca. 15 Minuten)*

**Nutze die Datei `src/kapitel_01/aufgabe_01-Z2.py` für Deine Lösung.**

**Aufgabenstellung:**
Schreibe ein Programm, das einen einfachen Kassenbon ausgibt. Das Programm soll den Benutzer nach drei Artikelnamen fragen und diese dann in einem formatierten Bon ausgeben. Es geht bei dieser Aufgabe noch nicht um Berechnungen – nur um die strukturierte Ausgabe von Texten.

**Lernziele:**
- Mehrere Variablen für Texteingaben verwenden.
- `print()` für eine mehrzeilige, strukturierte Ausgabe einsetzen.
- f-Strings zur Einbettung von Variablen in Ausgabezeilen nutzen.

**Erwartetes Ergebnis:**

- bei Eingabe von `Apfel`, `Milch`, `Brot`

```
Artikel 1: Apfel
Artikel 2: Milch
Artikel 3: Brot

========== KASSENBON ==========
  1x Apfel
  1x Milch
  1x Brot
===============================
Vielen Dank für Ihren Einkauf!
```

---

## Aufgabe 01-Z3: Persönlicher Steckbrief
*(ca. 15 Minuten)*

**Nutze die Datei `src/kapitel_01/aufgabe_01-Z3.py` für Deine Lösung.**

**Aufgabenstellung:**
Schreibe ein Programm, das vier Informationen vom Benutzer abfragt (Name, Alter, Wohnort, Lieblingsfarbe) und diese anschließend als übersichtlichen Steckbrief ausgibt.

**Lernziele:**
- Vier `input()`-Anweisungen nacheinander einsetzen.
- Variablen in einer strukturierten, mehrzeiligen Ausgabe wiederverwenden.
- Eine tabellenartige Textausgabe mit `print()` und f-Strings gestalten.

**Erwartetes Ergebnis:**

- bei Eingabe von `Marie`, `22`, `Hamburg`, `Blau`

```
Wie heißt du? Marie
Wie alt bist du? 22
Wo wohnst du? Hamburg
Was ist deine Lieblingsfarbe? Blau

-------- STECKBRIEF --------
Name:           Marie
Alter:          22 Jahre
Wohnort:        Hamburg
Lieblingsfarbe: Blau
----------------------------
```

---

## Aufgabe 01-Z4: Konzertkarte
*(ca. 20 Minuten)*

**Nutze die Datei `src/kapitel_01/aufgabe_01-Z4.py` für Deine Lösung.**

**Aufgabenstellung:**
Schreibe ein Programm, das eine einfache Konzertkarte als Textgrafik ausgibt. Das Programm fragt nach dem Namen des Konzertbesuchers, dem Namen der Band und dem Veranstaltungsort. Anschließend wird eine formatierte Eintrittskarte auf der Konsole ausgegeben.

**Lernziele:**
- `input()` für mehrere thematisch zusammenhängende Eingaben verwenden.
- Eine kreative, strukturierte Textgrafik mit `print()` und f-Strings gestalten.
- Den Unterschied zwischen festen Texten (Rahmen, Beschriftungen) und dynamischen Inhalten (Variablen) in der Ausgabe erkennen.

***Hinweise:***
- Die Rahmenzeichen kannst du einfach kopieren und in deinen Code einfügen.
- Die exakte Breite des Rahmens muss nicht pixelgenau stimmen – Hauptsache, die Struktur ist erkennbar.

**Erwartetes Ergebnis:**

- bei Eingabe von `Lisa`, `The Rolling Stones`, `Hamburg Barclays Arena`

```
Name des Besuchers: Lisa
Name der Band: The Rolling Stones
Veranstaltungsort: Hamburg Barclays Arena

===================================
       *** KONZERTKARTE ***
===================================
  Besucher: Lisa
  Band:     The Rolling Stones
  Ort:      Hamburg Barclays Arena
===================================
Viel Spass beim Konzert!
```

---

## Aufgabe 01-Z5: Chatbot-Einstieg
*(ca. 20 Minuten)*

**Nutze die Datei `src/kapitel_01/aufgabe_01-Z5.py` für Deine Lösung.**

**Aufgabenstellung:**
Schreibe ein Programm, das einen einfachen Chatbot simuliert. Der Bot soll sich vorstellen, den Benutzer nach seinem Namen und seiner Lieblingsprogrammiersprache fragen und anschließend eine individuelle Reaktion ausgeben.

**Lernziele:**
- Den Inhalt einer Variablen im prompt-Text einer `input()`-Funktion wiederverwenden, um einen dynamischen Dialog zu erzeugen.
- Mehrere Variablen in zusammenhängenden f-Strings kombinieren.
- Eine mehrstufige, dialogartige Konversation programmieren.

**Erwartetes Ergebnis:**

- bei Eingabe von `Yusuf` und `Python`

```
Bot: Hallo! Ich bin PyBot. Wie heißt du?
Du:  Yusuf
Bot: Schoen, dich kennenzulernen, Yusuf! Was ist deine Lieblingsprogrammiersprache?
Du:  Python
Bot: Ausgezeichnete Wahl! Python ist fantastisch. Ich bin selbst in Python geschrieben, Yusuf!
```

***Hinweise:***
- Für die "Du:"-Zeilen nutze `input()` mit dem entsprechenden Prompt-Text.
- Die Antwort des Bots kannst du danach mit `print()` ausgeben.

---

## Aufgabe 01-Z6: Bewerbungsanschreiben-Generator
*(Integrationsaufgabe, ca. 30 Minuten)*

**Nutze die Datei `src/kapitel_01/aufgabe_01-Z6.py` für Deine Lösung.**

**Aufgabenstellung:**
Schreibe ein Programm, das die wichtigsten Informationen für ein Bewerbungsanschreiben abfragt und daraus automatisch einen formatierten Brieftext erzeugt. Das Programm soll folgende Informationen abfragen: den Namen des Bewerbers, die angestrebte Stelle, den Namen des Unternehmens und eine persönliche Stärke des Bewerbers.

**Lernziele:**
- Alle Grundkonzepte des Kapitels (mehrere input()-Aufrufe, sinnvolle Variablennamen, f-Strings, mehrzeilige Ausgabe) in einer Anwendung kombinieren.
- Eine realistische Ausgabe mit fixen Textbausteinen und dynamischen Variablen gestalten.
- Den Nutzen von Variablen zur Wiederverwendung von Inhalten erkennen (der Name taucht mehrfach auf).

***Hinweise:***
- Der Name des Bewerbers wird im Brief mehrfach verwendet – speichere ihn in einer Variablen und nutze diese mehrfach.
- Eine Trennlinie lässt sich mit `print("-" * 40)` erzeugen.

**Erwartetes Ergebnis:**

- bei Eingabe von `Erika Musterfrau`, `Python-Entwicklerin`, `TechCorp GmbH`, `Problemloesungskompetenz`

```
Dein Name: Erika Musterfrau
Angestrebte Stelle: Python-Entwicklerin
Name des Unternehmens: TechCorp GmbH
Deine groesste Staerke: Problemloesungskompetenz

----------------------------------------
Sehr geehrte Damen und Herren,

hiermit bewerbe ich mich, Erika Musterfrau,
auf die ausgeschriebene Stelle als Python-Entwicklerin
bei der TechCorp GmbH.

Ich bringe ausgepragte Problemloesungskompetenz mit
und bin ueberzeugt, damit einen wertvollen Beitrag
in Ihrem Team leisten zu koennen.

Ich freue mich auf Ihre Rueckmeldung.

Mit freundlichen Gruessen,
Erika Musterfrau
----------------------------------------
```
