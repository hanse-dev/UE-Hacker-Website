def lese_oder_leer(name):
    try:
        with open(name, "r") as f:
            return f.read()
    except FileNotFoundError:
        return ""

print(f"Leer: {lese_oder_leer('fehlt.txt') == ''}")
with open("stallbuch.txt", "w") as f:
    f.write("Stallbuch Reiterhof\n")
print(f"Inhalt: {lese_oder_leer('stallbuch.txt').strip()}")
