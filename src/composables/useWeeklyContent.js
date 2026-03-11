import { reactive } from 'vue';
import fm from 'front-matter';
import { marked } from 'marked';

export async function loadWeeklyContent() {
  const weekModules = import.meta.glob('../../content/python-12-wochen-grundkurs/woche-*/*.md', { query: '?raw' });
  const notebookModules = import.meta.glob('../../content/python-12-wochen-grundkurs/woche-*/*.ipynb', { query: '?url', import: 'default' });
  const downloadModules = import.meta.glob('../../content/python-12-wochen-grundkurs/woche-*/*.*', { query: '?url', import: 'default' });
  const weeklyContent = {};

  await Promise.all(
    Object.entries(notebookModules).map(async ([path, loader]) => {
      const weekMatch = path.match(/woche-(\d+)/);
      if (!weekMatch) return;
      const weekNum = parseInt(weekMatch[1], 10);
      const notebookUrl = await loader();
      const isAbenteuer = path.includes('_abenteuer.ipynb');
      const isPferde = path.includes('_pferde.ipynb');
      const isScifi = path.includes('_scifi.ipynb');

      if (!weeklyContent[weekNum]) {
        weeklyContent[weekNum] = reactive({
          title: `Woche ${weekNum}`,
          hasNotebook: true,
          hasAbenteuerVariant: false,
          hasPferdeVariant: false,
          hasScifiVariant: false,
          abenteuerNotebookPath: null,
          abenteuerNotebookUrl: null,
          pferdeNotebookPath: null,
          pferdeNotebookUrl: null,
          scifiNotebookPath: null,
          scifiNotebookUrl: null,
          downloads: [],
          cheatSheets: [],
          wissensCheatSheetNotebookUrl: null,
          expandedCheatSheets: {},
          selectedVariant: null,
          expanded: weekNum === 1,
        });
      }

      if (isAbenteuer) {
        weeklyContent[weekNum].hasAbenteuerVariant = true;
        weeklyContent[weekNum].abenteuerNotebookPath = notebookUrl;
        weeklyContent[weekNum].abenteuerNotebookUrl = notebookUrl;
        if (!weeklyContent[weekNum].selectedVariant) weeklyContent[weekNum].selectedVariant = 'abenteuer';
      } else if (isPferde) {
        weeklyContent[weekNum].hasPferdeVariant = true;
        weeklyContent[weekNum].pferdeNotebookPath = notebookUrl;
        weeklyContent[weekNum].pferdeNotebookUrl = notebookUrl;
        if (!weeklyContent[weekNum].selectedVariant) weeklyContent[weekNum].selectedVariant = 'pferde';
      } else if (isScifi) {
        weeklyContent[weekNum].hasScifiVariant = true;
        weeklyContent[weekNum].scifiNotebookPath = notebookUrl;
        weeklyContent[weekNum].scifiNotebookUrl = notebookUrl;
        if (!weeklyContent[weekNum].selectedVariant) weeklyContent[weekNum].selectedVariant = 'scifi';
      } else if (path.includes('wissens_cheat_sheet')) {
        if (!weeklyContent[weekNum]) {
          weeklyContent[weekNum] = reactive({
            title: `Woche ${weekNum}`,
            hasNotebook: true,
            hasAbenteuerVariant: false,
            hasPferdeVariant: false,
            hasScifiVariant: false,
            abenteuerNotebookPath: null,
            abenteuerNotebookUrl: null,
            pferdeNotebookPath: null,
            pferdeNotebookUrl: null,
            scifiNotebookPath: null,
            scifiNotebookUrl: null,
            downloads: [],
            cheatSheets: [],
            wissensCheatSheetNotebookUrl: null,
            expandedCheatSheets: {},
            selectedVariant: null,
            expanded: weekNum === 1,
          });
        }
        weeklyContent[weekNum].wissensCheatSheetNotebookUrl = notebookUrl;
      }
    })
  );

  await Promise.all(
    Object.entries(weekModules).map(async ([path, loader]) => {
      const weekMatch = path.match(/woche-(\d+)/);
      if (!weekMatch) return;
      if (path.includes('cheat_sheet') || path.includes('cheat-sheet')) return;

      const weekNum = parseInt(weekMatch[1], 10);
      const rawContent = (await loader()).default;
      const parsed = fm(rawContent);

      if (weeklyContent[weekNum]) {
        weeklyContent[weekNum].content = marked(parsed.body);
        if (parsed.attributes.title) weeklyContent[weekNum].title = parsed.attributes.title;
      } else {
        weeklyContent[weekNum] = reactive({
          title: parsed.attributes.title || `Woche ${weekNum}`,
          content: marked(parsed.body),
          hasNotebook: false,
          downloads: [],
          selectedVariant: null,
          expanded: weekNum === 1,
        });
      }
    })
  );

  await Promise.all(
    Object.entries(downloadModules).map(async ([path, loader]) => {
      if (path.endsWith('.md') || path.endsWith('.ipynb')) return;
      const weekMatch = path.match(/woche-(\d+)/);
      if (!weekMatch) return;
      const weekNum = parseInt(weekMatch[1], 10);
      if (weeklyContent[weekNum]) {
        const url = await loader();
        weeklyContent[weekNum].downloads.push({ name: path.split('/').pop(), url });
      }
    })
  );

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
        const notebookUrl = weeklyContent[weekNum].wissensCheatSheetNotebookUrl || null;
        weeklyContent[weekNum].cheatSheets.push({
          name,
          content: marked(parsed.body),
          url,
          notebookUrl: filename.includes('wissens') ? notebookUrl : null,
        });
      } catch (e) {
        console.error('Could not load cheat sheet content:', e);
      }
    })
  );

  Object.values(weeklyContent).forEach((week) => {
    if (week.cheatSheets?.length > 1) {
      week.cheatSheets.sort((a, b) => (a.name.includes('Wissens') ? 0 : 1) - (b.name.includes('Wissens') ? 0 : 1));
    }
  });

  return Object.values(weeklyContent).sort((a, b) => {
    const weekA = parseInt(a.title.match(/\d+/) || 0, 10);
    const weekB = parseInt(b.title.match(/\d+/) || 0, 10);
    return weekA - weekB;
  });
}
