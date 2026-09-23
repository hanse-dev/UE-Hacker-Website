# 🐴 Übung 2: Ändern, ergänzen und entfernen

Ein Dictionary ist **veränderlich**: Du kannst Werte überschreiben, neue Einträge anlegen und Einträge löschen.

```python
pferd["alter"] = 20          # vorhandenen Schlüssel: Wert wird überschrieben
pferd["alter"] += 1          # rechnen geht auch
pferd["siege"] = 3       # neuer Schlüssel: Eintrag wird ergänzt

alt = pferd.pop("punkte")       # entfernt den Eintrag und gibt den Wert zurück
del pferd["rasse"]             # entfernt den Eintrag ohne Rückgabe
```

Dieselbe Schreibweise `dict[schlüssel] = wert` ändert also **oder** ergänzt – je nachdem, ob der Schlüssel schon existiert.
