# 📟 Systemprotokoll 5: Die while-Schleife – der Dauer-Scanner

Eine **while-Schleife** wiederholt Code, **solange eine Bedingung wahr ist**:

```python
scan = 0
while scan <= 10:
    print(f"Scan {scan}: Daten empfangen")
    scan += 1
```

1. `scan` startet bei 0
2. Solange `scan <= 10` gilt, läuft der eingerückte Code
3. `scan += 1` erhöht den Wert bei jedem Durchlauf
4. Bei `scan = 11` ist die Bedingung falsch und die Schleife endet

> ⚠️ **Vorsicht – Endlosschleife!** Wird die Bedingung nie falsch (zum Beispiel weil du `scan += 1` vergessen hast), endet die Schleife nie. Achte immer darauf, dass sich in der Schleife etwas ändert, das die Bedingung beeinflusst.
