# ⚔️ Evolutions-Zauber 2: Methoden überschreiben

Manchmal soll ein Kind etwas **anders** machen als seine Eltern. Dann schreibst du die Methode mit **demselben Namen** noch einmal – sie **überschreibt** die geerbte:

```python
class Held:
    def __init__(self, name):
        self.name = name

    def stelle_vor(self):
        print(f"Ich bin {self.name}.")

    def kaempfe(self):
        print(f"{self.name} kämpft mit bloßen Händen.")

class Krieger(Held):
    def kaempfe(self):
        print(f"{self.name} schwingt das Schwert.")

Held("Aria").kaempfe()
Krieger("Thorin").kaempfe()
```

1. Python nimmt immer die Methode der **eigenen** Klasse zuerst
2. Gibt es dort keine, sucht es bei den **Eltern**
3. Die Eltern-Klasse bleibt unverändert
