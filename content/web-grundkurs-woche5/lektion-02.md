# Selektoren

Der Selektor bestimmt, **welche** Elemente eine Regel trifft:

| Selektor | trifft | Beispiel |
|---|---|---|
| `p` | alle Elemente dieser Art | alle Absätze |
| `.hinweis` | alle Elemente mit `class="hinweis"` | Punkt vor dem Namen |
| `#start` | das eine Element mit `id="start"` | Raute vor dem Namen |
| `footer p` | Absätze, die **in** einem footer stecken | Nachfahren-Selektor (Leerzeichen) |
| `h1, h2` | alle h1 **und** alle h2 | Gruppe (Komma) |

```css
.hinweis {
  background-color: lightyellow;
}
footer p {
  font-size: 12px;
}
h1, h2 {
  font-family: Georgia, serif;
}
```

Klassen kannst du beliebig oft vergeben, eine id nur einmal. Für Design nimmt man deshalb meistens **Klassen**.
