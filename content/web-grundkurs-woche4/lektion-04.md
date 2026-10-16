# Pflichtfelder und Gruppen

Gute Formulare helfen beim Ausfüllen:

| Attribut | Wirkung |
|---|---|
| `required` | Pflichtfeld – ohne Eingabe lässt sich das Formular nicht abschicken |
| `placeholder="z. B. Max"` | grauer Beispieltext im leeren Feld |
| `checked` | Checkbox oder Radio-Button ist vorausgewählt |

> 💡 Ein `placeholder` ersetzt **kein** `label`: Er verschwindet, sobald man tippt – dann weiß man nicht mehr, wofür das Feld war.

## Felder gruppieren

Lange Formulare teilst du mit `fieldset` in Gruppen. `legend` ist die Überschrift der Gruppe:

```html
<fieldset>
  <legend>Über dich</legend>
  <label for="vorname">Vorname</label>
  <input type="text" id="vorname" name="vorname" required>
</fieldset>
```
