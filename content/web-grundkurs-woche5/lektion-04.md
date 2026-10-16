# Farben, Schrift und Variablen

## Farben angeben

| Schreibweise | Beispiel | |
|---|---|---|
| Name | `tomato` | über 140 Namen |
| Hex | `#ff6347` | Rot-, Grün-, Blauanteil von `00` bis `ff` |
| rgb() | `rgb(255, 99, 71)` | dieselben Anteile von 0 bis 255 |

Alle drei Zeilen meinen dieselbe Farbe.

## Schrift gestalten

```css
body {
  font-family: Verdana, sans-serif;   /* Wunschschrift, dann Ersatz */
  font-size: 18px;
  line-height: 1.5;                   /* Zeilenabstand */
}
h1 {
  text-align: center;
}
```

## Variablen

Kommt eine Farbe an vielen Stellen vor, legst du sie **einmal** als Variable an:

```css
:root {
  --hauptfarbe: #2a9d8f;
}
h1 { color: var(--hauptfarbe); }
.knopf { background-color: var(--hauptfarbe); }
```

Variablen beginnen mit `--`, gelesen werden sie mit `var(…)`. Willst du später eine andere Farbe, änderst du nur eine Zeile.
