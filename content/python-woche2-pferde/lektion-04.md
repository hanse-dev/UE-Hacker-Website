# 🏇 Übung 4: Galopp – Kommazahlen

Der Galopp ist ein fließender Drei-Takt, nie ganz exakt gleich. Passend dazu sind **Floats** (`float`) **Kommazahlen** – etwa das Gewicht (`550.5`) oder eine Futtermenge (`4.25`).

> ⚠️ Python schreibt das Komma als **Punkt**: `4.25`, nicht `4,25`!

```python
gewicht = 550.5
futter_menge = 4.25
print(f"Gewicht: {gewicht} kg, Futter: {futter_menge} kg")
print(type(gewicht))   # <class 'float'>
```

Sobald eine Zahl einen Punkt hat, ist sie ein `float` – auch `5.0` ist eine Kommazahl, `5` dagegen eine ganze Zahl.
