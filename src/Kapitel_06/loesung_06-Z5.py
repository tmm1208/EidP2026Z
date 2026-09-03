# Aufgabe 06-Z5: Telefonbuch
# Musterlösung

telefonbuch = {}

while True:
    befehl = input("Befehl (add/search/delete/show/quit): ")

    if befehl == "add":
        name = input("Name: ")
        nummer = input("Nummer: ")
        telefonbuch[name] = nummer

    elif befehl == "search":
        name = input("Name: ")
        ergebnis = telefonbuch.get(name)
        if ergebnis:
            print(f"{name}: {ergebnis}")
        else:
            print(f"'{name}' nicht im Telefonbuch.")

    elif befehl == "delete":
        name = input("Name: ")
        if name in telefonbuch:
            del telefonbuch[name]
            print(f"'{name}' gelöscht.")
        else:
            print(f"'{name}' nicht im Telefonbuch.")

    elif befehl == "show":
        if len(telefonbuch) == 0:
            print("Das Telefonbuch ist leer.")
        else:
            for name, nummer in telefonbuch.items():
                print(f"{name}: {nummer}")

    elif befehl == "quit":
        print("Tschüss!")
        break

    else:
        print("Unbekannter Befehl. Verfügbar: add, search, delete, show, quit")
