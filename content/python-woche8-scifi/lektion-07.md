# 🚀 Daten-Log 7: Verschachtelte Strukturen

Werte in einem Dictionary dürfen selbst Dictionaries oder Listen sein – und Listen dürfen Dictionaries enthalten:

```python
mitglied["ausruestung"] = {"werkzeug": "Laser", "anzug": "Raumanzug"}
print(mitglied["ausruestung"]["werkzeug"])   # zwei Schlüssel hintereinander: Laser

crew = [{"name": "Nova", "rang": 4}, {"name": "Rex", "rang": 6}]
for e in crew:
    print(e["name"])

starke = [e["name"] for e in crew if e["rang"] > 3]   # List Comprehension mit Bedingung
```

Du liest von außen nach innen: erst der äußere Schlüssel, dann der innere. Auch ein Tupel kann Schlüssel sein: `{(2, 3): "Punkt A"}`.
