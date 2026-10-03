#!/usr/bin/env node
// Wählt anhand geänderter Dateien nur die relevanten Playwright-Specs aus
// tests:checks aus, statt immer die volle Suite zu laufen.
//
// Sicherheitsnetz: jede Datei, die zu keiner Regel passt, oder eine Regel,
// die als "core" markiert ist, löst den vollen test:checks-Lauf aus statt
// eine Vermutung zu riskieren.
//
// Nutzung:
//   node scripts/test-changed.mjs            # Arbeitsverzeichnis + Branch-Diff zu main
//   node scripts/test-changed.mjs --staged    # nur staged Dateien (Pre-commit-Hook)
//   node scripts/test-changed.mjs --dry-run   # nur anzeigen, nicht ausführen

import { execFileSync, spawnSync } from 'node:child_process';

const ALL_CHECKS = [
  'tests/week-checks-logic.spec.js',
  'tests/week-checks.spec.js',
  'tests/site.spec.js',
  'tests/progress-merge.spec.js',
  'tests/storytelling-content.spec.js',
  'tests/zertifikate.spec.js',
  'tests/projekte.spec.js',
  'tests/js-spielewerkstatt.spec.js',
  'tests/js-grundkurs.spec.js',
  'tests/ki-labor.spec.js',
  'tests/python-woche1-lektionen.spec.js',
  'tests/python-lektionen-format.spec.js',
  'tests/woche12-abschlussprojekt.spec.js',
  'tests/lesson-bundle-generator.spec.js',
  'tests/lesson-notebook-generator.spec.js',
];

// Dateien/Präfixe, die zu breit wirken (viele Specs hängen daran), um sie
// spezifisch zu mappen -> lösen immer den vollen Lauf aus.
const CORE_PREFIXES = [
  'src/composables/useTaskValidation.js',
  'src/composables/devSkipChecks.js',
  'src/composables/useWeekChecks.js',
  'src/composables/useProgressSync.js',
  'src/composables/useAuth.js',
  'src/composables/useAuthApi.js',
  'src/composables/usePyodide.js',
  'src/composables/useLanguage.js',
  'src/App.vue',
  'src/router/',
  'src/locales/',
  'content/python-checks/',
  'playwright.config.js',
  'playwright.auth.config.js',
  'scripts/ensure-test-prereqs.mjs',
  'package.json',
  'scripts/build_cell_notebooks.py',
  'scripts/pack_notebooks.py',
];

// Präfix -> Liste betroffener Specs (aus ALL_CHECKS)
const RULES = [
  ['src/components/CodeChallenge.vue', ['tests/week-checks.spec.js', 'tests/week-checks-logic.spec.js', 'tests/zertifikate.spec.js', 'tests/ki-labor.spec.js']],
  ['src/components/WeekCheckPanel.vue', ['tests/week-checks.spec.js', 'tests/zertifikate.spec.js', 'tests/ki-labor.spec.js']],
  ['src/components/QuizStep.vue', ['tests/week-checks.spec.js', 'tests/week-checks-logic.spec.js', 'tests/zertifikate.spec.js']],
  ['src/components/JsLessonView.vue', ['tests/js-grundkurs.spec.js', 'tests/js-spielewerkstatt.spec.js', 'tests/projekte.spec.js']],
  ['src/components/JsCodeCell.vue', ['tests/js-grundkurs.spec.js', 'tests/js-spielewerkstatt.spec.js', 'tests/projekte.spec.js']],
  ['src/components/JsSandboxFrame.vue', ['tests/js-grundkurs.spec.js', 'tests/js-spielewerkstatt.spec.js', 'tests/projekte.spec.js']],
  ['src/composables/useJsSandbox.js', ['tests/js-grundkurs.spec.js', 'tests/js-spielewerkstatt.spec.js', 'tests/projekte.spec.js']],
  ['src/components/JsGrundkursTour.vue', ['tests/js-grundkurs.spec.js']],
  ['src/components/JsCourseTour.vue', ['tests/js-grundkurs.spec.js', 'tests/js-spielewerkstatt.spec.js']],
  ['src/components/KiLaborTour.vue', ['tests/ki-labor.spec.js']],
  ['src/components/LessonView.vue', ['tests/python-woche1-lektionen.spec.js', 'tests/python-lektionen-format.spec.js', 'tests/woche12-abschlussprojekt.spec.js']],
  ['src/components/CodeCell.vue', ['tests/python-woche1-lektionen.spec.js', 'tests/python-lektionen-format.spec.js', 'tests/woche12-abschlussprojekt.spec.js', 'tests/site.spec.js']],
  ['src/components/JupyterNotebook.vue', ['tests/storytelling-content.spec.js', 'tests/site.spec.js']],
  ['src/components/ProjectCourse.vue', ['tests/projekte.spec.js']],
  ['src/components/InteractiveCourse.vue', ['tests/site.spec.js']],
  ['src/assets/styles/course-layout.css', ['tests/projekte.spec.js', 'tests/site.spec.js', 'tests/js-spielewerkstatt.spec.js']],
  ['src/components/ProjectCompletionBox.vue', ['tests/projekte.spec.js']],
  ['src/composables/useCourseCertificates.js', ['tests/zertifikate.spec.js']],
  ['src/composables/useCertificatePdf.js', ['tests/zertifikate.spec.js']],
  ['src/composables/useZertifikate.js', ['tests/zertifikate.spec.js', 'tests/week-checks.spec.js']],
  ['src/composables/useCourseData.js', ['tests/site.spec.js', 'tests/projekte.spec.js']],
  ['src/composables/useLessonContent.js', ['tests/python-woche1-lektionen.spec.js', 'tests/python-lektionen-format.spec.js', 'tests/js-grundkurs.spec.js', 'tests/js-spielewerkstatt.spec.js', 'tests/projekte.spec.js']],
  ['src/composables/useProjectBadges.js', ['tests/projekte.spec.js']],
  ['src/composables/useFortschritt.js', ['tests/zertifikate.spec.js']],
  ['src/composables/useInteractiveProgress.js', ['tests/site.spec.js']],
  ['src/composables/useSavedCode.js', ['tests/python-woche1-lektionen.spec.js', 'tests/js-grundkurs.spec.js']],
  ['src/composables/useWeeklyContent.js', ['tests/storytelling-content.spec.js']],
  ['src/composables/useNotebookHeadings.js', ['tests/storytelling-content.spec.js']],
  ['src/views/CourseDetail.vue', ['tests/projekte.spec.js', 'tests/site.spec.js']],
  ['src/views/Home.vue', ['tests/site.spec.js']],
  ['src/views/AdminView.vue', ['tests/site.spec.js']],
  ['src/composables/useAdminApi.js', ['tests/site.spec.js']],
  ['api/src/routes/termine.js', ['tests/site.spec.js']],
  ['api/src/routes/adminTermine.js', ['tests/site.spec.js']],
  ['api/src/scripts/import-termine-json.js', ['tests/site.spec.js']],
  ['src/views/ProjekteView.vue', ['tests/projekte.spec.js']],
  ['src/views/ProfilView.vue', ['tests/zertifikate.spec.js']],
  ['scripts/build_lesson_bundle.py', ['tests/lesson-bundle-generator.spec.js']],
  ['scripts/build_lesson_notebook.py', ['tests/lesson-notebook-generator.spec.js']],
  ['scripts/build_project_notebook.py', ['tests/lesson-notebook-generator.spec.js', 'tests/projekte.spec.js']],
  ['scripts/build_kilabor_notebook.py', ['tests/lesson-notebook-generator.spec.js', 'tests/ki-labor.spec.js']],
  ['scripts/build_offline_py.py', ['tests/lesson-notebook-generator.spec.js']],
  ['scripts/check_kilabor_solutions.py', ['tests/lesson-notebook-generator.spec.js']],
  ['scripts/notebook_utils.py', ['tests/lesson-notebook-generator.spec.js']],
  ['src/components/OfflineDownloads.vue', ['tests/python-woche1-lektionen.spec.js', 'tests/ki-labor.spec.js', 'tests/projekte.spec.js']],
  ['src/components/WeekTourSideMenu.vue', ['tests/python-woche1-lektionen.spec.js']],
  ['content/python-woche1-', ['tests/python-woche1-lektionen.spec.js', 'tests/python-lektionen-format.spec.js']],
  ['content/python-woche12-', ['tests/woche12-abschlussprojekt.spec.js', 'tests/python-lektionen-format.spec.js']],
  ['content/python-woche', ['tests/python-lektionen-format.spec.js']],
  ['content/python-12-wochen-grundkurs', ['tests/storytelling-content.spec.js']],
  ['content/js-grundkurs', ['tests/js-grundkurs.spec.js']],
  ['content/js-spielewerkstatt', ['tests/js-spielewerkstatt.spec.js', 'tests/projekte.spec.js']],
  ['content/js-snake', ['tests/js-spielewerkstatt.spec.js', 'tests/projekte.spec.js']],
  ['content/ki-labor', ['tests/ki-labor.spec.js', 'tests/lesson-notebook-generator.spec.js']],
  ['content/caesar-chiffre', ['tests/projekte.spec.js']],
  ['content/vigenere-chiffre', ['tests/projekte.spec.js']],
  ['content/morsecode', ['tests/projekte.spec.js']],
  ['content/zahlendetektiv', ['tests/projekte.spec.js']],
  ['content/text-adventure-fluchtraum', ['tests/projekte.spec.js']],
  ['public/kurse.json', ['tests/projekte.spec.js', 'tests/site.spec.js']],
  ['public/rewards-manifest', ['tests/site.spec.js']],
  ['content/python-grundlagen-interaktiv', ['tests/site.spec.js']],
  ['content/python-einstufung', ['tests/site.spec.js', 'tests/week-checks.spec.js']],
  ['content/ferienkurse', ['tests/site.spec.js']],
  ['public/teaser.html', ['tests/site.spec.js']],
  ['src/views/Teaser.vue', ['tests/site.spec.js']],
  // Leere Liste = bewusst kein Spec aus test:checks: diese Dateien deckt die Suite gar nicht ab
  // (API hat eigene Tests: `npm --prefix api test` / `npm run test:auth`; der Rest ist lokales
  // Tooling). Ohne Regel würde hier bei jedem Commit sinnlos die volle Suite laufen. Muss nach den
  // spezifischeren api/-Regeln oben stehen (erste passende Regel gewinnt).
  ['api/', []],
  ['scripts/local-tools/', []],
  ['scripts/new-worktree.mjs', []],
  ['scripts/remove-worktree.mjs', []],
  ['scripts/test-changed.mjs', []],
];

function run(cmd, args) {
  return execFileSync(cmd, args, { encoding: 'utf8' }).trim();
}

function gitFiles(args) {
  try {
    const out = run('git', args);
    return out ? out.split('\n').filter(Boolean) : [];
  } catch {
    return [];
  }
}

function collectChangedFiles(staged) {
  if (staged) {
    return new Set(gitFiles(['diff', '--cached', '--name-only', '--diff-filter=ACMR']));
  }
  const files = new Set();
  for (const f of gitFiles(['diff', '--name-only'])) files.add(f);
  for (const f of gitFiles(['diff', '--cached', '--name-only'])) files.add(f);
  for (const f of gitFiles(['ls-files', '--others', '--exclude-standard'])) files.add(f);
  let mergeBase = null;
  try {
    mergeBase = run('git', ['merge-base', 'main', 'HEAD']);
  } catch {
    // kein main-Branch erreichbar (z.B. flacher Clone) -> ignorieren
  }
  if (mergeBase) {
    for (const f of gitFiles(['diff', '--name-only', mergeBase, 'HEAD'])) files.add(f);
  }
  return files;
}

function matchSpecs(changedFiles) {
  const specs = new Set();
  const unmatched = [];
  let coreHit = null;

  for (const file of changedFiles) {
    // Direkt geänderte Testdatei -> immer mitlaufen lassen.
    if (file.startsWith('tests/') && ALL_CHECKS.includes(file)) {
      specs.add(file);
      continue;
    }
    if (CORE_PREFIXES.some((p) => file.startsWith(p))) {
      coreHit = file;
      continue;
    }
    const rule = RULES.find(([prefix]) => file.startsWith(prefix));
    if (rule) {
      rule[1].forEach((s) => specs.add(s));
    } else if (file.startsWith('src/') || file.startsWith('content/') || file.startsWith('public/') || file.startsWith('scripts/') || file.startsWith('api/')) {
      unmatched.push(file);
    }
    // Sonstiges (Doku, .md, CLAUDE.md etc.) einfach ignorieren.
  }

  return { specs, unmatched, coreHit };
}

function main() {
  const args = process.argv.slice(2);
  const staged = args.includes('--staged');
  const dryRun = args.includes('--dry-run');

  const changedFiles = collectChangedFiles(staged);

  if (changedFiles.size === 0) {
    console.log('ℹ️  Keine geänderten Dateien gefunden — nichts zu testen.');
    return 0;
  }

  const { specs, unmatched, coreHit } = matchSpecs(changedFiles);

  if (coreHit || unmatched.length > 0) {
    if (coreHit) {
      console.log(`▶  "${coreHit}" ist eine Kern-Datei ohne spezifisches Mapping — volle Suite (test:checks) läuft.`);
    } else {
      console.log(`▶  Keine Mapping-Regel für: ${unmatched.join(', ')} — volle Suite (test:checks) läuft (Sicherheitsnetz).`);
    }
    if (dryRun) return 0;
    const res = spawnSync('npm', ['run', 'test:checks'], { stdio: 'inherit' });
    return res.status ?? 1;
  }

  if (specs.size === 0) {
    console.log('ℹ️  Geänderte Dateien betreffen keine getesteten Bereiche (z.B. nur Doku) — Tests übersprungen.');
    return 0;
  }

  const specList = [...specs];
  console.log(`▶  Geänderte Dateien: ${[...changedFiles].join(', ')}`);
  console.log(`▶  Laufe ${specList.length}/${ALL_CHECKS.length} Specs: ${specList.join(', ')}`);

  if (dryRun) return 0;

  const res = spawnSync('npx', ['playwright', 'test', ...specList], { stdio: 'inherit' });
  return res.status ?? 1;
}

if (import.meta.url === `file://${process.argv[1]}`) {
  process.exit(main());
}

export { matchSpecs, collectChangedFiles, ALL_CHECKS };
