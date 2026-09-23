# Das Inventar

Damit sich dein Fluchtraum wie ein echtes Spiel anfühlt, braucht die spielende Person ein **Inventar** – die Gegenstände, die sie bisher eingesammelt hat. Eine Liste passt perfekt dafür: Sie beginnt leer, und jeder gefundene Gegenstand wird per `append()` hinzugefügt.

```python
inventar = []
inventar.append("schluessel")
print(inventar)
```

Um später zu prüfen, ob ein bestimmter Gegenstand schon eingesammelt wurde, nutzt du `in` – du kennst das schon aus dem Zahlen-Detektiv-Projekt, nur diesmal auf einer Liste statt auf einem Bereich von Zahlen:

```python
if "schluessel" in inventar:
    print("Du hast den Schlüssel dabei.")
else:
    print("Kein Schlüssel.")
```

`in` durchsucht die ganze Liste und liefert `True` oder `False` – egal wie viele Gegenstände schon im Inventar liegen.
