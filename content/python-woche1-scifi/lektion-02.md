# 💾 Systemprotokoll 2: Datenspeicher

Eine Variable ist wie ein **beschrifteter Datenspeicher**: Du gibst ihr einen Namen und kannst darin etwas aufbewahren – und später wieder abrufen.

```python
schiff_name = "Enterprise"   # der Speicher heißt 'schiff_name', drin liegt der Text "Enterprise"
besatzung = 150              # der Speicher heißt 'besatzung', drin liegt die Zahl 150
```

**Die zwei häufigsten Arten von Werten:**

| Art | Fachbegriff | Beispiel | Erkennungszeichen |
|-----|------------|---------|------------------|
| Text | **String** | `"Enterprise"` | Anführungszeichen |
| Ganze Zahl | **Integer** | `150` | keine Anführungszeichen |

Variablen können sich **ändern**: Schreibst du einen neuen Wert in den Speicher, ist der alte überschrieben.

```python
energie = 80
energie = 45    # nach dem Sprung
print(energie)
```
