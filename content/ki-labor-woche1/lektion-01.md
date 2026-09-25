# 🤖 Regeln, die du selbst schreibst

Bevor wir über "künstliche Intelligenz" reden, schauen wir uns an, was **klassisches
Programmieren** ist – denn das ist der Gegenpol dazu.

Bei klassischem Programmieren schreibst **du** als Mensch jede einzelne Regel auf. Der Computer
führt sie stur aus, ohne selbst irgendetwas zu "lernen":

```python
def einschaetzung(temperatur):
    if temperatur > 25:
        return "Es ist heiß!"
    else:
        return "Es ist nicht heiß."

print(einschaetzung(30))
print(einschaetzung(15))
```

Du hast hier komplett selbst entschieden: *"Wenn die Temperatur über 25 liegt, ist es heiß."* Der
Computer prüft nur, ob deine Regel zutrifft.

Mit `elif` kannst du mehrere Regeln hintereinander prüfen:

```python
def wetter_gefuehl(temperatur):
    if temperatur > 25:
        return "heiß"
    elif temperatur < 5:
        return "kalt"
    else:
        return "mild"

print(wetter_gefuehl(30))
print(wetter_gefuehl(2))
print(wetter_gefuehl(15))
```

> 💡 Genau das macht den ganzen Kurs über einen Unterschied: Bei **Regeln** denkst du dir jeden
> Fall selbst aus. Ab Woche 3 lässt du den Computer die Regeln stattdessen **aus Beispielen**
> finden.
