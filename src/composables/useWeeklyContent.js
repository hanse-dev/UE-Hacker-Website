import { reactive } from 'vue';
import fm from 'front-matter';
import { marked } from 'marked';

// ── Markdown parser: extract shortDesc + lernziele ──────────────────────────
function parseWeekMarkdown(body) {
  const lines = body.split('\n');
  let shortDesc = '';
  const lernziele = [];
  const descLines = [];
  let inWelten = false;
  let inLernziele = false;

  for (const line of lines) {
    const trimmed = line.trim();

    // Detect section headings
    if (/^#{1,3}\s+/.test(trimmed)) {
      const headingText = trimmed.replace(/^#+\s+/, '').toLowerCase();
      inWelten    = /welten|auswahl|themenwelt/.test(headingText);
      inLernziele = headingText.includes('lernziel');
      continue;
    }

    if (inWelten || !trimmed) continue;

    if (inLernziele && trimmed.startsWith('- ')) {
      const raw = trimmed.slice(2);
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

  return { shortDesc, lernziele };
}

const NOTEBOOK_TYPES = [
  '0_glossar',
  '1_lektion',
  '2_debug',
  '3_missionen',
  '4_reflexion',
  '5_loesungen',
  '6_boss',
];

function emptyWeek(weekNum) {
  return reactive({
    title: `Woche ${weekNum}`,
    shortDesc: '',
    lernziele: [],
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
    expanded: weekNum === 1,
  });
}

export async function loadWeeklyContent() {
  const weekModules = import.meta.glob(
    '../../content/python-12-wochen-grundkurs/woche-*/*.md',
    { query: '?raw' }
  );

  // Split notebooks live in theme subfolders
  const splitNotebookModules = import.meta.glob(
    '../../content/python-12-wochen-grundkurs/woche-*/{abenteuer,pferde,scifi}/*.ipynb',
    { query: '?url', import: 'default' }
  );

  const downloadModules = import.meta.glob(
    '../../content/python-12-wochen-grundkurs/woche-*/*.*',
    { query: '?url', import: 'default' }
  );

  const weeklyContent = {};

  // ── Load split notebooks ────────────────────────────────────────────────
  await Promise.all(
    Object.entries(splitNotebookModules).map(async ([path, loader]) => {
      const weekMatch = path.match(/woche-(\d+)/);
      if (!weekMatch) return;
      const weekNum = parseInt(weekMatch[1], 10);

      // Extract variant (abenteuer|pferde|scifi) and type (0_glossar, 1_lektion…)
      const typeMatch = path.match(/\/(abenteuer|pferde|scifi)\/woche\d+_(?:abenteuer|pferde|scifi)_(\d+_\w+)\.ipynb$/);
      if (!typeMatch) return;
      const variant = typeMatch[1];
      const type = typeMatch[2];
      if (!NOTEBOOK_TYPES.includes(type)) return;

      const url = await loader();

      if (!weeklyContent[weekNum]) weeklyContent[weekNum] = emptyWeek(weekNum);

      weeklyContent[weekNum].hasNotebook = true;
      weeklyContent[weekNum].notebooks[variant][type] = url;

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

  // ── Load week markdown (description + cheat sheets) ────────────────────
  await Promise.all(
    Object.entries(weekModules).map(async ([path, loader]) => {
      const weekMatch = path.match(/woche-(\d+)/);
      if (!weekMatch) return;
      if (path.includes('cheat_sheet') || path.includes('cheat-sheet')) return;

      const weekNum = parseInt(weekMatch[1], 10);
      const rawContent = (await loader()).default;
      const parsed = fm(rawContent);

      if (!weeklyContent[weekNum]) weeklyContent[weekNum] = emptyWeek(weekNum);

      const { shortDesc, lernziele } = parseWeekMarkdown(parsed.body);
      weeklyContent[weekNum].shortDesc = shortDesc;
      weeklyContent[weekNum].lernziele = lernziele;
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
      if (filename.includes('wissens')) name = '📚 Wissens-Cheat-Sheet';
      else if (filename.includes('turtle')) name = '🐢 Turtle Cheat Sheet';

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
