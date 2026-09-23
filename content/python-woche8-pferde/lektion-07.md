# 🐴 Übung 7: Verschachtelte Strukturen

Werte in einem Dictionary dürfen selbst Dictionaries oder Listen sein – und Listen dürfen Dictionaries enthalten:

```python
pferd["ausruestung"] = {"sattel": "Leder", "decke": "Wolle"}
print(pferd["ausruestung"]["sattel"])   # zwei Schlüssel hintereinander: Leder

pferde = [{"name": "Blitz", "alter": 8}, {"name": "Sturm", "alter": 12}]
for e in pferde:
    print(e["name"])

starke = [e["name"] for e in pferde if e["alter"] > 7]   # List Comprehension mit Bedingung
```

Du liest von außen nach innen: erst der äußere Schlüssel, dann der innere. Auch ein Tupel kann Schlüssel sein: `{(2, 3): "Punkt A"}`.
