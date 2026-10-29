// Sprungmarke aus einer Überschrift: "Knöpfe" → "knoepfe", "Und, oder" → "und-oder".
// `anker` in content/begriffe.json muss genau so aus der Überschrift im Spickzettel entstehen.
export function slugify(text) {
  return String(text)
    .toLowerCase()
    .replace(/ä/g, 'ae')
    .replace(/ö/g, 'oe')
    .replace(/ü/g, 'ue')
    .replace(/ß/g, 'ss')
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '');
}
