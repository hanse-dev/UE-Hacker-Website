"""## Wichtige Operatoren

### Zuweisung vs Vergleich: = vs ==

**Das ist ein entscheidender Unterschied!**

- **`=` (ein Gleichheitszeichen)**: Weist einer Variable einen Wert zu
  ```python
  level = 10  # Weise level den Wert 10 zu
  ```

- **`==` (zwei Gleichheitszeichen)**: Vergleicht zwei Werte auf Gleichheit
  ```python
  if level == 10:  # Prüfe OB level 10 ist
      print(\"Level 10 erreicht!\")
  ```

### Die vier Vergleichsrunen

- **`<` (kleiner als)**: Prüft, ob der linke Wert kleiner ist
  ```python
  if level < 10:
      print(\"Noch nicht Level 10\")
  ```

- **`<=` (kleiner oder gleich)**: Prüft, ob der linke Wert kleiner oder gleich ist
  ```python
  if level <= 10:
      print(\"Level 10 oder niedriger\")
  ```

- **`>` (größer als)**: Prüft, ob der linke Wert größer ist
  ```python
  if level > 10:
      print(\"Über Level 10!\")
  ```

- **`>=` (größer oder gleich)**: Prüft, ob der linke Wert größer oder gleich ist
  ```python
  if level >= 10:
      print(\"Level 10 oder höher\")
  ```

**Merke:** In Bedingungen immer `==` für Vergleiche verwenden, nie `=`!"""
