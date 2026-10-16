# Ausrichten

Zwei Eigenschaften am Container richten die Items aus:

**`justify-content`** – entlang der **Hauptachse** (bei `row`: waagerecht)

| Wert | Wirkung |
|---|---|
| `flex-start` | alles an den Anfang (Standard) |
| `center` | alles in die Mitte |
| `space-between` | erstes Item ganz links, letztes ganz rechts, Rest gleichmäßig |
| `space-around` | gleicher Abstand um jedes Item |

**`align-items`** – entlang der **Querachse** (bei `row`: senkrecht)

| Wert | Wirkung |
|---|---|
| `stretch` | Items werden so hoch wie der Container (Standard) |
| `center` | senkrecht mittig |
| `flex-start` / `flex-end` | oben / unten |

Die klassische Kopfzeile: Logo links, Menü rechts, beides senkrecht mittig:

```css
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
```
