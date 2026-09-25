import { reactive } from 'vue';
import fm from 'front-matter';
import { marked } from 'marked';

// ── Markdown parser: extract shortDesc + lernziele ──────────────────────────
function parseWeekMarkdown(body) {
  const lines = body.split('\n');
  let shortDesc = '';
  const lernziele = [];
  const lernzieleFull = [];
  const descLines = [];
  let inWelten = false;
  let inLernziele = false;

  for (const line of lines) {
    const trimmed = line.trim();

    // Detect section headings
    if (/^#{1,3}\s+/.test(trimmed)) {
      const headingText = trimmed.replace(/^#+\s+/, '').toLowerCase();
      inWelten    = /welten|auswahl|themenwelt/.test(headingText);
      inLernziele = headingText.includes('lernziel') || headingText.includes('learning goal');
      continue;
    }

    if (inWelten || !trimmed) continue;

    if (inLernziele && trimmed.startsWith('- ')) {
      const raw = trimmed.slice(2);
      lernzieleFull.push(raw.replace(/\*\*/g, '').replace(/`/g, '').trim());
      const boldMatch = raw.match(/^\*\*(.+?)\*\*/);
      let chip = boldMatch ? boldMatch[1] : raw.replace(/\*\*/g, '').split(':')[0];
      // Shorten at first German preposition for compact chips
      for (const sep of [' für ', ' mit ', ' zur ', ' und ', ' in ', ' an ']) {
        if (chip.includes(sep)) { chip = chip.split(sep)[0]; break; }
      }
      lernziele.push(chip.trim().slice(0, 36));
    } else if (!inLernziele) {
      // Collect as potential short description (ignore list items in Welten)
      if (!trimmed.startsWith('-') && !trimmed.startsWith('#')) {
        descLines.push(trimmed);
      }
    }
  }

  // Take first 1-2 sentences of description
  const sentences = descLines.join(' ').match(/[^.!?]+[.!?]*/g) || [];
  shortDesc = sentences.slice(0, 2).join(' ').trim();

  return { shortDesc, lernziele, lernzieleFull };
}

// Seit alle Wochen im Lektions-Format sind (siehe HANDOFF.md 3.47-3.54), gibt es nur noch diese
// zwei Notebook-Typen als eigenständige Zellen-Ordner - Lektion/Debug/Missionen/Boss kommen aus
// content/python-woche{N}-{thema}[-en]/lessons.json (useLessonContent.js), nicht mehr von hier.
const NOTEBOOK_TYPES = [
  '0_glossar',
  '6_loesungen',
];

function emptyWeek(weekNum, label = 'Woche') {
  return reactive({
    title: `${label} ${weekNum}`,
    shortDesc: '',
    lernziele: [],
    lernzieleFull: [],
    hasNotebook: false,
    hasAbenteuerVariant: false,
    hasPferdeVariant: false,
    hasScifiVariant: false,
    notebooks: { abenteuer: {}, pferde: {}, scifi: {} },
    downloads: [],
    cheatSheets: [],
    expandedCheatSheets: {},
    selectedVariant: null,
    selectedTab: '1_lektion',
    expanded: false,
  });
}

// Nur Titel + Lernziele pro Woche, ohne Notebooks/Downloads/Cheat-Sheets - für die
// Zertifikat-PDF im Profil (useCourseCertificates.js), wo die volle loadWeeklyContent() (lädt
// auch alle Notebook-/Bundle-/Download-URLs) unnötig viel wäre. Genau ein .md pro Woche
// (variantenunabhängig, siehe content/python-12-wochen-grundkurs/woche-N/wocheN.md) - ein
// Zertifikat gilt für alle Varianten gleich.
export async function loadWeekLernziele(lang = 'de') {
  const isEn = lang === 'en';
  const weekModules = isEn
    ? import.meta.glob('../../content/python-12-wochen-grundkurs-en/woche-*/*.md', { query: '?raw' })
    : import.meta.glob('../../content/python-12-wochen-grundkurs/woche-*/*.md', { query: '?raw' });

  const result = {};
  await Promise.all(
    Object.entries(weekModules).map(async ([path, loader]) => {
      if (path.includes('cheat_sheet') || path.includes('cheat-sheet')) return;
      const weekMatch = path.match(/woche-(\d+)/);
      if (!weekMatch) return;
      const weekNum = parseInt(weekMatch[1], 10);
      const rawContent = (await loader()).default;
      const parsed = fm(rawContent);
      const { lernzieleFull } = parseWeekMarkdown(parsed.body);
      result[weekNum] = {
        title: parsed.attributes.title || `${isEn ? 'Week' : 'Woche'} ${weekNum}`,
        lernzieleFull,
      };
    })
  );
  return result;
}

export async function loadWeeklyContent(lang = 'de') {
  const isEn = lang === 'en';

  // ── DE globs (always compiled by Vite — strings must be static literals) ─
  const weekModulesDe = import.meta.glob(
    '../../content/python-12-wochen-grundkurs/woche-*/*.md',
    { query: '?raw' }
  );
  const splitNotebookModulesDe = import.meta.glob(
    '../../content/python-12-wochen-grundkurs/woche-*/{abenteuer,pferde,scifi}/*/_generated/*.ipynb.json',
    { query: '?url', import: 'default' }
  );
  const bundleModulesDe = import.meta.glob(
    '../../content/python-12-wochen-grundkurs/woche-*/{abenteuer,pferde,scifi}/*/_bundle/*.py',
    { query: '?url', import: 'default' }
  );
  const downloadModulesDe = import.meta.glob(
    '../../content/python-12-wochen-grundkurs/woche-*/*.*',
    { query: '?url', import: 'default' }
  );

  // ── EN globs (empty until content is translated) ──────────────────────────
  const weekModulesEn = import.meta.glob(
    '../../content/python-12-wochen-grundkurs-en/woche-*/*.md',
    { query: '?raw' }
  );
  const splitNotebookModulesEn = import.meta.glob(
    '../../content/python-12-wochen-grundkurs-en/woche-*/{adventure,horses,scifi}/*/_generated/*.ipynb.json',
    { query: '?url', import: 'default' }
  );
  const bundleModulesEn = import.meta.glob(
    '../../content/python-12-wochen-grundkurs-en/woche-*/{adventure,horses,scifi}/*/_bundle/*.py',
    { query: '?url', import: 'default' }
  );
  const downloadModulesEn = import.meta.glob(
    '../../content/python-12-wochen-grundkurs-en/woche-*/*.*',
    { query: '?url', import: 'default' }
  );

  const weekModules          = isEn ? weekModulesEn          : weekModulesDe;
  const splitNotebookModules = isEn ? splitNotebookModulesEn : splitNotebookModulesDe;
  const bundleModules        = isEn ? bundleModulesEn        : bundleModulesDe;
  const downloadModules      = isEn ? downloadModulesEn      : downloadModulesDe;

  // EN dir names (adventure/horses/scifi) map to the same internal keys as DE
  const variantDirToKey = isEn
    ? { adventure: 'abenteuer', horses: 'pferde', scifi: 'scifi' }
    : { abenteuer: 'abenteuer', pferde: 'pferde', scifi: 'scifi' };

  // Zellen-Format: .../{variante}/woche{N}_{variante}_{typ}/_generated|_bundle/....
  const variantDirPattern = isEn
    ? /\/(adventure|horses|scifi)\/week\d+_(?:adventure|horses|scifi)_(\d+_\w+)\/_generated\/[^/]+\.ipynb\.json$/
    : /\/(abenteuer|pferde|scifi)\/woche\d+_(?:abenteuer|pferde|scifi)_(\d+_\w+)\/_generated\/[^/]+\.ipynb\.json$/;
  const bundleDirPattern = isEn
    ? /\/(adventure|horses|scifi)\/week\d+_(?:adventure|horses|scifi)_(\d+_\w+)\/_bundle\/[^/]+\.py$/
    : /\/(abenteuer|pferde|scifi)\/woche\d+_(?:abenteuer|pferde|scifi)_(\d+_\w+)\/_bundle\/[^/]+\.py$/;

  const weekLabel = isEn ? 'Week' : 'Woche';

  const weeklyContent = {};

  // ── Load split notebooks ────────────────────────────────────────────────
  await Promise.all(
    Object.entries(splitNotebookModules).map(async ([path, loader]) => {
      const weekMatch = path.match(/woche-(\d+)/);
      if (!weekMatch) return;
      const weekNum = parseInt(weekMatch[1], 10);

      const typeMatch = path.match(variantDirPattern);
      if (!typeMatch) return;
      const variantDir = typeMatch[1];
      const type       = typeMatch[2];
      if (!NOTEBOOK_TYPES.includes(type)) return;

      const variant = variantDirToKey[variantDir];
      if (!variant) return;

      const url = await loader();

      if (!weeklyContent[weekNum]) weeklyContent[weekNum] = emptyWeek(weekNum, weekLabel);

      weeklyContent[weekNum].hasNotebook = true;
      weeklyContent[weekNum].notebooks[variant][type] = { renderUrl: url, downloadUrl: null, downloadName: null };

      if (variant === 'abenteuer') {
        weeklyContent[weekNum].hasAbenteuerVariant = true;
        if (!weeklyContent[weekNum].selectedVariant)
          weeklyContent[weekNum].selectedVariant = 'abenteuer';
      } else if (variant === 'pferde') {
        weeklyContent[weekNum].hasPferdeVariant = true;
        if (!weeklyContent[weekNum].selectedVariant)
          weeklyContent[weekNum].selectedVariant = 'pferde';
      } else if (variant === 'scifi') {
        weeklyContent[weekNum].hasScifiVariant = true;
        if (!weeklyContent[weekNum].selectedVariant)
          weeklyContent[weekNum].selectedVariant = 'scifi';
      }
    })
  );

  // ── Load offline-bundle download URLs (Zellen-Format: eine .py-Datei pro Notebook) ──
  await Promise.all(
    Object.entries(bundleModules).map(async ([path, loader]) => {
      const weekMatch = path.match(/woche-(\d+)/);
      if (!weekMatch) return;
      const weekNum = parseInt(weekMatch[1], 10);

      const typeMatch = path.match(bundleDirPattern);
      if (!typeMatch) return;
      const variantDir = typeMatch[1];
      const type       = typeMatch[2];
      if (!NOTEBOOK_TYPES.includes(type)) return;

      const variant = variantDirToKey[variantDir];
      if (!variant) return;

      const url = await loader();
      // Kleine Bundles landen unter Vites Inline-Grenze als data:-URI ohne Dateinamen -
      // echten Namen aus dem Pfad ziehen, damit der Download-Button trotzdem sinnvoll heißt.
      const nameMatch = path.match(/\/([^/]+)\/_bundle\//);
      const downloadName = nameMatch ? `${nameMatch[1]}.py` : null;

      if (!weeklyContent[weekNum]) weeklyContent[weekNum] = emptyWeek(weekNum, weekLabel);
      if (!weeklyContent[weekNum].notebooks[variant][type]) {
        weeklyContent[weekNum].notebooks[variant][type] = { renderUrl: null, downloadUrl: null, downloadName: null };
      }
      weeklyContent[weekNum].notebooks[variant][type].downloadUrl = url;
      weeklyContent[weekNum].notebooks[variant][type].downloadName = downloadName;
    })
  );

  // ── Load week markdown (description + cheat sheets) ────────────────────
  await Promise.all(
    Object.entries(weekModules).map(async ([path, loader]) => {
      const weekMatch = path.match(/woche-(\d+)/);
      if (!weekMatch) return;
      if (path.includes('cheat_sheet') || path.includes('cheat-sheet')) return;

      const weekNum = parseInt(weekMatch[1], 10);
      const rawContent = (await loader()).default;
      const parsed = fm(rawContent);

      if (!weeklyContent[weekNum]) weeklyContent[weekNum] = emptyWeek(weekNum, weekLabel);

      const { shortDesc, lernziele, lernzieleFull } = parseWeekMarkdown(parsed.body);
      weeklyContent[weekNum].shortDesc = shortDesc;
      weeklyContent[weekNum].lernziele = lernziele;
      weeklyContent[weekNum].lernzieleFull = lernzieleFull;
      if (parsed.attributes.title) weeklyContent[weekNum].title = parsed.attributes.title;
    })
  );

  // ── Load other downloads ────────────────────────────────────────────────
  await Promise.all(
    Object.entries(downloadModules).map(async ([path, loader]) => {
      if (path.endsWith('.md') || path.endsWith('.ipynb')) return;
      const weekMatch = path.match(/woche-(\d+)/);
      if (!weekMatch) return;
      const weekNum = parseInt(weekMatch[1], 10);
      if (!weeklyContent[weekNum]) return;
      const url = await loader();
      weeklyContent[weekNum].downloads.push({ name: path.split('/').pop(), url });
    })
  );

  // ── Load cheat sheets ───────────────────────────────────────────────────
  await Promise.all(
    Object.entries(weekModules).map(async ([path, loader]) => {
      if (!path.includes('cheat_sheet') && !path.includes('cheat-sheet')) return;
      const weekMatch = path.match(/woche-(\d+)/);
      if (!weekMatch) return;
      const weekNum = parseInt(weekMatch[1], 10);
      if (!weeklyContent[weekNum]) return;

      const url = path.replace('../../content', '/content').replace('.md', '') + '.md';
      const filename = path.split('/').pop() || '';
      let name = 'Cheat Sheet';
      if (filename.includes('wissens')) name = isEn ? '📚 Knowledge Cheat Sheet' : '📚 Wissens-Cheat-Sheet';

      try {
        const contentLoader = await loader();
        const parsed = fm(contentLoader.default);
        if (!weeklyContent[weekNum].cheatSheets) weeklyContent[weekNum].cheatSheets = [];
        weeklyContent[weekNum].cheatSheets.push({
          name,
          content: marked(parsed.body),
          url,
          notebookUrl: null,
        });
      } catch (e) {
        console.error('Could not load cheat sheet content:', e);
      }
    })
  );

  Object.values(weeklyContent).forEach((week) => {
    if (week.cheatSheets?.length > 1) {
      week.cheatSheets.sort(
        (a, b) => (a.name.includes('Wissens') ? 0 : 1) - (b.name.includes('Wissens') ? 0 : 1)
      );
    }
  });

  return Object.values(weeklyContent).sort((a, b) => {
    const weekA = parseInt(a.title.match(/\d+/) || 0, 10);
    const weekB = parseInt(b.title.match(/\d+/) || 0, 10);
    return weekA - weekB;
  });
}
