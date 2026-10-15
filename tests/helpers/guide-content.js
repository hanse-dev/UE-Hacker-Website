import { expect } from '@playwright/test';
import fs from 'node:fs';
import path from 'node:path';

const GUIDE_VIEW = fs.readFileSync(path.join('src', 'components', 'GuideLessonView.vue'), 'utf8');

/**
 * Prüft die Regeln für Anleitungs-Kurse (`engine: "anleitung"`, INHALTE.md §6) für alle Lektionen
 * eines Content-Ordners: Pflichtaufgaben, Bonus-Abschnitte, Blöcke/Python paarweise, Code nur in
 * den Abschnitten, jede Block-Kategorie hat eine Farbe und jedes Bild unter /microbit/ existiert.
 */
export function expectGuideContent(contentDir) {
  const lessons = JSON.parse(fs.readFileSync(path.join(contentDir, 'lessons.json'), 'utf8'));
  for (const lesson of lessons) {
    expect(lesson.tasks.some((task) => !task.isBonus), lesson.id).toBe(true);
    const md = fs.readFileSync(path.join(contentDir, lesson.file), 'utf8');
    // Jede Bonusaufgabe braucht im Text eine eigene Aufgabenstellung.
    if (lesson.tasks.some((task) => task.isBonus)) {
      expect(md, `${lesson.file}: Bonus-Abschnitt`).toMatch(/^## Bonus: /m);
    }
    const opened = md.match(/^:::(bloecke|python)$/gm) || [];
    const closed = md.match(/^:::$/gm) || [];
    expect(closed.length, `${lesson.file}: Abschnitte geschlossen`).toBe(opened.length);
    expect(opened.filter((m) => m === ':::bloecke').length, `${lesson.file}: Blöcke und Python gleich oft`)
      .toBe(opened.filter((m) => m === ':::python').length);
    // Ein Block-Listing ausserhalb eines :::bloecke-Abschnitts waere auch in der Python-Ansicht sichtbar.
    const outside = md.replace(/^:::(bloecke|python)$[\s\S]*?^:::$/gm, '');
    expect(outside, `${lesson.file}: Code nur innerhalb der Abschnitte`).not.toMatch(/```(bloecke|python)/);

    // Eine Kategorie ohne .mc-<name>-Farbe wäre ein farbloser Block.
    for (const [, category] of md.matchAll(/^\s*\[([a-z]+)\] /gm)) {
      expect(GUIDE_VIEW, `${lesson.file}: Farbe für [${category}]`).toContain(`.mc-${category})`);
    }
    for (const [, src] of md.matchAll(/<img src="\/(microbit\/[^"]+)"/g)) {
      expect(fs.existsSync(path.join('public', src)), `${lesson.file}: Bild ${src}`).toBe(true);
    }
  }
  return lessons;
}
