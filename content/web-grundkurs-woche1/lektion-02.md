# Das Grundgerüst

Bisher hast du nur Inhalt geschrieben. Eine vollständige HTML-Seite hat aber immer dasselbe **Gerüst**:

```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <title>Skateboarden</title>
</head>
<body>
  <h1>Skateboarden</h1>
</body>
</html>
```

| Teil | Bedeutung |
|---|---|
| `<!DOCTYPE html>` | sagt dem Browser: Das ist modernes HTML |
| `<html lang="de">` | umschließt alles; `lang` nennt die Sprache (wichtig z. B. für Vorleseprogramme und Silbentrennung) |
| `<head>` | Infos **über** die Seite – erscheinen nicht im Fenster |
| `<meta charset="utf-8">` | Zeichensatz, damit ä, ö, ü und Emojis richtig angezeigt werden |
| `<title>` | Text im Browser-Tab und in Suchergebnissen |
| `<body>` | alles, was man auf der Seite **sieht** |

> 💡 Browser sind gnädig: Fehlt das Gerüst, ergänzen sie es selbst. Verlassen solltest du dich darauf nicht – Suchmaschinen, Vorleseprogramme und andere Browser verhalten sich sonst womöglich anders.
