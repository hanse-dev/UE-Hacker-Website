import { EditorView } from '@codemirror/view';
import { HighlightStyle, syntaxHighlighting } from '@codemirror/language';
import { tags } from '@lezer/highlight';

// Farben der Code-Editoren über CSS-Variablen (--cm-*, src/style.css), damit Hell/Dunkel ohne
// Neuaufbau des Editors umschaltet. Ersetzt den hellen Standard-Highlighter von basicSetup.
const highlight = HighlightStyle.define([
  { tag: [tags.keyword, tags.controlKeyword, tags.operatorKeyword, tags.moduleKeyword, tags.definitionKeyword], color: 'var(--cm-keyword)' },
  { tag: [tags.string, tags.special(tags.string), tags.regexp], color: 'var(--cm-string)' },
  { tag: [tags.number, tags.bool, tags.null, tags.atom], color: 'var(--cm-number)' },
  { tag: [tags.comment, tags.lineComment, tags.blockComment], color: 'var(--cm-comment)', fontStyle: 'italic' },
  { tag: [tags.definition(tags.variableName), tags.function(tags.definition(tags.variableName)), tags.definition(tags.propertyName)], color: 'var(--cm-def)' },
  { tag: [tags.standard(tags.variableName), tags.className, tags.typeName, tags.self], color: 'var(--cm-builtin)' },
  { tag: [tags.tagName, tags.angleBracket], color: 'var(--cm-keyword)' },
  { tag: tags.attributeName, color: 'var(--cm-def)' },
  { tag: tags.invalid, color: 'var(--danger)' },
]);

export const editorColors = [
  syntaxHighlighting(highlight),
  EditorView.theme({
    // Hintergrund und Zeilennummern-Leiste setzen die Komponenten selbst (.cm-host, --surface-tint).
    '&': { color: 'var(--text)' },
    '.cm-content': { caretColor: 'var(--text)' },
    '.cm-cursor, .cm-dropCursor': { borderLeftColor: 'var(--text)' },
    '.cm-activeLine': { backgroundColor: 'var(--cm-active-line)' },
    '.cm-activeLineGutter': { backgroundColor: 'var(--cm-active-line)' },
    '&.cm-focused > .cm-scroller > .cm-selectionLayer .cm-selectionBackground, .cm-selectionBackground, ::selection': {
      backgroundColor: 'var(--cm-selection)',
    },
    '.cm-tooltip': {
      backgroundColor: 'var(--surface)',
      color: 'var(--text)',
      border: '1px solid var(--border-strong)',
    },
    '.cm-tooltip-autocomplete > ul > li[aria-selected]': {
      backgroundColor: 'var(--primary-purple)',
      color: '#fff',
    },
    '.cm-matchingBracket, &.cm-focused .cm-matchingBracket': { backgroundColor: 'var(--cm-selection)' },
  }),
];
