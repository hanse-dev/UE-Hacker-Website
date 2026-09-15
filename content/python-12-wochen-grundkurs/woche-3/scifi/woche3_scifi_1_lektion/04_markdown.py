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
      print(\"Zugriffslevel 10 erreicht!\")
  ```

### Die vier Vergleichsalgorithmen

- **`<` (kleiner als)**: Prüft, ob der linke Wert kleiner ist
  ```python
  if energie < 20:
      print(\"⚠️ Niedrige Energie!\")
  ```

- **`<=` (kleiner oder gleich)**: Prüft, ob der linke Wert kleiner oder gleich ist
  ```python
  if temperatur <= 100:
      print(\"🌡️ Normale Temperatur!\")
  ```

- **`>` (größer als)**: Prüft, ob der linke Wert größer ist
  ```python
  if geschwindigkeit > 1000:
      print(\"💨 Überlichtgeschwindigkeit!\")
  ```

- **`>=` (größer oder gleich)**: Prüft, ob der linke Wert größer oder gleich ist
  ```python
  if schildstaerke >= 50:
      print(\"🛡️ Schilde stabil!\")
  ```

**Merke:** In Bedingungen immer `==` für Vergleiche verwenden, nie `=`!"""
