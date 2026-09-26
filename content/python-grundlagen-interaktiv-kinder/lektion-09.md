# Dictionaries – das Tierlexikon 📖

Bei einer Liste findest du Werte über ihre Position (`tiere[0]`). Ein Dictionary funktioniert anders: Es speichert Schlüssel-Wert-Paare – wie ein echtes Wörterbuch, in dem du nicht die Seite, sondern das Wort selbst nachschlägst!

```python
tier_infos = {"Hund": "bellt", "Katze": "miaut"}
print(tier_infos["Hund"])  # gibt "bellt" aus
```

Hier ist `"Hund"` der Schlüssel und `"bellt"` der dazugehörige Wert. Du schreibst das Dictionary in geschweiften Klammern `{}`, jedes Paar getrennt durch einen Doppelpunkt, und mehrere Paare durch Kommas getrennt.

Du kannst jederzeit neue Einträge hinzufügen – einfach einen neuen Schlüssel in eckigen Klammern angeben und einen Wert zuweisen:

```python
tier_infos["Vogel"] = "zwitschert"
print(tier_infos["Vogel"])
```

**Achtung:** Fragst du nach einem Schlüssel, den es nicht gibt (z.B. `tier_infos["Fisch"]`), meldet Python einen Fehler (`KeyError`). Ein Dictionary kennt eben nur die Schlüssel, die du auch wirklich reingetan hast.
