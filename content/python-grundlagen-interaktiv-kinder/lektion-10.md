# Kleine Übung: Alles zusammen! 🏆

Du hast so viel gelernt! Variablen, Rechnen, f-Strings, `if`, `for`-Schleifen, Listen, Funktionen und Dictionaries – das sind schon die wichtigsten Bausteine, aus denen fast jedes Python-Programm besteht. Jetzt kombinieren wir alles in einem Beispiel:

```python
tiere = ["Hund", "Katze", "Vogel"]
for tier in tiere:
    print(f"Das Tier heißt: {tier}")
```

Hier siehst du drei Dinge zusammen: eine Liste (`tiere`), eine `for`-Schleife, die jeden Eintrag durchgeht, und einen f-String, der den aktuellen Wert (`tier`) in einen Satz einbaut.

Und mit einer Funktion, die selbst eine Schleife enthält:

```python
def verdoppeln(zahlen):
    for z in zahlen:
        print(z * 2)

verdoppeln([1, 2, 3])  # gibt 2, 4, 6 aus
```

Die Funktion `verdoppeln` bekommt eine ganze Liste als Parameter übergeben und geht sie dann selbst mit einer Schleife durch – genau so bauen richtige Programmierer:innen ihre Werkzeuge: kleine Bausteine, die man beliebig kombinieren kann.

Du bist bereit für den großen Kurs! Im 12-Wochen-Grundkurs baust du auf genau diesem Wissen auf und lernst, ganze Spiele und Geschichten selbst zu programmieren. 🚀
