# ⚔️ Archiv-Zauber 7: Verschachtelte Strukturen

Werte in einem Dictionary dürfen selbst Dictionaries oder Listen sein – und Listen dürfen Dictionaries enthalten:

```python
held["ausruestung"] = {"waffe": "Stab", "ruestung": "Robe"}
print(held["ausruestung"]["waffe"])   # zwei Schlüssel hintereinander: Stab

helden = [{"name": "Aria", "level": 15}, {"name": "Thorin", "level": 18}]
for e in helden:
    print(e["name"])

starke = [e["name"] for e in helden if e["level"] > 14]   # List Comprehension mit Bedingung
```

Du liest von außen nach innen: erst der äußere Schlüssel, dann der innere. Auch ein Tupel kann Schlüssel sein: `{(2, 3): "Punkt A"}`.
