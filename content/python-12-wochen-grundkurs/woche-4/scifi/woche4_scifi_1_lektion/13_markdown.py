"""## Systemprotokoll 3: Verschachtelte Schleifen – Der Zeit-in-Zeit-Zyklus

**Was es ist:** Eine Schleife kann eine weitere Schleife enthalten – man nennt das Verschachtelung. Die innere Schleife läuft bei jedem einzelnen Durchlauf der äußeren Schleife komplett durch.

```python
for aussen in range(3):
    for innen in range(2):
        # Dieser Code läuft 3 × 2 = 6 Mal
```

**Wichtig:** Jede zusätzliche Verschachtelungsebene braucht eine weitere Einrückung!"""
