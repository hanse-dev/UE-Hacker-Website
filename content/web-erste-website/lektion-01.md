# Hallo Website

Willkommen! In diesem Kurs baust du deine eigene Website. Jede Website, die du kennst – ob YouTube, Wikipedia oder die Seite deiner Schule –, ist aus derselben Sprache gebaut: **HTML**.

HTML ist keine Programmiersprache mit Rechnen und Schleifen. Es ist eher wie ein **Bauplan**: Du sagst dem Browser, was auf der Seite steht und was eine Überschrift oder ein Absatz ist.

## Tags: Schilder für den Browser

Dafür gibt es **Tags**. Ein Tag steht in spitzen Klammern und kommt fast immer im Doppelpack:

```html
<h1>Meine Katze Mia</h1>
```

- `<h1>` ist das **Anfangs-Tag**: Hier beginnt eine große Überschrift.
- `</h1>` ist das **End-Tag** – erkennbar am Schrägstrich `/`. Hier hört die Überschrift auf.
- Dazwischen steht der Text, den man auf der Seite sieht.

Für normalen Text gibt es den **Absatz** `<p>` (vom englischen *paragraph*):

```html
<p>Mia ist drei Jahre alt und schläft am liebsten in der Sonne.</p>
```

## Das Gerüst

Jede Seite hat ein festes Gerüst. Das ist in den Aufgaben schon fertig – du schreibst nur zwischen `<body>` und `</body>`, denn dort steht alles, was man auf der Seite **sieht**.

```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <title>Meine erste Website</title>
</head>
<body>
  <!-- Hier kommt deine Seite hin -->
</body>
</html>
```

> 💡 Alles zwischen `<!--` und `-->` ist ein **Kommentar**: eine Notiz für dich, die der Browser nicht anzeigt.

Wenn du auf **Ausführen** klickst, erscheint deine Seite in der **Vorschau**. Probier es gleich aus!
