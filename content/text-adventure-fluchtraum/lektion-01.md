# Ein Raum als Dictionary

Ein Text-Adventure lebt von seinen Räumen – und jeder Raum braucht zwei Dinge: eine **Beschreibung**, die der Spielerin/dem Spieler angezeigt wird, und eine Liste der **Ausgänge**, durch die man den Raum verlassen kann. Ein Dictionary ist dafür genau richtig, weil es beides unter benannten Schlüsseln zusammenhält:

```python
raum = {
    "beschreibung": "Ein kalter, steinerner Gang.",
    "ausgaenge": {"norden": "halle"}
}

print(raum["beschreibung"])
print(raum["ausgaenge"]["norden"])
```

`raum["ausgaenge"]` ist dabei selbst wieder ein Dictionary: Die Schlüssel sind die Himmelsrichtungen ("norden", "westen", …), die Werte sind die Namen der Räume, in die man von dort aus kommt. Ein **verschachteltes Dictionary** – ein Dictionary in einem Dictionary.

> 💡 Genau wie bei deinem Vigenère-Projekt: Erst baust du eine einzelne Grundzutat sauber, bevor du im nächsten Schritt mehrere davon verbindest.
