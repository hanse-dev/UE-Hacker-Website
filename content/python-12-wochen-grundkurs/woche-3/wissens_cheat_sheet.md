# Wissens-Cheat-Sheet: Woche 3

_Zusammenfassung aller Themen aus Woche 1–2_

## Woche 1: Einführung und erstes Programm

### print()
Gibt Text auf dem Bildschirm aus. Text steht in Anführungszeichen.

```python
print("Hallo Welt!")
```

### Variablen
Speichern Informationen für spätere Verwendung. Ein Name wird einem Wert zugewiesen.

```python
name = "Python"
anzahl = 3
```

### String-Kombination mit + und str()
Texte mit `+` verbinden. Zahlen mit `str()` in Text umwandeln, um sie einzubauen.

```python
print("Ich heiße " + name)
print("Anzahl: " + str(anzahl))
```

### Kommentare
Mit `#` werden Zeilen ignoriert – für Erklärungen im Code.

```python
# Das ist ein Kommentar
x = 5  # x hat den Wert 5
```

---

## Woche 2: Datentypen und Variablen

### f-Strings
Moderne Textformatierung: Variablen in geschweiften Klammern einfügen.

```python
print(f"Name: {name}, Anzahl: {anzahl}")
```

### Die vier Datentypen
- **String** (str): Text in Anführungszeichen
- **Integer** (int): Ganze Zahlen
- **Float** (float): Dezimalzahlen
- **Boolean** (bool): `True` oder `False`

```python
text = "Hallo"
zahl = 42
komma = 3.14
wahr = True
```

### Operationen
Mathematik mit Zahlen, String-Verkettung mit `+`, Wiederholung mit `*`.

```python
ergebnis = 10 + 5
text_lang = "A" * 3  # "AAA"
```

### Typumwandlungen
`int()`, `float()`, `str()` wandeln zwischen Datentypen um.

```python
x = int("42")
text = str(3.14)
```
