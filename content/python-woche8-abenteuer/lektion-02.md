# ⚔️ Archiv-Zauber 2: Ändern, ergänzen und entfernen

Ein Dictionary ist **veränderlich**: Du kannst Werte überschreiben, neue Einträge anlegen und Einträge löschen.

```python
held["level"] = 20          # vorhandenen Schlüssel: Wert wird überschrieben
held["level"] += 1          # rechnen geht auch
held["mana"] = 80       # neuer Schlüssel: Eintrag wird ergänzt

alt = held.pop("leben")       # entfernt den Eintrag und gibt den Wert zurück
del held["klasse"]             # entfernt den Eintrag ohne Rückgabe
```

Dieselbe Schreibweise `dict[schlüssel] = wert` ändert also **oder** ergänzt – je nachdem, ob der Schlüssel schon existiert.
