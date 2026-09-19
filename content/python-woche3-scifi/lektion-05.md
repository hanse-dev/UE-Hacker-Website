# 📟 Systemprotokoll 5: Logische Verknüpfungen

Mit **`and`**, **`or`** und **`not`** kombinierst du mehrere Bedingungen:

| Operator | Bedeutung | Wahr, wenn … |
|---|---|---|
| `and` | und | **beide** Bedingungen wahr sind |
| `or` | oder | **mindestens eine** Bedingung wahr ist |
| `not` | nicht | die Bedingung **falsch** ist (kehrt um) |

```python
hat_zugangscode = True
hat_fingerabdruck = True
if hat_zugangscode and hat_fingerabdruck:
    print("Zugang zum Kommandodeck gewährt!")
```

```python
hat_notfallschluessel = False
hat_ueberbrueckungscode = True
if hat_notfallschluessel or hat_ueberbrueckungscode:
    print("Du kannst die Tür manuell öffnen!")
```

```python
alarm_aktiv = False
if not alarm_aktiv:
    print("Keine Gefahr – alle Systeme sicher!")
```

Du kannst auch Vergleiche verknüpfen, zum Beispiel `if schild > 10 and waffen > 10:`.

> 📡 **Merke:** `and` ist streng (alles muss stimmen), `or` ist großzügig (eins reicht), `not` dreht um.
