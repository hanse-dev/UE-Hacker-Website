# Funktionen – dein eigener Zauberspruch 🪄

Eine Funktion ist ein wiederverwendbarer Code-Block. Du definierst ihn einmal mit `def` und einem Namen – und kannst ihn danach beliebig oft aufrufen, ohne den Code nochmal zu schreiben!

```python
def zaubern():
    print("Abrakadabra!")

zaubern()  # ruft die Funktion auf
zaubern()  # und nochmal!
```

Das Wort `def` bedeutet "definiere" – du erklärst Python damit einen neuen Zauberspruch, der aber erst passiert, wenn du ihn auch tatsächlich **aufrufst** (also den Namen gefolgt von `()` schreibst). Nur `def zaubern():` alleine gibt noch nichts aus!

Funktionen können auch Werte entgegennehmen – solche Werte heißen **Parameter** und stehen in den Klammern:

```python
def begruessen(name):
    print(f"Hallo, {name}!")

begruessen("Luna")   # gibt "Hallo, Luna!" aus
begruessen("Finn")   # gibt "Hallo, Finn!" aus
```

Bei jedem Aufruf kannst du einen anderen Wert übergeben – der Parameter `name` nimmt dann innerhalb der Funktion genau diesen Wert an. Das ist der ganze Trick: Ein Zauberspruch, der sich je nach Zutat anders verhält.
