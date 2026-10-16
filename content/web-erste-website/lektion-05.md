# Kisten überall

Für den Browser ist jedes Element eine **Kiste** – eine Überschrift, ein Absatz, ein Bild. Und Kisten kann man gestalten: mit Rahmen, Abstand und runden Ecken.

## Rahmen

```css
h1 {
  border: 3px solid purple;
}
```

`border` braucht drei Angaben: wie **dick** (`3px`), welche **Art** (`solid` = durchgezogen, `dashed` = gestrichelt, `dotted` = gepunktet) und welche **Farbe**.

`px` steht für **Pixel**, die winzigen Leuchtpunkte deines Bildschirms. `3px` ist also ein dünner Rahmen, `10px` ein dicker.

## Abstand innen und außen

- `padding` ist der Abstand **innen**: zwischen Text und Rahmen. Ohne `padding` klebt der Text am Rahmen.
- `margin` ist der Abstand **außen**: zwischen der Kiste und ihren Nachbarn.

```css
p {
  border: 2px dashed teal;
  padding: 12px;
  margin: 20px;
}
```

## Runde Ecken

```css
h1 {
  border-radius: 12px;
}
```

Je größer die Zahl, desto runder. Mit einem Hintergrund und `border-radius` wird aus einer Überschrift schnell ein hübsches Schild.

> 💡 Probier verschiedene Werte aus und klick immer wieder auf **Ausführen** – so siehst du am schnellsten, was jede Zahl bewirkt.
