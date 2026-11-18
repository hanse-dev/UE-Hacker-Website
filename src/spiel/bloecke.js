// Blockly fuer die Spiel-Projekte (engine "spiel"): eigene deutsche Spiel-Bloecke, Werkzeugkasten
// und die Uebersetzung in Python. Die Bloecke erzeugen genau das Python, das auch die Python-Ansicht
// schreibt (Modul src/spiel/spiel.py) - beide Ansichten laufen auf derselben Spiel-Laufzeit und
// werden gleich geprueft. Die Gegenrichtung (Python -> Bloecke fuer Vorlagen und Loesungen) steht
// in src/spiel/zu_bloecken.py; jeder Block hier braucht dort ein Gegenstueck.
//
// Blockly ist gross (~1 MB) und wird nur in Spiel-Lektionen per dynamischem Import geladen - als
// `blockly/core` + `blockly/blocks`: Der Paket-Einstieg `blockly` zieht Node-Teile (jsdom/buffer) mit.

let geladen = null;

const FARBEN = [
  ['blau', 'blau'], ['rot', 'rot'], ['grün', 'gruen'], ['gelb', 'gelb'], ['orange', 'orange'],
  ['lila', 'lila'], ['pink', 'pink'], ['türkis', 'tuerkis'], ['braun', 'braun'], ['grau', 'grau'],
  ['schwarz', 'schwarz'], ['weiß', 'weiss'],
];
const EIGENSCHAFTEN = [['x', 'x'], ['y', 'y'], ['Breite', 'breite'], ['Höhe', 'hoehe'], ['Farbe', 'farbe']];
const TASTEN = [['← links', 'links'], ['→ rechts', 'rechts'], ['↑ oben', 'oben'], ['↓ unten', 'unten'], ['Leertaste', 'leertaste']];

const FARBE_START = '#d97706';
const FARBE_FIGUR = '#2563eb';
const FARBE_SPIEL = '#7c3aed';

const BLOECKE = [
  {
    type: 'spiel_start',
    message0: 'beim Start %1 %2',
    args0: [{ type: 'input_dummy' }, { type: 'input_statement', name: 'DO' }],
    colour: FARBE_START,
    tooltip: 'Läuft einmal, wenn du auf ▶ Spielen klickst.',
  },
  {
    type: 'spiel_jedes_bild',
    message0: 'jedes Bild %1 %2',
    args0: [{ type: 'input_dummy' }, { type: 'input_statement', name: 'DO' }],
    colour: FARBE_START,
    tooltip: 'Läuft immer wieder, 60-mal pro Sekunde, solange das Spiel läuft.',
  },
  {
    type: 'spiel_figur',
    message0: 'neue Figur %1 %2 x %3 y %4 Breite %5 Höhe %6',
    args0: [
      { type: 'field_dropdown', name: 'FARBE', options: FARBEN },
      { type: 'input_dummy' },
      { type: 'input_value', name: 'X', check: 'Number', align: 'RIGHT' },
      { type: 'input_value', name: 'Y', check: 'Number', align: 'RIGHT' },
      { type: 'input_value', name: 'B', check: 'Number', align: 'RIGHT' },
      { type: 'input_value', name: 'H', check: 'Number', align: 'RIGHT' },
    ],
    // Untereinander statt nebeneinander: schmaler, passt neben Lektionstext und Buehne.
    inputsInline: false,
    output: null,
    colour: FARBE_FIGUR,
    tooltip: 'Ein Rechteck auf der Bühne. x und y sind die linke obere Ecke.',
  },
  {
    type: 'spiel_setze',
    message0: 'setze %1 von %2 auf %3',
    args0: [
      { type: 'field_dropdown', name: 'EIG', options: EIGENSCHAFTEN },
      { type: 'field_variable', name: 'VAR', variable: 'spieler' },
      { type: 'input_value', name: 'WERT' },
    ],
    inputsInline: true,
    previousStatement: null,
    nextStatement: null,
    colour: FARBE_FIGUR,
  },
  {
    type: 'spiel_aendere',
    message0: 'ändere %1 von %2 um %3',
    args0: [
      { type: 'field_dropdown', name: 'EIG', options: EIGENSCHAFTEN.slice(0, 4) },
      { type: 'field_variable', name: 'VAR', variable: 'spieler' },
      { type: 'input_value', name: 'WERT', check: 'Number' },
    ],
    inputsInline: true,
    previousStatement: null,
    nextStatement: null,
    colour: FARBE_FIGUR,
    tooltip: 'Zählt etwas dazu. Mit einer Minuszahl wird es kleiner.',
  },
  {
    type: 'spiel_eigenschaft',
    message0: '%1 von %2',
    args0: [
      { type: 'field_dropdown', name: 'EIG', options: EIGENSCHAFTEN },
      { type: 'field_variable', name: 'VAR', variable: 'spieler' },
    ],
    output: null,
    colour: FARBE_FIGUR,
  },
  {
    type: 'spiel_beruehrt',
    message0: '%1 berührt %2',
    args0: [
      { type: 'field_variable', name: 'A', variable: 'spieler' },
      { type: 'field_variable', name: 'B', variable: 'stein' },
    ],
    output: 'Boolean',
    colour: FARBE_FIGUR,
  },
  {
    type: 'spiel_entferne',
    message0: 'entferne %1',
    args0: [{ type: 'field_variable', name: 'VAR', variable: 'stein' }],
    previousStatement: null,
    nextStatement: null,
    colour: FARBE_FIGUR,
    tooltip: 'Nimmt die Figur von der Bühne.',
  },
  {
    type: 'spiel_taste',
    message0: 'Taste %1 gedrückt',
    args0: [{ type: 'field_dropdown', name: 'TASTE', options: TASTEN }],
    output: 'Boolean',
    colour: FARBE_SPIEL,
  },
  {
    type: 'spiel_zufall',
    message0: 'Zufallszahl von %1 bis %2',
    args0: [
      { type: 'input_value', name: 'VON', check: 'Number' },
      { type: 'input_value', name: 'BIS', check: 'Number' },
    ],
    inputsInline: true,
    output: 'Number',
    colour: FARBE_SPIEL,
  },
  {
    type: 'spiel_zeige',
    message0: 'zeige %1',
    args0: [{ type: 'input_value', name: 'TEXT' }],
    previousStatement: null,
    nextStatement: null,
    colour: FARBE_SPIEL,
    tooltip: 'Schreibt einen Text oben links auf die Bühne.',
  },
  {
    type: 'spiel_ende',
    message0: 'Spiel vorbei %1',
    args0: [{ type: 'input_value', name: 'TEXT' }],
    previousStatement: null,
    nextStatement: null,
    colour: FARBE_SPIEL,
    tooltip: 'Hält das Spiel an und zeigt den Text groß in der Mitte.',
  },
  {
    type: 'spiel_hintergrund',
    message0: 'Hintergrund %1',
    args0: [{ type: 'field_dropdown', name: 'FARBE', options: FARBEN }],
    previousStatement: null,
    nextStatement: null,
    colour: FARBE_SPIEL,
  },
  {
    type: 'spiel_liste_add',
    message0: 'hänge %1 an die Liste %2 an',
    args0: [
      { type: 'input_value', name: 'WERT' },
      { type: 'field_variable', name: 'VAR', variable: 'steine' },
    ],
    inputsInline: true,
    previousStatement: null,
    nextStatement: null,
    colour: '#745ba5',
  },
];

const zahl = (n) => ({ shadow: { type: 'math_number', fields: { NUM: n } } });

export const WERKZEUGKASTEN = {
  kind: 'categoryToolbox',
  contents: [
    {
      kind: 'category', name: 'Spiel', colour: FARBE_START, contents: [
        { kind: 'block', type: 'spiel_start' },
        { kind: 'block', type: 'spiel_jedes_bild' },
        { kind: 'block', type: 'spiel_taste' },
        { kind: 'block', type: 'spiel_zufall', inputs: { VON: zahl(0), BIS: zahl(360) } },
        { kind: 'block', type: 'spiel_zeige', inputs: { TEXT: { shadow: { type: 'text', fields: { TEXT: 'Punkte' } } } } },
        { kind: 'block', type: 'spiel_ende', inputs: { TEXT: { shadow: { type: 'text', fields: { TEXT: 'Erwischt!' } } } } },
        { kind: 'block', type: 'spiel_hintergrund' },
      ],
    },
    {
      kind: 'category', name: 'Figuren', colour: FARBE_FIGUR, contents: [
        { kind: 'block', type: 'spiel_figur', inputs: { X: zahl(180), Y: zahl(0), B: zahl(40), H: zahl(40) } },
        { kind: 'block', type: 'spiel_aendere', inputs: { WERT: zahl(5) } },
        { kind: 'block', type: 'spiel_setze', inputs: { WERT: zahl(0) } },
        { kind: 'block', type: 'spiel_eigenschaft' },
        { kind: 'block', type: 'spiel_beruehrt' },
        { kind: 'block', type: 'spiel_entferne' },
      ],
    },
    {
      kind: 'category', name: 'Logik', categorystyle: 'logic_category', contents: [
        { kind: 'block', type: 'controls_if' },
        { kind: 'block', type: 'controls_if', extraState: { hasElse: true } },
        { kind: 'block', type: 'logic_compare' },
        { kind: 'block', type: 'logic_operation' },
        { kind: 'block', type: 'logic_negate' },
        { kind: 'block', type: 'logic_boolean' },
      ],
    },
    {
      kind: 'category', name: 'Schleifen', categorystyle: 'loop_category', contents: [
        { kind: 'block', type: 'controls_repeat_ext', inputs: { TIMES: zahl(3) } },
        { kind: 'block', type: 'controls_forEach' },
      ],
    },
    {
      kind: 'category', name: 'Rechnen', categorystyle: 'math_category', contents: [
        { kind: 'block', type: 'math_number' },
        { kind: 'block', type: 'math_arithmetic', inputs: { A: zahl(1), B: zahl(1) } },
      ],
    },
    {
      kind: 'category', name: 'Text', categorystyle: 'text_category', contents: [
        { kind: 'block', type: 'text' },
        { kind: 'block', type: 'text_join' },
      ],
    },
    {
      kind: 'category', name: 'Listen', categorystyle: 'list_category', contents: [
        { kind: 'block', type: 'lists_create_empty' },
        { kind: 'block', type: 'spiel_liste_add' },
        { kind: 'block', type: 'lists_length' },
      ],
    },
    { kind: 'category', name: 'Variablen', categorystyle: 'variable_category', custom: 'VARIABLE' },
  ],
};

function definiereBloecke(Blockly, pythonGenerator, Order) {
  Blockly.common.defineBlocksWithJsonArray(BLOECKE);
  const g = pythonGenerator;
  g.INDENT = '    ';
  const f = g.forBlock;
  const name = (block, feld = 'VAR') => g.getVariableName(block.getFieldValue(feld));
  const wert = (block, input, fallback = '0') => g.valueToCode(block, input, Order.NONE) || fallback;
  const ausruecken = (code) => code.replace(new RegExp(`^${g.INDENT}`, 'gm'), '');

  // Blockly schreibt sonst `x = None` fuer jede Variable an den Anfang - die Python-Ansicht hat das
  // nicht, und "Python ansehen" soll dasselbe zeigen.
  const init = g.init.bind(g);
  g.init = (workspace) => {
    init(workspace);
    delete g.definitions_.variables;
  };

  f.spiel_start = (block) => ausruecken(g.statementToCode(block, 'DO'));
  // `global` nur fuer Variablen, die in jedes_bild neu zugewiesen werden (setze/aendere) - genau
  // wie Python es verlangt und die Python-Vorlagen es schreiben (`global punkte`). Figuren wie
  // `spieler` brauchen es nicht, dort aendern sich nur x/y.
  f.spiel_jedes_bild = (block) => {
    const namen = [...new Set(block.getDescendants(false)
      .filter((b) => b.isEnabled() && (b.type === 'variables_set' || b.type === 'math_change'))
      .map((b) => name(b)))];
    const koerper = g.statementToCode(block, 'DO');
    let code = 'def jedes_bild():\n';
    if (namen.length) code += `${g.INDENT}global ${namen.join(', ')}\n`;
    return code + (koerper || `${g.INDENT}pass\n`);
  };
  f.spiel_figur = (block) => [
    `figur(${wert(block, 'X')}, ${wert(block, 'Y')}, ${wert(block, 'B', '40')}, ${wert(block, 'H', '40')}, "${block.getFieldValue('FARBE')}")`,
    Order.FUNCTION_CALL,
  ];
  f.spiel_setze = (block) => `${name(block)}.${block.getFieldValue('EIG')} = ${wert(block, 'WERT')}\n`;
  f.spiel_aendere = (block) => {
    const delta = wert(block, 'WERT');
    const ziel = `${name(block)}.${block.getFieldValue('EIG')}`;
    if (/^-\d+(\.\d+)?$/.test(delta)) return `${ziel} -= ${delta.slice(1)}\n`;
    return `${ziel} += ${delta}\n`;
  };
  f.spiel_eigenschaft = (block) => [`${name(block)}.${block.getFieldValue('EIG')}`, Order.MEMBER];
  f.spiel_beruehrt = (block) => [`${name(block, 'A')}.beruehrt(${name(block, 'B')})`, Order.FUNCTION_CALL];
  f.spiel_entferne = (block) => `${name(block)}.entferne()\n`;
  f.spiel_taste = (block) => [`taste("${block.getFieldValue('TASTE')}")`, Order.FUNCTION_CALL];
  f.spiel_zufall = (block) => [`zufall(${wert(block, 'VON')}, ${wert(block, 'BIS', '360')})`, Order.FUNCTION_CALL];
  f.spiel_zeige = (block) => `zeige(${wert(block, 'TEXT', "''")})\n`;
  f.spiel_ende = (block) => `spiel_ende(${g.valueToCode(block, 'TEXT', Order.NONE)})\n`;
  f.spiel_hintergrund = (block) => `hintergrund("${block.getFieldValue('FARBE')}")\n`;
  f.spiel_liste_add = (block) => `${name(block)}.append(${wert(block, 'WERT', 'None')})\n`;
  // Blockly schreibt fuer "aendere um" sonst `x = (x if isinstance(x, Number) else 0) + 1`.
  f.math_change = (block) => {
    const delta = wert(block, 'DELTA');
    if (/^-\d+(\.\d+)?$/.test(delta)) return `${name(block)} -= ${delta.slice(1)}\n`;
    return `${name(block)} += ${delta}\n`;
  };
}

/** Laedt Blockly einmal (dynamischer Import) und gibt { Blockly, pythonGenerator } zurueck. */
export function ladeBlockly() {
  if (!geladen) {
    geladen = (async () => {
      const [Blockly, python, , De] = await Promise.all([
        import('blockly/core'),
        import('blockly/python'),
        import('blockly/blocks'),
        import('blockly/msg/de'),
      ]);
      Blockly.setLocale(De);
      // Wie im MakeCode-Editor der micro:bit-Kurse: "wenn ... dann" statt "falls ... mache", und
      // "aendere ... um" passt auch zu Minuszahlen (statt "erhoehe").
      Object.assign(Blockly.Msg, {
        CONTROLS_IF_MSG_IF: 'wenn',
        CONTROLS_IF_MSG_THEN: 'dann',
        CONTROLS_IF_MSG_ELSEIF: 'sonst wenn',
        CONTROLS_IF_MSG_ELSE: 'sonst',
        MATH_CHANGE_TITLE: 'ändere %1 um %2',
        CONTROLS_REPEAT_INPUT_DO: '',
        CONTROLS_FOREACH_INPUT_DO: '',
      });
      definiereBloecke(Blockly, python.pythonGenerator, python.Order);
      return { Blockly, pythonGenerator: python.pythonGenerator };
    })();
  }
  return geladen;
}

/** Python-Code aus einem Arbeitsbereich - mit `from spiel import *`, wie die Python-Ansicht ihn hat. */
export function pythonAusBloecken(pythonGenerator, workspace) {
  const code = pythonGenerator.workspaceToCode(workspace).trim();
  return `from spiel import *\n\n${code}\n`;
}

/** Blockly-Themes passend zu useTheme.js (hell/dunkel). */
const themes = {};
export function blocklyTheme(Blockly, dunkel) {
  const name = dunkel ? 'ue-spiel-dunkel' : 'ue-spiel-hell';
  themes[name] ||= Blockly.Theme.defineTheme(name, {
      base: Blockly.Themes.Classic,
      fontStyle: { family: 'system-ui, sans-serif', size: 12 },
      componentStyles: dunkel
        ? {
          workspaceBackgroundColour: '#1b1f2a',
          toolboxBackgroundColour: '#252a37',
          toolboxForegroundColour: '#e5e7eb',
          flyoutBackgroundColour: '#2d3343',
          flyoutForegroundColour: '#e5e7eb',
          flyoutOpacity: 0.95,
          scrollbarColour: '#4b5563',
          insertionMarkerColour: '#ffffff',
          gridColour: '#2f3545',
        }
        : {
          workspaceBackgroundColour: '#f8fafc',
          toolboxBackgroundColour: '#eef2f7',
          toolboxForegroundColour: '#1f2937',
          flyoutBackgroundColour: '#e5e9f0',
          flyoutOpacity: 0.95,
          gridColour: '#e2e8f0',
        },
  });
  return themes[name];
}
