with open("stallbuch.txt", "w") as f:
    f.write("Stallbuch Reiterhof\n")
    f.write("Status: Geöffnet\n")
    f.write("Ausritt geplant\n")
def zeilen_zaehlen(name):
    try:
        with open(name, "r") as f:
            return len(f.readlines())
    except FileNotFoundError:
        return 0

print(f"stallbuch.txt: {zeilen_zaehlen('stallbuch.txt')}")
print(f"fehlt.txt: {zeilen_zaehlen('fehlt.txt')}")
