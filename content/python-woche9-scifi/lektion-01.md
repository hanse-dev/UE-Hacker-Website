# 🚀 Daten-Log 1: Dateien schreiben und lesen

Willkommen im **Datenspeicher der Raumstation Nebula-7**! Die Bordintelligenz sagt: *"Was nur im Arbeitsspeicher steht, ist weg, sobald die Station herunterfährt. Was in einer Datei steht, bleibt für immer."*

Mit **`open()`** öffnest du eine Datei. Der **Modus** sagt, was du vorhast: `"w"` = schreiben (überschreibt!), `"r"` = lesen.

```python
with open("bordbuch.txt", "w") as f:      # Datei zum Schreiben öffnen
    f.write("Bordbuch Nebula-7\n")           # \n = neue Zeile

with open("bordbuch.txt", "r") as f:      # Datei zum Lesen öffnen
    inhalt = f.read()               # ganzen Inhalt als Text
print(inhalt)
```

**Schritt für Schritt:**
1. **`with open(name, modus) as f:`** öffnet die Datei und schließt sie am Ende des Blocks **automatisch**
2. **`f.write(text)`** schreibt Text – einen Zeilenumbruch musst du selbst mit `\n` anhängen
3. **`f.read()`** liefert den ganzen Inhalt als einen Text

> ⚠️ Im Modus `"w"` kannst du nur schreiben, im Modus `"r"` nur lesen – und `"w"` **löscht** den alten Inhalt.
