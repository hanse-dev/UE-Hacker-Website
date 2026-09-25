# 🔍 Lernen statt Regeln schreiben

Statt für jeden Fall eine eigene Regel zu schreiben, probieren wir jetzt etwas anderes: Wir geben
dem Computer einfach **Beispiele** – und er schlägt darin nach.

```python
beispiele = [
    ("katze", "Säugetier"),
    ("spinne", "Spinnentier"),
    ("biene", "Insekt"),
]

def finde_antwort(frage, beispiele):
    for eingabe, antwort in beispiele:
        if eingabe == frage:
            return antwort
    return "unbekannt"

print(finde_antwort("katze", beispiele))
print(finde_antwort("hai", beispiele))
```

Kein `if beine == 4` mehr – stattdessen eine **Liste von Beispielen**, durch die der Code einfach
durchgeht. Das ist noch keine "richtige" KI (der Computer kann nur exakt bekannte Beispiele
wiederfinden, nichts Neues erschließen), aber es ist der erste Schritt weg vom Regeln-Schreiben
hin zum **Beispiele-Sammeln**. Ab Woche 3 baust du daraus einen Algorithmus, der auch bei
**unbekannten** Eingaben eine sinnvolle Vermutung abgeben kann.
