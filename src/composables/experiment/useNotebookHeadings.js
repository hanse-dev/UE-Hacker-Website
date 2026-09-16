import { ref, watch } from 'vue';

/**
 * Extracts the sub-section headings of a notebook (##/### at the start of a markdown
 * cell) so the tour side menu can offer a jump-list into the currently open step.
 * The very first cell's "#" title is skipped (that's the notebook title, not a section).
 */
function extractHeadings(cells) {
  const headings = [];
  cells.forEach((cell, index) => {
    if (cell.cell_type !== 'markdown') return;
    const source = Array.isArray(cell.source) ? cell.source.join('') : cell.source;
    const match = source.match(/^\s*(#{2,3})\s+(.+)$/m);
    if (!match) return;
    headings.push({
      cellIndex: index,
      level: match[1].length,
      text: match[2].trim(),
    });
  });
  return headings;
}

export function useNotebookHeadings(renderUrlRef) {
  const headings = ref([]);

  const load = async (url) => {
    if (!url) {
      headings.value = [];
      return;
    }
    try {
      const res = await fetch(url);
      if (!res.ok) throw new Error('failed to load notebook');
      const nb = await res.json();
      headings.value = extractHeadings(nb.cells || []);
    } catch {
      headings.value = [];
    }
  };

  watch(renderUrlRef, (url) => load(url), { immediate: true });

  return { headings };
}
