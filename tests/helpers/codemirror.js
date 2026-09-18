// Gemeinsamer Helper fuer alle CodeMirror-6-Editoren im Repo (12-Wochen-Notebooks via
// CodeCell.vue, JS-Spielewerkstatt via JsCodeCell.vue) - .fill()/.inputValue() funktionieren
// dort nicht, da es keine <textarea> ist. insertText() statt type(), damit CodeMirrors
// Auto-Indent literale "\n"-Zeichen in mehrzeiligem Test-Code nicht zusaetzlich einrueckt.
export async function setCodeMirrorContent(cmHost, code) {
  const content = cmHost.locator('.cm-content');
  await content.click();
  await content.press('ControlOrMeta+a');
  await content.press('Backspace');
  await content.page().keyboard.insertText(code);
}
