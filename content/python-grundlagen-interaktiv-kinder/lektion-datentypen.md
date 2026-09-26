# Datentypen – was steckt dahinter? 🔍

Jeder Wert in Python hat einen Typ – also eine Art, die festlegt, was man damit machen kann. Python kennt vier wichtige Grundtypen:

- **int** – ganze Zahlen wie `42` (int steht für "Integer")
- **float** – Kommazahlen wie `3.14` (float, weil der Punkt "schwimmt")
- **str** – Text wie `"Hallo"` (str steht für "String", eine Kette von Buchstaben)
- **bool** – Wahr oder Falsch: `True` oder `False` (bool steht für "Boolean")

Anders als in manchen anderen Programmiersprachen musst du den Typ nicht selbst festlegen – Python erkennt ihn automatisch daran, wie du den Wert aufschreibst. Zahlen ohne Anführungszeichen sind `int` oder `float`, alles in Anführungszeichen ist `str`.

Mit `type()` kannst du jederzeit herausfinden, welcher Typ ein Wert hat:

```python
print(type(42))       # <class 'int'>
print(type("Hallo"))  # <class 'str'>
```

Manchmal möchtest du einen Wert in einen anderen Typ umwandeln – z.B. weil du eine Zahl bekommen hast, die als Text gespeichert ist (`"18"` statt `18`). Dafür gibt es `int()`, `float()` und `str()`:

```python
alter_als_text = "18"
alter_als_zahl = int(alter_als_text)
print(alter_als_zahl + 1)  # gibt 19 aus
```

**Wichtig:** `"18" + 1` funktioniert nicht (Fehler!), weil man Text und Zahlen nicht einfach so addieren kann – erst nach der Umwandlung mit `int()` klappt es.
