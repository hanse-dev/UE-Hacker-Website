class drache:
    def fliegen():
        print("Der Drache fliegt!")

class feuerspucker(drache):
    def feuerspeien():
        print("Feuer! 🔥")

drache = feuerspucker()
drache.fliegen()