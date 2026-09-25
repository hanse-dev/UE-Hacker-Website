# Zahlenpalindrome

Ein Palindrom ist etwas, das vorwärts und rückwärts gelesen gleich aussieht – bei Wörtern z.B. "Anna" oder "Reittier". Das geht auch mit Zahlen: 121 ist ein **Zahlenpalindrom**, 123 nicht.

Der Trick: verwandle die Zahl in einen String, drehe den String um und vergleiche beide. So läuft das Prinzip ab:

```
text = str(zahl)
umgedreht = text rückwärts (Slice [::-1])
gib zurück: text gleich umgedreht?
```

`text[::-1]` ist ein bekannter Python-Trick, um einen String rückwärts zu lesen.

Vervollständige jetzt `ist_zahlenpalindrom`, damit sie diese Idee für eine beliebige Zahl umsetzt.
