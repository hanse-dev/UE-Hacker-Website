# 🐴 Übung 1: Dateien schreiben und lesen

Willkommen im **Stallbüro des Reiterhofs**! Hier stehen Stallbuch und Aktenschrank, damit nichts verloren geht. Die Stallmeisterin sagt: *"Was nur im Kopf des Computers steht, ist weg, sobald er ausgeht. Was im Stallbuch steht, bleibt für immer."*

Mit **`open()`** öffnest du eine Datei. Der **Modus** sagt, was du vorhast: `"w"` = schreiben (überschreibt!), `"r"` = lesen.

```python
with open("stallbuch.txt", "w") as f:      # Datei zum Schreiben öffnen
    f.write("Stallbuch Reiterhof\n")           # \n = neue Zeile

with open("stallbuch.txt", "r") as f:      # Datei zum Lesen öffnen
    inhalt = f.read()               # ganzen Inhalt als Text
print(inhalt)
```

**Schritt für Schritt:**
1. **`with open(name, modus) as f:`** öffnet die Datei und schließt sie am Ende des Blocks **automatisch**
2. **`f.write(text)`** schreibt Text – einen Zeilenumbruch musst du selbst mit `\n` anhängen
3. **`f.read()`** liefert den ganzen Inhalt als einen Text

> ⚠️ Im Modus `"w"` kannst du nur schreiben, im Modus `"r"` nur lesen – und `"w"` **löscht** den alten Inhalt.
