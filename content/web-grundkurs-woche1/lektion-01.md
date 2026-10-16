# Was ist HTML?

Jede Webseite, die du im Browser siehst, ist zunächst nur eine **Textdatei**. Der Browser liest sie und macht daraus das, was du siehst: Überschriften, Absätze, Bilder, Knöpfe. Die Sprache, in der diese Datei geschrieben ist, heißt **HTML** – *HyperText Markup Language*.

HTML ist eine **Auszeichnungssprache**: Du rechnest nicht und schreibst keine Schleifen, sondern **markierst**, welche Rolle ein Stück Text spielt.

## Elemente und Tags

```html
<h1>Mein Lieblingsspiel</h1>
<p>Minecraft spiele ich am liebsten mit Freunden.</p>
```

- `<h1>` ist ein **Anfangs-Tag**, `</h1>` das passende **End-Tag** (mit `/`).
- Anfangs-Tag, Inhalt und End-Tag zusammen bilden ein **Element**.
- `h1` bis `h6` sind Überschriften (1 = wichtigste), `p` ist ein Absatz (*paragraph*).

## Was der Browser daraus macht

Der Browser baut aus deinem Text einen **Baum** aus Elementen – das **DOM** (*Document Object Model*). Leerzeichen und Zeilenumbrüche im Code fasst er dabei zu einem einzigen Leerzeichen zusammen. Wie dein Code eingerückt ist, ändert also nichts an der Seite – es macht ihn nur für Menschen lesbarer.

> 💡 Rechts in der **Vorschau** siehst du nach jedem Klick auf **Ausführen**, was der Browser aus deinem Code macht.
