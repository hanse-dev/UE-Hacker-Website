# 🚀 Woche 2 – Die vier Quanten-Typen

Willkommen zurück, Kommandant:in! Du betrittst das **Datenlabor der Nebula-7** – ein Ort, an dem die vier fundamentalen **Quanten-Typen** beherrscht werden. In dieser Woche lernst du:

1. Meldungen mit **f-Strings** bauen
2. **Strings** und **Integer** (Text und ganze Zahlen)
3. **Floats** und **Booleans** (Kommazahlen und Ja/Nein-Werte)
4. Mit Zahlen **rechnen**
5. Texte mit `+` und `*` verbinden
6. Typen **umwandeln** mit `int()`, `float()`, `str()` und `bool()`

## 📟 Systemprotokoll 1: f-Strings

Der **f-String** ist die moderne Methode, Text und Variablen zu einer Nachricht zu verschmelzen. Setze ein **`f` vor die Anführungszeichen** und schreibe Variablen in **geschweifte Klammern `{}`**:

```python
pilot = "Zara"
print(f"Hallo {pilot}!")
```

Der Wert der Variable wird an der Stelle der Klammern eingesetzt. Und das Beste: Zahlen brauchen hier **kein** `str()` (das kennst du aus Woche 1)! In den Klammern darf sogar **gerechnet** werden:

```python
print(f"Gesamt: {75 + 25}%")
```

> 📡 **Merke:** Ohne das `f` vor dem Text werden die Klammern einfach als normaler Text ausgegeben – vergiss das `f` nicht!
