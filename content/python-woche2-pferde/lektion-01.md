# 🐴 Woche 2: Die vier Hufschlag-Typen

Willkommen zurück auf dem **Reiterhof Sonnental**! Hier beherrscht man die vier fundamentalen Reittechniken. In dieser Woche lernst du die vier **Hufschlag-Typen** – die vier Datentypen von Python:

1. Moderne Nachrichten mit **f-Strings**
2. 🚶 **Schritt** – Text (`str`)
3. 🐎 **Trab** – Ganze Zahlen (`int`)
4. 🏇 **Galopp** – Kommazahlen (`float`)
5. 🦘 **Sprung** – Wahrheitswerte (`bool`)
6. Rechnen mit Zahlen und Texten
7. Typen **umwandeln**
8. Eingaben verarbeiten

Auch diese Woche gilt: Jede **Übung** ist eine **Funktion**, die du mit **Klammern** aufrufst – wie `print()` aus Woche 1.

## 📣 Übung 1: f-Strings

In Woche 1 hast du Text und Zahlen mit `+` und `str()` verbunden. Das geht auch einfacher: Setze ein **`f`** vor die Anführungszeichen und schreibe Variablen in **geschweifte Klammern** `{}`.

```python
pferd_name = "Thunder"
alter = 8
print(f"Hallo {pferd_name}! Du bist {alter} Jahre alt!")
```

In den Klammern darf sogar gerechnet werden: `f"Futter: {morgens + abends} kg"`.

> 🐴 **Wichtig:** Ohne das `f` vor den Anführungszeichen wird `{alter}` einfach als Text ausgegeben!
