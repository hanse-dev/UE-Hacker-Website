# 🔤 Buchstaben durchlaufen

Eine `for`-Schleife kann nicht nur Zahlen, sondern auch die **Buchstaben eines Textes** einzeln durchlaufen:

```python
name = "Aria"
for buchstabe in name:
    print(f"  - {buchstabe}")
```

Das gibt nacheinander `A`, `r`, `i`, `a` aus. Python behandelt den Text wie eine Kette von Zeichen, und `buchstabe` ist bei jedem Durchlauf das nächste Zeichen.

Damit kannst du zum Beispiel **Buchstaben zählen** – ganz ohne `len()`:

```python
anzahl = 0
for buchstabe in "Drache":
    anzahl += 1
```
