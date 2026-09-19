# 🔥🪨💧💨 Zauberformel 2: type() und die vier Elemente

Die Turmwächterin zeigt dir die vier Elementsteine. Jeder hat eine eigene **Natur** – in Python nennen wir das den **Typ** eines Werts.

| Element | Typ | Fachbegriff | Beispiel | Natur |
|---------|-----|------------|---------|-------|
| 🔥 Feuer | Text | `str` | `"Feuerball"` | ausgesprochene Worte, Namen, Zaubersprüche |
| 🪨 Erde | Ganze Zahl | `int` | `42` | fest und zählbar – Level, Gold, Punkte |
| 💧 Wasser | Kommazahl | `float` | `3.14` | fließend, nie ganz genau – Prozente, Schaden |
| 💨 Luft | Wahrheitswert | `bool` | `True` / `False` | unsichtbar, nur da oder nicht da – Schalter |

## `type()` – der Elementsucher

Auch `type()` ist eine **Zauberformel (Funktion)**, genau wie `print()` aus Woche 1: Du rufst sie mit Klammern auf und gibst ihr in die Klammern einen Wert. Sie liefert dir den Typ zurück:

```python
name = "Aria"
print(type(name))    # <class 'str'>  -> Feuer-Element
print(type(42))      # <class 'int'>  -> Erd-Element
```

Beachte: `type()` **liefert** den Typ nur zurück – sichtbar wird er erst, wenn du ihn mit `print()` ausgibst.
