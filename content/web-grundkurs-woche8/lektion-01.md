# Grid-Raster

Flexbox ordnet in **einer** Richtung an. **Grid** ordnet in **zwei** Richtungen gleichzeitig – in Zeilen **und** Spalten, wie ein Raster:

```css
.raster {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 12px;
}
```

- `display: grid` macht das Element zum **Grid-Container**.
- `grid-template-columns` legt die **Spalten** fest – hier drei.
- Die Kinder füllen das Raster automatisch Zeile für Zeile: Item 4 rutscht in die zweite Zeile.

## Die Einheit fr

`fr` (*fraction*, Anteil) verteilt den freien Platz: `1fr 1fr 1fr` sind drei gleich breite Spalten, `2fr 1fr` macht die erste Spalte doppelt so breit wie die zweite. Feste Breiten gehen auch: `200px 1fr` – links 200px, rechts der Rest.
