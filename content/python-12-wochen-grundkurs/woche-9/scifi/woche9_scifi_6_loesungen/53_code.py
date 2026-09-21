with open("bordbuch.txt", "w") as f:
    f.write("Bordbuch Nebula-7\n")
    f.write("Status: Aktiv\n")
    f.write("Signal empfangen\n")
def zeilen_zaehlen(name):
    try:
        with open(name, "r") as f:
            return len(f.readlines())
    except FileNotFoundError:
        return 0

print(f"bordbuch.txt: {zeilen_zaehlen('bordbuch.txt')}")
print(f"fehlt.txt: {zeilen_zaehlen('fehlt.txt')}")
