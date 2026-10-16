# Eingabetypen

Mit `type` wählst du, was in ein Feld gehört. Der Browser hilft dann mit: Auf dem Handy erscheint z. B. bei `email` gleich eine Tastatur mit @.

| type | Feld für | Extra |
|---|---|---|
| `text` | beliebigen Text | |
| `email` | eine E-Mail-Adresse | prüft auf @ |
| `number` | eine Zahl | `min`, `max`, `step` |
| `date` | ein Datum | Kalender zum Auswählen |
| `checkbox` | ein Häkchen (ja/nein) | `checked` = vorausgewählt |
| `radio` | **eine** Wahl aus mehreren | alle mit gleichem `name` |

## Radio-Buttons

Radio-Buttons gehören zusammen, wenn sie **denselben `name`** haben – dann kann man nur einen davon wählen:

```html
<input type="radio" id="s" name="groesse" value="S"> <label for="s">S</label>
<input type="radio" id="m" name="groesse" value="M"> <label for="m">M</label>
```

`value` ist der Wert, der für die gewählte Option verschickt wird.
