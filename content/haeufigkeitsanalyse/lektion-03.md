# Das Balkendiagramm

Ein Dictionary voller Zahlen ist schwer zu überblicken. Viel schneller sieht man Unterschiede in einem **Balkendiagramm** – und das kannst du ganz ohne Grafik bauen, nur mit dem Zeichen `#`.

Dafür brauchst du zwei kleine Tricks:

```python
print("#" * 5)                    # #####
print(sorted({'t': 2, 'o': 2}))   # ['o', 't']
```

- Ein String mal eine Zahl wiederholt den String – `"#" * 5` ergibt fünf Rauten.
- `sorted()` liefert die Schlüssel aus einem Dictionary in alphabetischer Reihenfolge. So stehen die Buchstaben im Diagramm ordentlich von `a` bis `z`.

So läuft das Prinzip ab:

```
zaehlung = zaehle_buchstaben(text)
für jeden buchstabe in den sortierten Schlüsseln von zaehlung:
    gib aus: den buchstaben, so viele "#" wie seine Anzahl, und die Anzahl
```

Übergibst du `print()` mehrere Werte mit Komma getrennt, setzt es automatisch ein Leerzeichen dazwischen. Für das Wort `"otto"` sähe das Diagramm so aus:

```
o ## 2
t ## 2
```

In der zweiten Aufgabe zeichnest du das Diagramm für die abgefangene Nachricht. Achte auf den längsten Balken – er verrät gleich den Schlüssel.

> 💡 Deine Funktion `zaehle_buchstaben` aus der letzten Lektion steht schon fertig im Editor. Du musst nur noch die Schleife für die Ausgabe schreiben.
