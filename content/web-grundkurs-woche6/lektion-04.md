# Positionierung

Normalerweise stehen Boxen einfach untereinander – das ist der **normale Fluss**. Mit `position` kannst du einzelne Elemente daraus lösen:

| Wert | Wirkung |
|---|---|
| `static` | Standard: normaler Fluss |
| `relative` | bleibt im Fluss, lässt sich aber mit `top`/`left` verschieben – und wird **Bezugspunkt** für absolute Kinder |
| `absolute` | wird aus dem Fluss genommen und mit `top`, `right`, `bottom`, `left` am nächsten positionierten Vorfahren ausgerichtet |

Das klassische Beispiel: ein **Abzeichen** in der Ecke einer Karte.

```css
.karte {
  position: relative;
}
.abzeichen {
  position: absolute;
  top: 0;
  right: 0;
}
```

Ohne `position: relative` an der Karte richtet sich das Abzeichen an der **ganzen Seite** aus und landet in deren Ecke.
