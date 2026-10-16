# repeat und minmax

Bei vielen gleichen Spalten wird `1fr 1fr 1fr 1fr` schnell lang. Kürzer geht es mit `repeat`:

```css
grid-template-columns: repeat(4, 1fr);   /* vier gleiche Spalten */
```

## Raster, das sich selbst anpasst

Noch besser: Du sagst nicht, **wie viele** Spalten es gibt, sondern wie **breit** eine mindestens sein soll. Der Browser rechnet aus, wie viele hineinpassen:

```css
.galerie {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
  gap: 10px;
}
```

- `minmax(120px, 1fr)` – jede Spalte ist mindestens 120px breit, höchstens ein gleicher Anteil.
- `auto-fill` – so viele Spalten, wie hineinpassen.

Auf dem Handy entstehen so zwei Spalten, auf dem Laptop fünf – ganz ohne extra Regeln.
