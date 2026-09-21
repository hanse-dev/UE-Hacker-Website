# 🚀 KI-Modul 2: Methoden überschreiben

Manchmal soll ein Kind etwas **anders** machen als seine Eltern. Dann schreibst du die Methode mit **demselben Namen** noch einmal – sie **überschreibt** die geerbte:

```python
class Roboter:
    def __init__(self, name):
        self.name = name

    def stelle_vor(self):
        print(f"Ich bin {self.name}.")

    def arbeite(self):
        print(f"{self.name} läuft im Leerlauf.")

class Kampfroboter(Roboter):
    def arbeite(self):
        print(f"{self.name} feuert den Laser ab.")

Roboter("Nova").arbeite()
Kampfroboter("Orbit").arbeite()
```

1. Python nimmt immer die Methode der **eigenen** Klasse zuerst
2. Gibt es dort keine, sucht es bei den **Eltern**
3. Die Eltern-Klasse bleibt unverändert
