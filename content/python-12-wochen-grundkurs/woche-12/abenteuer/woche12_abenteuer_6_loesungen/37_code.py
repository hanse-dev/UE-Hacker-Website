def zerlege(text):
    try:
        aktion, ziel = text.split()
    except ValueError:
        return None
    return (aktion, ziel)

print(zerlege("gehe norden"))
print(zerlege("hallo"))
