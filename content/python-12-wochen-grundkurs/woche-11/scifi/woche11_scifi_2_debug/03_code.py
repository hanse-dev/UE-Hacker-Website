class roboter:
    bewegen():
        print("Roboter bewegt sich")

class drohne(roboter):
    fliegen():
        print("Drohne fliegt")

meine_drohne = drohne()
meine_drohne.bewegen()