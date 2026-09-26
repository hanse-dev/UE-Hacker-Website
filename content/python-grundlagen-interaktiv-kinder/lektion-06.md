# Schleifen mit for 🔄

Stell dir vor, du müsstest "Hallo!" zehnmal ausgeben – willst du wirklich zehnmal `print("Hallo!")` tippen? Mit `for` kannst du Code mehrmals ausführen, ohne ihn zu wiederholen. `range(3)` liefert dabei die Zahlen 0, 1, 2 (also drei Zahlen, aber bei 0 beginnend).

```python
for i in range(3):
    print("Hallo!")
# gibt dreimal "Hallo!" aus
```

Die Variable `i` bekommt bei jedem Durchlauf einen neuen Wert aus der Reihe – du kannst sie also auch direkt benutzen:

```python
for i in range(3):
    print(i)
# gibt 0, 1, 2 aus (jeweils in eigener Zeile)
```

Du kannst auch direkt über eine Liste von Tieren gehen, ganz ohne `range()` – dann bekommst du bei jedem Durchlauf ein Element der Liste:

```python
tiere = ["Hund", "Katze", "Vogel"]
for tier in tiere:
    print(tier)
```

Genau wie beim `if` muss der Code, der wiederholt werden soll, eingerückt sein. Alles, was nicht eingerückt ist, gehört nicht mehr zur Schleife und läuft nur einmal.
