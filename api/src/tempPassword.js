import crypto from 'crypto';

// Gleiches Format wie scripts/local-tools/drucker.py: zwei kurze deutsche Wörter
// (ohne Umlaute/ß, leicht abzutippen) + zwei Ziffern, z.B. "Igel-Zug-79".
const WORDS = [
  'Apfel', 'Baum', 'Berg', 'Blume', 'Boot', 'Brot', 'Delfin', 'Drache', 'Ecke', 'Elefant',
  'Feuer', 'Fisch', 'Fuchs', 'Garten', 'Gitarre', 'Hafen', 'Hase', 'Held', 'Herbst', 'Himmel',
  'Honig', 'Hund', 'Hut', 'Igel', 'Insel', 'Katze', 'Keks', 'Kiwi', 'Koffer', 'Komet',
  'Kranich', 'Kuchen', 'Lampe', 'Mantel', 'Meer', 'Mond', 'Muschel', 'Nebel',
  'Nudel', 'Ozean', 'Panda', 'Pilz', 'Planet', 'Pirat', 'Rakete', 'Ritter', 'Roboter', 'Sand',
  'Schiff', 'Schnee', 'See', 'Sommer', 'Stern', 'Sturm', 'Tiger', 'Traum', 'Tunnel', 'Turm',
  'Vogel', 'Wald', 'Wal', 'Welle', 'Wiese', 'Wind', 'Winter', 'Wolke', 'Zauber', 'Ziege',
  'Zirkus', 'Zug',
];

export function generateTempPassword() {
  const first = crypto.randomInt(WORDS.length);
  let second = crypto.randomInt(WORDS.length - 1);
  if (second >= first) second += 1;
  const digits = String(crypto.randomInt(100)).padStart(2, '0');
  return `${WORDS[first]}-${WORDS[second]}-${digits}`;
}
