# Formular und Textfeld

Formulare kennst du von jeder Anmeldung: Namen eintippen, Häkchen setzen, abschicken. In HTML steckt ein Formular in `form`:

```html
<form>
  <label for="vorname">Vorname</label>
  <input type="text" id="vorname" name="vorname">
  <button type="submit">Anmelden</button>
</form>
```

- `input` ist ein Eingabefeld – ein leeres Element ohne End-Tag. `type="text"` macht ein einzeiliges Textfeld.
- `name` ist der Name, unter dem der Wert später verschickt wird.
- `label` ist die **Beschriftung**. Mit `for` zeigt es auf die `id` des Feldes. Dann gilt: Klick auf die Beschriftung → das Feld wird aktiv. Und Vorleseprogramme wissen, was in das Feld gehört.

> 💡 In der Vorschau wird ein Formular nie wirklich abgeschickt – es gibt ja keinen Server, der die Daten empfängt. Das Formular selbst baust du aber genau wie auf einer echten Seite.
