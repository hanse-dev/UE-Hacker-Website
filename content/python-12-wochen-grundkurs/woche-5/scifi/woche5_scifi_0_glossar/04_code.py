# Einfache Funktion
def begrüße(name):
    print("Willkommen an Bord, " + name + "!")

begrüße("Kirk")

# Funktion mit return
def verdopple(zahl):
    return zahl * 2

ergebnis = verdopple(5)
print(ergebnis)  # 10

# try / except
def teile(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Fehler: Division durch 0!"

print(teile(10, 2))  # 5.0
print(teile(10, 0))  # Fehler: Division durch 0!
