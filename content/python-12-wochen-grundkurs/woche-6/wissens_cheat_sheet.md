# Wissens-Cheat-Sheet: Woche 6

_Zusammenfassung aller Themen aus Woche 1–5_

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

---

## Woche 3: Bedingungen (if-else)

### if, if-else, if-elif-else
Entscheidungen: Nur bestimmter Code wird ausgeführt, wenn die Bedingung erfüllt ist.

```python
if alter >= 18:
    print("Volljährig")
elif alter >= 16:
    print("Fast volljährig")
else:
    print("Minderjährig")
```

### Vergleichsoperatoren
`==` (gleich), `!=` (ungleich), `<`, `>`, `<=`, `>=`

### Logische Operatoren
`and` (beides wahr), `or` (mindestens eines wahr), `not` (verneinen)

### Verschachtelte Bedingungen
if-Blöcke in if-Blöcken – Einrückung mit 4 Leerzeichen ist entscheidend.

---

## Woche 4: Schleifen (for, while)

### for mit range()
Wiederholt Code eine feste Anzahl – `range(n)` liefert 0 bis n-1.

```python
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4
```

### while-Schleife
Läuft, solange die Bedingung wahr ist.

```python
while zähler < 10:
    zähler += 1
```

### Schleifen über Sequenzen
Über Strings oder Listen iterieren – jedes Element durchgehen.

```python
for zeichen in "Hallo":
    print(zeichen)
```

### break und continue
`break` beendet die Schleife sofort. `continue` überspringt den Rest.

### Verschachtelte Schleifen
Schleife innerhalb einer Schleife – z.B. für Muster oder Tabellen.

---

## Woche 5: Funktionen

### def und Parameter
Code-Blöcke wiederverwenden. Parameter sind Platzhalter für Werte beim Aufruf.

```python
def grüßen(name):
    print(f"Hallo, {name}!")
grüßen("Anna")
```

### return
Gibt einen Wert zurück – die Funktion wird zu diesem Wert.

```python
def verdoppeln(x):
    return x * 2
ergebnis = verdoppeln(5)
```

### Docstrings
Erklären die Funktion in drei Anführungszeichen direkt unter `def`.

```python
def addieren(a, b):
    """Addiert zwei Zahlen."""
    return a + b
```

### Standardwerte
Parameter können einen Vorgabewert haben.

```python
def sagen(text, ende="."):
    print(text + ende)
sagen("Hallo")  # Ende ist "."
```
