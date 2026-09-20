# 🚀 Systemprotokoll 1: Ein Protokoll definieren

Willkommen im **Hauptquartier der Wiederverwendbarkeit** an Bord der Raumstation Nebula-7! Die Bordintelligenz meldet: *"Ein Systemprotokoll wird einmal geschrieben – und läuft auf jeder Mission."*

Genau das macht eine **Funktion**: ein Stück Code mit einem Namen, das du immer wieder aufrufen kannst.

```python
def starte_scan():
    print("Scan gestartet...")
    print("Sektor wird geprüft!")

starte_scan()
starte_scan()
```

**Schritt für Schritt:**
1. **`def`** startet die Definition – hier legst du das Protokoll nur *fest*
2. **`starte_scan`** ist der Name des Protokolls
3. **`()`** und der **Doppelpunkt `:`** gehören immer dazu
4. Der **eingerückte** Code (4 Leerzeichen) ist das Protokoll selbst
5. **`starte_scan()`** – mit Klammern – *führt* es aus

> ⚠️ Beim Definieren passiert noch nichts! Erst der **Aufruf mit Klammern** führt den Code aus. Ohne Klammern (`starte_scan`) startet nichts.

Jeder Aufruf führt den Code erneut aus – so sparst du dir Copy & Paste.
