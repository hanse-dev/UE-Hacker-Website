# Hindernisse: nicht jede Form willst du fangen

Nicht alles, was fällt, ist gut für dich. Jetzt kommt ein zweites fallendes Objekt dazu – ein
**Hindernis** (ein rotes Quadrat). Fängt dein Schläger es, kostet das ein Leben statt einen Punkt
zu geben.

Das Gute: die Kollisionserkennung hast du schon – `istTreffer(x, y, schlaegerX)` prüft nur, ob
eine Position bei `schlaegerX` landet. Das funktioniert für jedes fallende Objekt, nicht nur für
den Ball. Du rufst dieselbe Funktion einfach noch einmal mit der Position des Hindernisses auf:

```js
if (istTreffer(hindernisX, hindernisY, schlaegerX)) {
  leben = leben - 1;        // Autsch - ein Leben weg
  hindernisY = 20;
} else if (hindernisY > 300) {
  hindernisY = 20;          // durchgerutscht, kein Problem - startet neu oben
} else {
  hindernisY = hindernisY + 2;
}
```

Fällt dir das Muster auf? Es ist genau dieselbe Struktur wie beim Ball – nur mit umgekehrter
Konsequenz beim Treffer. Zuerst zeichnest du das Hindernis mit einer eigenen Funktion
`zeichneHindernis(ctx, x, y)`, danach baust du es ins Spiel ein.
