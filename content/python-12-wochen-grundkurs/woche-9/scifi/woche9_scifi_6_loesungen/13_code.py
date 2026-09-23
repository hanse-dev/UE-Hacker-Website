try:
    with open("fehlt.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Keine Datei: fehlt.txt")
