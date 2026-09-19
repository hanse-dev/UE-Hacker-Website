# ⚖️ Zauberformel 4: Logische Verknüpfungen (`and`, `or`, `not`)

Oft reicht *eine* Bedingung nicht. Mit **logischen Operatoren** kombinierst du mehrere:

| Operator | Bedeutung | Wahr, wenn ... |
|----------|-----------|----------------|
| `and` | und | **beide** Seiten wahr sind |
| `or` | oder | **mindestens eine** Seite wahr ist |
| `not` | nicht | die Bedingung **falsch** ist (kehrt um) |

```python
hat_schluessel = True
hat_fackel = True
if hat_schluessel and hat_fackel:
    print("Du kannst die dunkle Kammer sicher öffnen!")
```

```python
hat_schwert = False
hat_zauberstab = True
if hat_schwert or hat_zauberstab:
    print("Du bist bewaffnet und bereit!")
```

```python
ist_verflucht = False
if not ist_verflucht:
    print("Du bist frei von jedem Fluch!")
```

Du kannst sie auch mit Vergleichen mischen, zum Beispiel `if staerke > 10 and intelligenz > 10:`.
