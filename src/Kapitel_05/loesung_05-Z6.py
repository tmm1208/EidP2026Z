# Aufgabe 05-Z6: Playlist-Verwaltung
# Musterlösung

playlist = []

while True:
    befehl = input("Befehl (add/remove/show/sort/quit): ")

    if befehl == "add":
        song = input("Song: ")
        playlist.append(song)

    elif befehl == "remove":
        song = input("Song: ")
        if song in playlist:
            del playlist[playlist.index(song)]
            print(f"'{song}' entfernt.")
        else:
            print(f"'{song}' ist nicht in der Playlist.")

    elif befehl == "show":
        if len(playlist) == 0:
            print("Die Playlist ist leer.")
        else:
            for i in range(len(playlist)):
                print(f"{i + 1}. {playlist[i]}")

    elif befehl == "sort":
        playlist.sort()
        print("Playlist sortiert.")

    elif befehl == "quit":
        print("Tschüss!")
        break

    else:
        print("Unbekannter Befehl. Verfügbar: add, remove, show, sort, quit")
