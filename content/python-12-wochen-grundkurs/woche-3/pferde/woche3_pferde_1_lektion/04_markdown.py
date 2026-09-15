"""## Wichtige Operatoren

### Zuweisung vs Vergleich: = vs ==

**Das ist ein entscheidender Unterschied!**

- **`=` (ein Gleichheitszeichen)**: Weist einer Variable einen Wert zu

```python
alter = 10  # Weise alter den Wert 10 zu
```

- **`==` (zwei Gleichheitszeichen)**: Vergleicht zwei Werte auf Gleichheit

```python
if alter == 10:  # Prüfe OB alter 10 ist
    print(\"Das Pferd ist 10 Jahre alt!\")
```

### Die vier Vergleichsoperatoren

- **`<` (kleiner als)**: Prüft, ob der linke Wert kleiner ist

```python
if alter < 5:
    print(\"Noch ein Fohlen!\")
```

- **`<=` (kleiner oder gleich)**: Prüft, ob der linke Wert kleiner oder gleich ist

```python
if alter <= 5:
    print(\"Junges Pferd oder Fohlen!\")
```

- **`>` (größer als)**: Prüft, ob der linke Wert größer ist

```python
if alter > 15:
    print(\"Ein erfahrenes Pferd!\")
```

- **`>=` (größer oder gleich)**: Prüft, ob der linke Wert größer oder gleich ist

```python
if alter >= 3:
    print(\"Alt genug zum Reiten!\")
```

**Merke:** In Bedingungen immer `==` für Vergleiche verwenden, nie `=`!"""
