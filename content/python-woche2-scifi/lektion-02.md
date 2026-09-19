# 🧬 Systemprotokoll 2: Strings und Integer

Jede Information auf der Nebula-7 hat einen **Quanten-Typ** – wie die Aggregatzustände der Materie. Heute die ersten zwei:

| Typ | Python-Name | Bedeutung | Beispiel |
|---|---|---|---|
| **String** | `str` | Text | `"Starlight"` |
| **Integer** | `int` | ganze Zahl | `250` |

## Den Typ herausfinden mit `type()`

`type()` ist ein **Systemprotokoll** (also eine **Funktion**, Aufruf mit Klammern!): Du gibst ihr einen Wert in die Klammern, und sie sagt dir dessen Typ.

```python
crew_anzahl = 250
print(type(crew_anzahl))
```

Ausgabe: `<class 'int'>` – also ein Integer. Bei Text steht dort `<class 'str'>`.

> 📡 **Merke:** `"250"` (mit Anführungszeichen) ist ein **String**, `250` (ohne) ist ein **Integer**. Sieht ähnlich aus, verhält sich aber ganz anders!
