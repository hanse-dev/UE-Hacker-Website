<template>
  <div class="lesson-view js-lesson-view" :class="{ 'with-workspace': workspaceEnabled }">
   <div class="js-lesson-grid">
    <div class="lesson-content">
      <p v-if="!lessonContent" class="lesson-loading">{{ t('lesson.loading') }}</p>
      <div v-else v-html="lessonContent"></div>
      <ConceptBox v-if="lessonContent && conceptList.length" :concepts="conceptList" />
    </div>

    <div class="lesson-editor-section">
      <p class="editor-hint">{{ t('jsLesson.editorHint') }}</p>
      <p class="editor-hint editor-hint-ran">{{ t('jsLesson.ranExplainer') }}</p>

      <template v-for="(task, idx) in tasks" :key="lesson.id + '-' + idx">
        <div
          class="task-block"
          :class="isExample(idx) ? 'task-example' : 'task-required'"
          :style="{ order: 10 + idx * 2 }"
        >
          <span class="task-badge" :class="isExample(idx) ? 'badge-example' : 'badge-required'">
            {{ isExample(idx) ? t('jsLesson.badgeExample') : t('jsLesson.badgeRequired') }}
          </span>
          <p class="task-instruction">
            <span v-if="completedTasks.has(idx)" class="task-done">✓</span>
            <span v-else-if="skippedTasks.has(idx)" class="task-skipped">⏭</span>
            <span v-else class="task-pending">○</span>
            <span v-html="instructionWithGlossary(task.instruction || t('lesson.taskPrefix') + (idx + 1))"></span>
            <span v-if="completedTasks.has(idx)" class="task-status-label">{{ t('lesson.taskDone') }}</span>
            <span v-else-if="skippedTasks.has(idx)" class="task-status-label">{{ t('lesson.taskSkipped') }}</span>
            <span v-else-if="completedTasks.size > 0" class="task-status-label">{{ t('lesson.taskPending') }}</span>
          </p>
          <p v-if="task.meineSeite" class="meine-seite-note">🏠 {{ t('webLesson.meineSeite') }}</p>
          <div class="code-editor-wrapper" :class="{ 'code-editor-ran': taskRan[idx] }">
            <JsCodeCell v-model="taskCodes[idx]" :language="webMode ? 'html' : 'javascript'" />
          </div>
          <p v-if="taskRan[idx]" class="code-ran-note">▶ {{ t('jsLesson.alreadyRan') }}</p>
          <div class="editor-actions">
            <button @click="runTask(idx)" :disabled="checking" class="btn-run">
              {{ t('editor.run') }}
            </button>
            <button
              v-if="!isExample(idx)"
              @click="checkTask(idx)"
              :disabled="checking"
              class="btn-check"
            >
              {{ checking ? t('editor.checking') : t('editor.check') }}
            </button>
            <button
              v-if="!isExample(idx) && !isTaskDone(idx) && (taskAttempts[idx] || 0) >= 2"
              @click="skipTask(idx)"
              :disabled="checking"
              class="btn-skip"
            >
              {{ t('lesson.skipTask') }}
            </button>
            <button
              v-if="task.codeTemplate && !task.meineSeite && taskCodes[idx] !== task.codeTemplate"
              @click="resetTask(idx)"
              :disabled="checking"
              class="btn-reset"
            >
              {{ t('editor.reset') }}
            </button>
            <button v-if="webMode" type="button" @click="downloadTask(idx)" class="btn-reset btn-download">
              {{ t('webLesson.download') }}
            </button>
          </div>
          <details v-if="task.solution" class="solution-reveal">
            <summary>{{ t('jsLesson.showSolution') }}</summary>
            <pre class="solution-code">{{ task.solution }}</pre>
          </details>
          <div v-if="taskOutputs[idx] !== null" class="output-display">
            <strong>{{ t('editor.output') }}</strong>
            <pre class="output-content">{{ taskOutputs[idx] }}</pre>
          </div>
          <div v-if="taskFeedback[idx]" :class="['feedback', taskFeedback[idx].success ? 'feedback-success' : 'feedback-error']">
            {{ taskFeedback[idx].message }}
          </div>
        </div>
      </template>

      <!-- Arbeitsflaeche: EINE Sandbox fuer die ganze Lektion. Breit (Container >= 920px) steht sie
           als mitlaufende Spalte rechts neben Text und Aufgaben, schmal per CSS-`order` direkt unter
           der zuletzt ausgefuehrten Aufgabe - ohne das iframe im DOM zu verschieben (das wuerde es
           neu laden). -->
      <div
        class="js-workspace"
        :class="{ 'is-empty': activeIdx === null, 'no-canvas': activeIdx !== null && !activeShowsCanvas }"
        :style="{ order: activeIdx === null ? 9998 : 11 + activeIdx * 2 }"
      >
        <div class="js-workspace-inner">
          <p class="js-workspace-title">
            {{ t('jsLesson.workspaceTitle') }}<span v-if="activeIdx !== null" class="js-workspace-task"> · {{ t('jsLesson.workspaceTask').replace('{n}', activeIdx + 1) }}</span>
          </p>
          <p v-if="activeIdx === null" class="js-workspace-hint">{{ t('jsLesson.workspaceEmpty') }}</p>
          <JsSandboxFrame v-if="activeIdx !== null" ref="sandboxEl" :show-canvas="activeShowsCanvas" :dom-mode="domMode" :web-mode="webMode" />
          <!-- Breit zeigt die Arbeitsflaeche auch die Ausgabe (dann ohne Kopie unter dem Code), damit
               rechts immer das ganze Ergebnis steht - auch bei Aufgaben, die nichts zeichnen. -->
          <div v-if="activeIdx !== null && taskOutputs[activeIdx] !== null" class="output-display js-workspace-output">
            <strong>{{ t('editor.output') }}</strong>
            <pre class="output-content">{{ taskOutputs[activeIdx] }}</pre>
          </div>
        </div>
      </div>

      <div v-if="allTasksComplete" class="lesson-complete-box" :style="{ order: 99999 }">
        <p class="lesson-summary">{{ lessonSummary }}</p>
        <ProjectCompletionBox v-if="isProjectCourse && isLastLesson" :next-course-id="lesson.nextCourseId" />
        <template v-else>
          <router-link
            v-if="lesson.nextCourseId"
            :to="'/kurs/' + lesson.nextCourseId"
            class="btn-next"
          >
            {{ t('lesson.goToWeeklyCourse') }}
          </router-link>
          <button v-else @click="goToNext" class="btn-next">{{ t(leadsToFinalCheck ? 'check.toFinal' : 'lesson.nextLesson') }}</button>
        </template>
      </div>
    </div>
   </div>
  </div>
</template>

<script>
import { ref, watch, onMounted, onBeforeUnmount, computed, nextTick } from 'vue';
import JsSandboxFrame from './JsSandboxFrame.vue';
import JsCodeCell from './JsCodeCell.vue';
import { useInteractiveProgress } from '../composables/useInteractiveProgress';
import { useLanguage } from '../composables/useLanguage';
import { validateOutput, validateWebChecks } from '../composables/useTaskValidation';
import { webDocumentForDownload } from '../composables/useJsSandbox';
import { loadSavedCode, saveLessonCode, loadMeineSeite, saveMeineSeite } from '../composables/useSavedCode';
import { DEV_SKIP_CHECKS } from '../composables/devSkipChecks.js';
import { useLessonContent } from '../composables/useLessonContent';
import ProjectCompletionBox from './ProjectCompletionBox.vue';
import ConceptBox from './ConceptBox.vue';
import { conceptsInText, mergeConcepts } from '../composables/useConcepts';

export default {
  name: 'JsLessonView',
  components: { JsSandboxFrame, JsCodeCell, ProjectCompletionBox, ConceptBox },
  props: {
    lesson: { type: Object, required: true },
    contentPath: { type: String, required: true },
    variant: { type: String, default: 'kinder' },
    courseId: { type: String, default: 'python-grundlagen-interaktiv' },
    showCanvas: { type: Boolean, default: true },
    domMode: { type: Boolean, default: false },
    // Web-Kurse (`"sandboxMode": "web"` in kurse.json): Aufgaben sind HTML-Seiten statt JS, die
    // Arbeitsflaeche zeigt die Seite selbst, Pruefungen laufen ueber `validation.type: 'web'`.
    webMode: { type: Boolean, default: false },
    // true nur bei ProjectCourse.vue (Projekt-Kurse) - steuert, ob am Ende der letzten Lektion
    // ProjectCompletionBox (Abzeichen-Hinweis + zurueck zu /projekte) statt des generischen
    // "Weiter"-Buttons erscheint.
    isProjectCourse: { type: Boolean, default: false },
    isLastLesson: { type: Boolean, default: false },
    // Letzte Lektion eines Kurses mit Abschluss-Check (ProjectCourse.vue `finalCheck`): der
    // Weiter-Knopf fuehrt zum Check statt zur naechsten Lektion.
    leadsToFinalCheck: { type: Boolean, default: false },
    // Begriffs-Links (useConcepts.js, content/begriffe.json): Sprache (`javascript`/`python`) -
    // Begriffe im Lektionstext verlinken auf die Grundkurs-Woche, am Ende steht der "Hier lernst du
    // mehr"-Kasten. Leer = aus. In einem Grundkurs selbst zusaetzlich conceptCourse/conceptWeek,
    // dann nur Verweise auf fruehere Wochen. Nur auf Deutsch (die Erklaerungen sind deutsch).
    conceptLanguage: { type: String, default: '' },
    conceptCourse: { type: String, default: '' },
    conceptWeek: { type: Number, default: 0 },
  },
  emits: ['completed', 'next'],
  setup(props, { emit }) {
    const { lang, t } = useLanguage();
    const conceptOptions = computed(() => (props.conceptLanguage && lang.value !== 'en'
      ? { language: props.conceptLanguage, course: props.conceptCourse, week: props.conceptWeek }
      : null));
    const { markCompleted } = useInteractiveProgress(props.variant, props.courseId);

    // Eine gemeinsame Sandbox (Arbeitsflaeche) fuer alle Aufgaben der Lektion - jeder Lauf baut das
    // iframe ohnehin komplett neu auf (kein geteilter Zustand zwischen Laeufen, siehe
    // useJsSandbox.js). activeIdx = Aufgabe, deren Ergebnis die Arbeitsflaeche gerade zeigt; erst
    // beim ersten Ausfuehren wird das Frame gemountet (Heartbeat-Schleife, siehe runTask).
    const sandboxEl = ref(null);
    const activeIdx = ref(null);
    const checking = ref(false);
    const isMounted = ref(true);
    const { lessonContent, lessonConcepts, loadGlossary, loadContent, instructionWithGlossary } = useLessonContent(
      isMounted,
      { conceptOptions: () => conceptOptions.value },
    );

    const tasks = computed(() => {
      const list = props.lesson?.tasks;
      return Array.isArray(list) ? list : [];
    });

    const conceptList = computed(() => (conceptOptions.value
      ? mergeConcepts(
        lessonConcepts.value,
        ...tasks.value.map((task) => conceptsInText(task.instruction, conceptOptions.value)),
      )
      : []));

    // Beispiel-Aufgaben (bereits fertiger, unveraenderter codeTemplate zum Anschauen) brauchen
    // keinen "Pruefen"-Button - nur "Ausfuehren". Deine-Aufgabe-Aufgaben (leerer/unfertiger
    // codeTemplate, echte Erwartung) brauchen beides. Reines Anzeige-/Verhaltensmerkmal, keine
    // eigene Validierung - jede Aufgabe hat weiterhin ein `validation`-Objekt.
    const isExample = (idx) => !!tasks.value[idx]?.example;

    // Eine Aufgabe, die nichts zeichnet (reine Funktionslogik, z.B. eine isolierte Hilfsfunktion
    // vor dem Einbau ins Spiel), braucht auch keinen sichtbaren Canvas-Bereich - der wirkt dort
    // nur als leere graue Flaeche. `task.showCanvas: false` in lessons.json blendet ihn fuer genau
    // diese eine Aufgabe aus, ohne das kurs-/lektionsweite showCanvas-Prop anzutasten.
    const taskShowsCanvas = (idx) => tasks.value[idx]?.showCanvas ?? props.showCanvas;

    // Geteilte Ansicht nur, wenn in der Lektion ueberhaupt etwas zu sehen ist - reine
    // Konsolen-Lektionen (z.B. js-grundkurs Woche 1-6) bleiben einspaltig, das Frame laeuft dort
    // unsichtbar weiter.
    const workspaceEnabled = computed(() => tasks.value.some((_, idx) => taskShowsCanvas(idx)));
    const activeShowsCanvas = computed(() => activeIdx.value !== null && taskShowsCanvas(activeIdx.value));

    // Uebersprungene Aufgaben zaehlen fuer den Lektions-Abschluss wie erledigt (damit man nicht
    // blockiert bleibt), bleiben aber optisch als "uebersprungen" erkennbar statt als geloest -
    // gilt bewusst nur fuer normale Lektionsaufgaben, nicht fuer den Wochen-Check (CodeChallenge.vue).
    const doneCount = computed(() => new Set([...completedTasks.value, ...skippedTasks.value]).size);
    const isTaskDone = (idx) => completedTasks.value.has(idx) || skippedTasks.value.has(idx);

    const allTasksComplete = computed(() => {
      const list = tasks.value;
      return list.length > 0 && doneCount.value === list.length;
    });

    const lessonSummary = computed(() => props.lesson?.lessonSummary || t('lesson.defaultSummary'));

    const taskCodes = ref([]);
    const taskOutputs = ref([]);
    const taskFeedback = ref([]);
    const taskAttempts = ref([]);
    const taskRan = ref([]);
    const completedTasks = ref(new Set());
    const skippedTasks = ref(new Set());

    const initTaskState = () => {
      const list = tasks.value;
      const templates = list.map((x) => x.codeTemplate ?? '');
      // Zwischengespeicherten Code (max. 5 Tage alt, nur lokal) wiederherstellen - wie LessonView.vue.
      // „Meine Seite“-Aufgaben (Web-Kurse) starten mit der eigenen, über alle Lektionen
      // mitwachsenden Seite; erst wenn es die noch nicht gibt, mit der Vorlage.
      const saved = loadSavedCode(props.contentPath)[props.lesson?.id];
      const codes = saved && saved.codes.length === templates.length ? [...saved.codes] : templates;
      const meineSeite = list.some((x) => x.meineSeite) ? loadMeineSeite(props.contentPath) : null;
      taskCodes.value = codes.map((code, i) => (list[i].meineSeite && meineSeite ? meineSeite : code));
      taskOutputs.value = list.map(() => null);
      taskFeedback.value = list.map(() => null);
      taskAttempts.value = list.map(() => 0);
      taskRan.value = list.map(() => false);
      completedTasks.value = new Set();
      skippedTasks.value = new Set();
      activeIdx.value = null;
    };

    const skipTask = (idx) => {
      if (isTaskDone(idx)) return;
      skippedTasks.value = new Set([...skippedTasks.value, idx]);
      taskFeedback.value[idx] = null;
      if (doneCount.value === tasks.value.length) markCompleted(props.lesson.id);
    };

    // Stellt nur den vorgegebenen codeTemplate der einen Aufgabe wieder her - Fortschritt/Status
    // der anderen Aufgaben bleibt unberuehrt, ebenso ob die Aufgabe schon erledigt ist.
    const resetTask = (idx) => {
      taskCodes.value[idx] = tasks.value[idx]?.codeTemplate ?? '';
      taskOutputs.value[idx] = null;
      taskFeedback.value[idx] = null;
      taskRan.value[idx] = false;
      if (activeIdx.value === idx) activeIdx.value = null;
    };

    watch(taskCodes, (codes) => {
      if (!props.lesson?.id || !codes.length) return;
      const templates = tasks.value.map((x) => x.codeTemplate ?? '');
      saveLessonCode(props.contentPath, props.lesson.id, codes, templates);
      tasks.value.forEach((task, i) => {
        if (task.meineSeite && codes[i] !== templates[i]) saveMeineSeite(props.contentPath, codes[i]);
      });
    }, { deep: true });

    const activate = async (idx) => {
      taskRan.value[idx] = true;
      activeIdx.value = idx;
      await nextTick();
      sandboxEl.value.scrollIntoView();
    };

    onMounted(() => {
      loadGlossary(props.contentPath);
    });

    onBeforeUnmount(() => {
      isMounted.value = false;
    });

    watch(
      () => props.lesson,
      (newLesson) => {
        initTaskState();
        loadContent(newLesson, props.contentPath);
      },
      { immediate: true }
    );

    // Ein Rechteck zu zeichnen erzeugt keine console.log-Ausgabe - ohne diesen Hinweis wirkt die
    // "Ausgabe"-Box faelschlich leer, obwohl oben im Spielfeld sichtbar etwas passiert ist. Nur
    // relevant, wenn diese Lektion ueberhaupt ein sichtbares Canvas hat (showCanvas).
    const withCanvasNote = async (idx, rawOutput) => {
      const trimmed = (rawOutput || '').trim();
      // Web-Modus: das Ergebnis ist die Seite in der Arbeitsflaeche - eine Ausgabe-Box gibt es nur,
      // wenn ein <script> wirklich etwas mit console.log geschrieben hat.
      if (props.webMode) return trimmed || null;
      if (!taskShowsCanvas(idx)) return trimmed || t('jsLesson.noOutput');
      const drew = await sandboxEl.value.checkCanvasNotBlank();
      if (drew) return trimmed ? `${trimmed}\n\n${t('jsLesson.canvasNote')}` : t('jsLesson.canvasNote');
      return trimmed || t('jsLesson.noOutput');
    };

    const runTask = async (idx) => {
      if (checking.value) return;
      checking.value = true;
      taskOutputs.value[idx] = null;
      taskFeedback.value[idx] = null;
      // Sandbox-Frame wird erst bei der ersten Ausfuehrung ueberhaupt gemountet (v-if auf activeIdx)
      // - vorher gibt es nichts zu sehen, und ein gemountetes Frame startet eine dauerhaft
      // laufende requestAnimationFrame-Heartbeat-Schleife (useJsSandbox.js).
      await activate(idx);

      const result = await sandboxEl.value.run(taskCodes.value[idx]);
      if (!isMounted.value) return;

      taskOutputs.value[idx] = result.success
        ? await withCanvasNote(idx, result.output)
        : t('editor.errorPrefix') + (result.error || t('jsLesson.unknownError'));
      // Beispiel-Aufgaben haben keinen "Pruefen"-Button - ein erfolgreicher Lauf zaehlt hier schon
      // als "gesehen/erledigt", damit die Lektion trotzdem abschliessbar bleibt.
      if (result.success && isExample(idx)) markExampleDone(idx);
      checking.value = false;
    };

    const markExampleDone = (idx) => {
      if (completedTasks.value.has(idx)) return;
      completedTasks.value = new Set([...completedTasks.value, idx]);
      if (doneCount.value === tasks.value.length) markCompleted(props.lesson.id);
    };

    const checkTask = async (idx) => {
      if (checking.value) return;
      // Dev-Modus (devSkipChecks.js): weder Code ausfuehren noch Canvas/DOM pruefen -
      // validateOutput() meldet ohnehin "bestanden".
      if (DEV_SKIP_CHECKS) {
        taskFeedback.value[idx] = null;
        if (validateOutput('', tasks.value[idx]?.validation)) {
          completedTasks.value = new Set([...completedTasks.value, idx]);
          finishCheck(idx);
        }
        return;
      }
      checking.value = true;
      taskFeedback.value[idx] = null;
      await activate(idx);

      const validation = tasks.value[idx]?.validation || {};
      const result = await sandboxEl.value.run(taskCodes.value[idx]);
      if (!isMounted.value) return;

      if (!result.success) {
        taskAttempts.value[idx] = (taskAttempts.value[idx] || 0) + 1;
        const errMsg = t('editor.errorPrefix') + (result.error || t('jsLesson.unknownError'));
        taskOutputs.value[idx] = errMsg;
        taskFeedback.value[idx] = { success: false, message: errMsg };
        checking.value = false;
        return;
      }
      taskOutputs.value[idx] = await withCanvasNote(idx, result.output);

      // Canvas- und DOM-Checks laufen ausserhalb von validateOutput() - beide fragen den lebenden
      // Sandbox-Zustand per RPC ab (Pixel-Daten bzw. echtes DOM-Auslesen/Klick-Simulation), nicht
      // die Konsolen-Ausgabe. `validation.expected` bleibt fuer diese Typen bewusst leer (die
      // dom_*-Typen nutzen stattdessen `validation.text`), sonst wuerde validateOutput()s
      // Ausgabe-Fallback-Check faelschlich gegen die (meist leere) Konsolen-Ausgabe pruefen.
      let extraChecksOk = true;
      let failedHint = '';
      if (validation.type === 'canvas_not_blank') {
        extraChecksOk = await sandboxEl.value.checkCanvasNotBlank();
      } else if (validation.type === 'canvas_changed') {
        extraChecksOk = await sandboxEl.value.checkCanvasChanged(validation.ms || 400);
      } else if (validation.type === 'dom_text') {
        const text = await sandboxEl.value.checkDomText(validation.target);
        extraChecksOk = typeof text === 'string' && text.trim() === validation.text;
      } else if (validation.type === 'dom_click_text') {
        const text = await sandboxEl.value.checkDomClickText(validation.click, validation.target, validation.clicks);
        extraChecksOk = typeof text === 'string' && text.trim() === validation.text;
      } else if (validation.type === 'web') {
        const facts = await sandboxEl.value.checkWeb(validation.checks || []);
        const webResult = validateWebChecks(validation, facts);
        extraChecksOk = webResult.ok;
        failedHint = webResult.ok ? '' : validation.checks?.[webResult.failedIndex]?.hint || '';
      }
      if (!isMounted.value) return;

      const valid = extraChecksOk && validateOutput(result.output, validation);

      if (valid) {
        completedTasks.value = new Set([...completedTasks.value, idx]);
        if (skippedTasks.value.has(idx)) {
          const next = new Set(skippedTasks.value);
          next.delete(idx);
          skippedTasks.value = next;
        }
        finishCheck(idx);
      } else {
        taskAttempts.value[idx] = (taskAttempts.value[idx] || 0) + 1;
        if (taskAttempts.value[idx] < 2) {
          taskFeedback.value[idx] = { success: false, message: t('lesson.hintSoft') };
        } else if (validation.type === 'web') {
          // Web-Pruefungen haben kein `expected` - stattdessen der Hinweis der ersten Pruefung,
          // die noch nicht passt (`hint` in lessons.json).
          taskFeedback.value[idx] = { success: false, message: failedHint || t('lesson.hintSoft') };
        } else {
          taskFeedback.value[idx] = {
            success: false,
            message: t('lesson.hintExpected').replace('{expected}', validation.expected || ''),
          };
        }
      }
      checking.value = false;
    };

    const finishCheck = (idx) => {
      const total = tasks.value.length;
      const done = doneCount.value;
      if (done === total) {
        markCompleted(props.lesson.id);
        taskFeedback.value[idx] = { success: true, message: t('lesson.allTasksDone') };
      } else {
        const remaining = total - done;
        taskFeedback.value[idx] = {
          success: true,
          message: t('lesson.taskDoneRemaining').replace('{n}', idx + 1).replace('{r}', remaining),
        };
      }
    };

    // Die eigene Seite als echte .html-Datei mitnehmen - laesst sich danach per Doppelklick im
    // Browser oeffnen (Bilder aus /web-bilder/ zeigen dann auf die volle Adresse).
    const downloadTask = (idx) => {
      const blob = new Blob([webDocumentForDownload(taskCodes.value[idx])], { type: 'text/html' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'meine-website.html';
      a.click();
      URL.revokeObjectURL(url);
    };

    const goToNext = () => {
      emit('completed', props.lesson.id);
    };

    return {
      lang,
      t,
      lessonContent,
      conceptList,
      sandboxEl,
      activeIdx,
      workspaceEnabled,
      activeShowsCanvas,
      checking,
      tasks,
      isExample,
      taskShowsCanvas,
      taskCodes,
      taskOutputs,
      taskFeedback,
      taskRan,
      runTask,
      checkTask,
      goToNext,
      allTasksComplete,
      lessonSummary,
      completedTasks,
      skippedTasks,
      skipTask,
      resetTask,
      downloadTask,
      isTaskDone,
      taskAttempts,
      instructionWithGlossary,
    };
  },
};
</script>

<style scoped>
.lesson-view {
  max-width: 800px;
  margin: 0 auto;
  container-type: inline-size;
}

.lesson-view.with-workspace {
  max-width: 1320px;
}

.js-lesson-grid {
  position: relative;
}

/* Arbeitsflaeche, schmale Ansicht: Flex-Kind der Aufgabenliste, per `order` (im Template) direkt
   unter der zuletzt ausgefuehrten Aufgabe. Vor dem ersten Lauf und in reinen Konsolen-Lektionen
   unsichtbar (das Frame laeuft dort trotzdem). */
.js-workspace {
  margin: -8px 0 24px 0;
}

.js-workspace.is-empty,
.js-workspace.no-canvas,
.lesson-view:not(.with-workspace) .js-workspace,
.js-workspace-output {
  display: none;
}

.js-workspace-inner {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 12px;
}

.js-workspace-title {
  margin: 0 0 8px 0;
  font-weight: 600;
  color: var(--brand-text);
}

.js-workspace-task {
  font-weight: 400;
  color: var(--text-muted);
}

.js-workspace-hint {
  margin: 0 0 8px 0;
  font-size: 0.9em;
  color: var(--text-muted);
}

/* Breite Ansicht: rechts eine eigene Spalte ueber die ganze Lektion, die Karte darin bleibt beim
   Scrollen stehen (sticky in einem absolut positionierten, vollhohen Container). */
@container (min-width: 920px) {
  .with-workspace .js-lesson-grid {
    padding-right: 446px;
  }

  .with-workspace .js-workspace,
  .with-workspace .js-workspace.is-empty,
  .with-workspace .js-workspace.no-canvas {
    display: block;
    position: absolute;
    top: 0;
    bottom: 0;
    right: 0;
    width: 426px;
    margin: 0;
  }

  .with-workspace .js-workspace-inner {
    position: sticky;
    top: 16px;
    max-height: calc(100vh - 32px);
    overflow-y: auto;
  }

  .with-workspace .js-workspace-output {
    display: block;
    margin-bottom: 0;
  }

  .with-workspace .task-block .output-display {
    display: none;
  }

  /* Neben der Arbeitsflaeche darf der Editor die ganze linke Spalte nutzen (sonst 500px). */
  .with-workspace .code-editor-wrapper,
  .with-workspace .solution-reveal {
    max-width: none;
  }
}

.lesson-content {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 24px;
  margin-bottom: 20px;
  line-height: 1.6;
}

.lesson-loading {
  color: var(--text-muted);
  font-style: italic;
}

.lesson-content :deep(h1) {
  font-size: 1.5em;
  margin-top: 0;
  margin-bottom: 1em;
  border-bottom: 2px solid var(--accent-yellow, #fdd835);
  padding-bottom: 0.3em;
}

.lesson-content :deep(h2) {
  font-size: 1.2em;
  margin-top: 1em;
  margin-bottom: 0.5em;
}

.lesson-content :deep(code) {
  background: var(--surface-muted);
  padding: 2px 6px;
  border-radius: 3px;
  font-family: 'Courier New', monospace;
  font-size: 0.9em;
}

.lesson-content :deep(.glossary-term) {
  border-bottom: 1px dotted var(--brand-text);
  cursor: help;
}

.lesson-content :deep(.concept-link) {
  color: inherit;
  text-decoration: none;
  border-bottom: 1px dotted var(--brand-text);
}

.lesson-content :deep(.concept-link)::after {
  content: '↗';
  font-size: 0.75em;
  margin-left: 1px;
  color: var(--brand-text);
}

.lesson-content :deep(.concept-link:hover) {
  color: var(--brand-text);
}

.lesson-content :deep(pre) {
  background: var(--surface-muted);
  padding: 12px;
  border-radius: 6px;
  overflow-x: auto;
}

.lesson-editor-section {
  display: flex;
  flex-direction: column;
  background: var(--surface-muted);
  border: 2px solid var(--brand-text);
  border-radius: 8px;
  padding: 20px;
}

.editor-hint {
  margin: 0 0 12px 0;
  font-size: 0.9em;
  color: var(--text-muted);
}

.editor-hint-ran {
  color: var(--brand-text);
}

.task-block {
  margin-bottom: 24px;
  padding-bottom: 24px;
  padding-left: 14px;
  border-bottom: 1px solid var(--border);
  border-left: 4px solid transparent;
}

.task-block.task-required {
  border-left-color: var(--accent-orange, #ff9800);
}

.task-block.task-example {
  border-left-color: var(--border-strong);
}

.task-block:last-child {
  margin-bottom: 0;
  padding-bottom: 0;
  border-bottom: none;
}

.task-badge {
  display: inline-block;
  margin-bottom: 6px;
  padding: 2px 10px;
  border-radius: 12px;
  font-size: 0.72em;
  font-weight: 700;
  letter-spacing: 0.03em;
  text-transform: uppercase;
}

.badge-example {
  background: var(--surface-muted);
  color: var(--text-faint);
}

.badge-required {
  background: var(--warning-bg);
  color: var(--accent-orange, #fb8c00);
}

.task-instruction {
  display: block;
  font-weight: 600;
  color: var(--brand-text);
  margin: 0 0 8px 0;
  font-size: 0.95em;
  line-height: 1.4;
}

.task-done {
  color: var(--success);
  margin-right: 6px;
}

.task-pending {
  color: var(--text-faint);
  margin-right: 6px;
}

.task-skipped {
  color: #d9822b;
  margin-right: 6px;
}

.task-status-label {
  font-weight: 400;
  color: var(--text-muted);
  font-size: 0.9em;
}

.lesson-complete-box {
  margin-top: 24px;
  padding: 20px;
  background: var(--success-bg);
  border: 1px solid var(--success-border);
  border-radius: 8px;
}

.lesson-summary {
  margin: 0 0 16px 0;
  font-size: 1.05em;
  color: var(--success-text);
  font-weight: 500;
}

.btn-next {
  background: var(--primary-purple, #4a2274);
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 6px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
}

.btn-next:hover {
  background: #3d1b5c;
}

a.btn-next {
  display: inline-block;
  text-decoration: none;
  text-align: center;
}

.code-editor-wrapper {
  max-width: 500px;
  border-radius: 8px;
  transition: box-shadow 0.15s, border-color 0.15s;
}

/* Rahmen zeigt: dieser Code wurde schon mindestens einmal ausgefuehrt (siehe jsLesson.ranExplainer
   oben in der Lektion) - unabhaengig davon, ob die Aufgabe schon bestanden ist. */
.code-editor-wrapper.code-editor-ran :deep(.cm-host) {
  border-color: var(--accent-orange, #ff9800);
  box-shadow: 0 0 0 2px rgba(255, 152, 0, 0.2);
}

.meine-seite-note {
  margin: 0 0 8px 0;
  padding: 6px 10px;
  background: var(--warning-bg);
  border: 1px solid #ffe082;
  border-radius: 6px;
  font-size: 0.85em;
  color: #6d4c00;
}

.code-ran-note {
  margin: -6px 0 12px 0;
  font-size: 0.82em;
  color: var(--accent-orange, #fb8c00);
  font-weight: 600;
}

.solution-reveal {
  max-width: 500px;
  margin: 0 0 12px 0;
  border: 1px dashed var(--border-tint);
  border-radius: 6px;
  background: var(--surface-tint);
}

.solution-reveal summary {
  cursor: pointer;
  padding: 8px 12px;
  font-weight: 600;
  font-size: 0.85em;
  color: var(--brand-text);
  user-select: none;
}

.solution-code {
  margin: 0;
  padding: 0 12px 12px 12px;
  font-family: 'Courier New', Consolas, Monaco, monospace;
  font-size: 0.85em;
  white-space: pre-wrap;
  word-break: break-word;
  color: var(--text);
}

.editor-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  align-items: center;
  margin-bottom: 12px;
}

.btn-run {
  background: #6c757d;
  color: white;
  border: none;
  padding: 10px 24px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 16px;
  font-weight: 600;
}

.btn-run:hover:not(:disabled) {
  background: #5a6268;
}

.btn-run:disabled {
  background: #adb5bd;
  cursor: not-allowed;
  opacity: 0.6;
}

.btn-check {
  background: var(--accent-orange, #ff9800);
  color: white;
  border: none;
  padding: 10px 24px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 16px;
  font-weight: 600;
}

.btn-check:hover:not(:disabled) {
  background: #fb8c00;
}

.btn-check:disabled {
  background: #6c757d;
  cursor: not-allowed;
  opacity: 0.6;
}

.btn-skip {
  background: transparent;
  color: var(--text-muted);
  border: 1px solid var(--border);
  padding: 10px 20px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 15px;
}

.btn-skip:hover:not(:disabled) {
  background: var(--surface-muted);
  border-color: var(--border-strong);
}

.btn-skip:disabled {
  cursor: not-allowed;
  opacity: 0.6;
}

.btn-reset {
  background: transparent;
  color: var(--text-muted);
  border: 1px solid var(--border);
  padding: 10px 20px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 15px;
}

.btn-reset:hover:not(:disabled) {
  background: var(--surface-muted);
  border-color: var(--border-strong);
}

.btn-reset:disabled {
  cursor: not-allowed;
  opacity: 0.6;
}

.output-display {
  margin-top: 12px;
  padding: 12px;
  background: var(--surface-muted);
  border: 1px solid var(--border);
  border-radius: 6px;
  margin-bottom: 12px;
}

.output-display strong {
  display: block;
  margin-bottom: 8px;
  font-size: 0.9em;
  color: var(--text-muted);
}

.output-content {
  margin: 0;
  font-family: 'Courier New', Consolas, Monaco, monospace;
  font-size: 14px;
  white-space: pre-wrap;
  word-break: break-word;
}

.feedback {
  padding: 12px 16px;
  border-radius: 6px;
  font-weight: 500;
}

.feedback-success {
  background: var(--success-bg);
  color: var(--success-text);
  border: 1px solid var(--success-border);
}

.feedback-error {
  background: var(--danger-bg);
  color: var(--danger-text);
  border: 1px solid var(--danger-border);
}
</style>
