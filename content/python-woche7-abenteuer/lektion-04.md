# 🔤 Archiv-Zauber 4: Das string-Modul

Das Modul **`string`** liefert fertige **Zeichensammlungen**:

```python
import string

print(string.ascii_letters)   # alle Buchstaben a–z und A–Z (52)
print(string.ascii_uppercase) # nur Großbuchstaben
print(string.digits)          # 0123456789
```

Zusammen mit `random.choice()` schmiedest du daraus einen **Schlüssel** (Passwort):

```python
import random, string

alphabet = string.ascii_letters + string.digits          # 62 Zeichen
schluessel = "".join([random.choice(alphabet) for _ in range(8)])
```

- **`"".join(liste)`** klebt die Einträge einer Liste zu **einem Text** zusammen (zwischen die Anführungszeichen kommt das, was zwischen den Teilen stehen soll – hier nichts)
- Die List Comprehension `[... for _ in range(8)]` wiederholt `random.choice` **8-mal**
