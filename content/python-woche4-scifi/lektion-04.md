# 📟 Systemprotokoll 4: Die Buchstaben eines Codes

Eine for-Schleife kann auch einen **String** durchlaufen – Buchstabe für Buchstabe:

```python
code = "ALPHA"
for buchstabe in code:
    print(f"  - {buchstabe}")
```

Der String wird als Folge von Buchstaben behandelt. Bei jedem Durchlauf enthält `buchstabe` den nächsten Buchstaben.

Du kannst beim Durchlaufen auch **zählen**: Lege vor der Schleife eine Variable an und erhöhe sie in der Schleife:

```python
anzahl = 0
for buchstabe in "NEXUS":
    anzahl += 1
print(anzahl)   # 5
```
