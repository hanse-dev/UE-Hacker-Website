# Wer gewinnt?

Oft treffen **mehrere Regeln** dasselbe Element. Welche gilt dann? Das regelt die **Kaskade** – das C in CSS.

## 1. Die genauere Regel gewinnt (Spezifität)

| Selektor | Gewicht |
|---|---|
| `p` (Element) | niedrig |
| `.rot` (Klasse) | mittel |
| `#hinweis` (id) | hoch |
| `style="…"` am Element | noch höher |

Ein Selektor aus mehreren Teilen zählt alle Teile zusammen: `#hinweis.rot` ist genauer als `#hinweis`.

## 2. Bei Gleichstand gewinnt die spätere Regel

```css
h2 { color: green; }
h2 { color: orange; }   /* gewinnt – steht weiter unten */
```

## 3. Manches wird vererbt

Farbe und Schrift **erben** Kinder von ihren Eltern: `body { color: navy; }` färbt allen Text. Rahmen und Abstände werden nicht vererbt.

> 💡 Wenn eine Regel „nicht wirkt“, gibt es fast immer eine genauere oder spätere Regel, die gewinnt.
