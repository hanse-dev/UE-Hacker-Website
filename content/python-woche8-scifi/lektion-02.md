# 🚀 Daten-Log 2: Ändern, ergänzen und entfernen

Ein Dictionary ist **veränderlich**: Du kannst Werte überschreiben, neue Einträge anlegen und Einträge löschen.

```python
mitglied["rang"] = 20          # vorhandenen Schlüssel: Wert wird überschrieben
mitglied["rang"] += 1          # rechnen geht auch
mitglied["schild"] = 80       # neuer Schlüssel: Eintrag wird ergänzt

alt = mitglied.pop("energie")       # entfernt den Eintrag und gibt den Wert zurück
del mitglied["rolle"]             # entfernt den Eintrag ohne Rückgabe
```

Dieselbe Schreibweise `dict[schlüssel] = wert` ändert also **oder** ergänzt – je nachdem, ob der Schlüssel schon existiert.
