# Auswahllisten und Textbereiche

## Auswahlliste

```html
<label for="kurs">Kurs</label>
<select id="kurs" name="kurs">
  <option value="">Bitte wählen</option>
  <option value="bouldern">Bouldern</option>
  <option value="seil">Seilklettern</option>
</select>
```

`select` ist ein Aufklappmenü, jedes `option` eine Wahl. Der Text zwischen den Tags ist sichtbar, `value` wird verschickt.

## Textbereich

Für längere Texte gibt es `textarea` – anders als `input` **mit** End-Tag:

```html
<label for="nachricht">Nachricht</label>
<textarea id="nachricht" name="nachricht" rows="4"></textarea>
```

`rows` legt fest, wie viele Zeilen sichtbar sind.

## Knöpfe

`<button type="submit">` schickt das Formular ab, `<button type="reset">` leert alle Felder.
