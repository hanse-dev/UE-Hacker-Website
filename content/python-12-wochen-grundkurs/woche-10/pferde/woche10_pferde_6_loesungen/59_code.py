class Pferd:
    def __init__(self, name):
        self.name = name
        self.energie = 100

    def galoppiere(self, kosten):
        self.energie -= kosten
        if self.energie < 0:
            self.energie = 0

pferd = Pferd("Blitz")
pferd.galoppiere(40)
pferd.galoppiere(40)
pferd.galoppiere(40)
print(f"Energie: {pferd.energie}")
