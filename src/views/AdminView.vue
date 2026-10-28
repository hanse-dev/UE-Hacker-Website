<template>
  <section class="admin-page">
    <h1>{{ t('admin.title') }}</h1>
    <p class="admin-intro">{{ t('admin.intro') }}</p>

    <form v-if="!token" class="admin-login-card" @submit.prevent="login">
      <input
        type="text"
        name="username"
        autocomplete="username"
        value="admin"
        hidden
        readonly
      >
      <label class="field">
        <span>{{ t('admin.adminPassword') }}</span>
        <input
          v-model="password"
          type="password"
          name="password"
          autocomplete="current-password"
        >
      </label>
      <p v-if="error" class="error">{{ error }}</p>
      <button type="submit" class="btn-primary" :disabled="busy">
        {{ busy ? t('admin.working') : t('admin.login') }}
      </button>
    </form>

    <template v-else>
      <div class="admin-tabs">
        <button
          type="button"
          class="admin-tab"
          :class="{ active: activeTab === 'users' }"
          @click="activeTab = 'users'"
        >{{ t('admin.tab.users') }}</button>
        <button
          type="button"
          class="admin-tab"
          :class="{ active: activeTab === 'termine' }"
          @click="activeTab = 'termine'"
        >{{ t('admin.tab.termine') }}</button>
        <button
          type="button"
          class="admin-tab"
          :class="{ active: activeTab === 'kurse' }"
          @click="activeTab = 'kurse'"
        >{{ t('admin.tab.kurse') }}</button>
        <button
          type="button"
          class="admin-tab"
          :class="{ active: activeTab === 'stats' }"
          @click="activeTab = 'stats'"
        >{{ t('admin.tab.stats') }}</button>
      </div>

      <section v-if="activeTab === 'users'">
        <div class="admin-toolbar">
          <button type="button" class="btn-secondary" @click="logout">{{ t('admin.logout') }}</button>
          <button type="button" class="btn-primary" @click="openCreate">{{ t('admin.create') }}</button>
        </div>

        <p v-if="error" class="error">{{ error }}</p>
        <p v-if="busy && !users.length" class="muted">{{ t('admin.loading') }}</p>

        <div v-if="resetResult" class="reset-result" role="status">
          <p>
            {{ t('admin.resetResult').replace('{name}', resetResult.username) }}
            <strong class="temp-password">{{ resetResult.password }}</strong>
          </p>
          <p class="muted">{{ t('admin.resetResultHint') }}</p>
          <button type="button" class="btn-link" @click="resetResult = null">{{ t('admin.resetResultClose') }}</button>
        </div>

        <div v-if="grantResult" class="reset-result grant-result" role="status">
          <p>{{ t('admin.grantResult').replace('{course}', grantResult.course).replace('{name}', grantResult.username) }}</p>
          <button type="button" class="btn-link" @click="grantResult = null">{{ t('admin.resetResultClose') }}</button>
        </div>

        <table v-if="users.length" class="admin-table">
          <thead>
            <tr>
              <th>{{ t('admin.col.username') }}</th>
              <th>{{ t('admin.col.age') }}</th>
              <th>{{ t('admin.col.updated') }}</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="u in users" :key="u.id">
              <td>
                {{ u.username }}
                <span v-if="u.mustChangePassword" class="must-change-badge">{{ t('admin.mustChange') }}</span>
              </td>
              <td>{{ ageLabel(u.ageGroup) }}</td>
              <td>{{ formatDate(u.updatedAt) }}</td>
              <td class="actions">
                <button type="button" class="btn-link" @click="openEdit(u)">{{ t('admin.edit') }}</button>
                <button type="button" class="btn-link reset-password-btn" @click="resetPassword(u)">{{ t('admin.resetPassword') }}</button>
                <button type="button" class="btn-link grant-project-btn" @click="openGrant(u)">{{ t('admin.grant') }}</button>
                <button type="button" class="btn-link danger" @click="remove(u)">{{ t('admin.delete') }}</button>
              </td>
            </tr>
          </tbody>
        </table>
        <p v-else-if="!busy" class="muted">{{ t('admin.empty') }}</p>
      </section>

      <section v-else-if="activeTab === 'termine'" class="admin-termine">
        <div class="admin-toolbar">
          <button type="button" class="btn-secondary" @click="logout">{{ t('admin.logout') }}</button>
          <button type="button" class="btn-primary" @click="openCreateTermin">{{ t('admin.termine.create') }}</button>
        </div>

        <p v-if="terminError" class="error">{{ terminError }}</p>
        <p v-if="terminBusy && !termine.length" class="muted">{{ t('admin.termine.loading') }}</p>

        <table v-if="termine.length" class="admin-table">
          <thead>
            <tr>
              <th>{{ t('admin.termine.col.date') }}</th>
              <th>{{ t('admin.termine.col.topic') }}</th>
              <th>{{ t('admin.termine.col.location') }}</th>
              <th>{{ t('admin.termine.col.status') }}</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="terminItem in termine" :key="terminItem.id">
              <td>{{ terminItem.date }}<br><small>{{ terminItem.time }}</small></td>
              <td>{{ terminItem.topic }}</td>
              <td>{{ terminItem.location }}</td>
              <td>
                <span v-if="terminItem.cancelled" class="badge badge-cancelled">{{ t('admin.termine.cancelled') }}</span>
                <span v-if="terminItem.recurring" class="badge badge-recurring">{{ t('admin.termine.recurring') }}</span>
              </td>
              <td class="actions">
                <button type="button" class="btn-link" @click="openEditTermin(terminItem)">{{ t('admin.edit') }}</button>
                <button type="button" class="btn-link danger" @click="removeTermin(terminItem)">{{ t('admin.delete') }}</button>
              </td>
            </tr>
          </tbody>
        </table>
        <p v-else-if="!terminBusy" class="muted">{{ t('admin.termine.empty') }}</p>
      </section>

      <AdminStolperstellen v-else-if="activeTab === 'stats'" />

      <!-- Nur Anzeige aus kurse.json, keine API: welche Kurse noch nicht verlinkt oder Beta sind. -->
      <section v-else class="admin-kurse">
        <div class="admin-toolbar">
          <button type="button" class="btn-secondary" @click="logout">{{ t('admin.logout') }}</button>
        </div>
        <p class="muted">{{ t('admin.kurse.hint') }}</p>
        <table class="admin-table">
          <thead>
            <tr>
              <th>{{ t('admin.kurse.col.title') }}</th>
              <th>{{ t('admin.kurse.col.status') }}</th>
              <th>{{ t('admin.kurse.col.link') }}</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="kurs in adminKurse" :key="kurs.id" :data-kurs="kurs.id">
              <td>{{ kurs.title }}</td>
              <td>
                <span v-if="kurs.unlisted" class="badge badge-unlisted">{{ t('admin.kurse.unlisted') }}</span>
                <BetaBadge v-if="kurs.beta" />
              </td>
              <td><router-link :to="`/kurs/${kurs.id}`" target="_blank">/kurs/{{ kurs.id }}</router-link></td>
            </tr>
          </tbody>
        </table>
      </section>

      <div v-if="formOpen" class="modal-backdrop" @click.self="closeForm">
        <div class="modal-card" role="dialog" aria-modal="true">
          <h2>{{ editing ? t('admin.editTitle') : t('admin.createTitle') }}</h2>
          <label class="field">
            <span>{{ t('admin.col.username') }}</span>
            <input v-model="form.username" autocomplete="off">
          </label>
          <label class="field">
            <span>{{ t('admin.col.age') }}</span>
            <select v-model="form.ageGroup">
              <option value="kinder">{{ t('admin.age.kinder') }}</option>
              <option value="jugendliche">{{ t('admin.age.jugendliche') }}</option>
            </select>
          </label>
          <label class="field">
            <span>{{ editing ? t('admin.passwordOptional') : t('admin.password') }}</span>
            <input v-model="form.password" type="password" autocomplete="new-password">
          </label>
          <p v-if="formError" class="error">{{ formError }}</p>
          <div class="modal-actions">
            <button type="button" class="btn-secondary" @click="closeForm">{{ t('admin.cancel') }}</button>
            <button type="button" class="btn-primary" :disabled="busy" @click="save">
              {{ busy ? t('admin.working') : t('admin.save') }}
            </button>
          </div>
        </div>
      </div>

      <div v-if="grantUser" class="modal-backdrop" @click.self="closeGrant">
        <div class="modal-card grant-modal" role="dialog" aria-modal="true">
          <h2>{{ t('admin.grantTitle').replace('{name}', grantUser.username) }}</h2>
          <p class="muted">{{ t('admin.grantHint') }}</p>
          <label class="field">
            <span>{{ t('admin.grantCourse') }}</span>
            <select v-model="grantCourseId" class="grant-course">
              <option v-for="p in projects" :key="p.id" :value="p.id">{{ p.title }}</option>
            </select>
          </label>
          <p v-if="grantError" class="error">{{ grantError }}</p>
          <div class="modal-actions">
            <button type="button" class="btn-secondary" @click="closeGrant">{{ t('admin.cancel') }}</button>
            <button type="button" class="btn-primary grant-submit" :disabled="busy || !grantCourseId" @click="grant">
              {{ busy ? t('admin.working') : t('admin.grantSubmit') }}
            </button>
          </div>
        </div>
      </div>

      <div v-if="terminFormOpen" class="modal-backdrop" @click.self="closeTerminForm">
        <div class="modal-card" role="dialog" aria-modal="true">
          <h2>{{ editingTermin ? t('admin.termine.editTitle') : t('admin.termine.createTitle') }}</h2>
          <label class="field">
            <span>{{ t('admin.termine.course') }}</span>
            <select v-model="terminForm.auswahl" class="termin-auswahl" @change="onTerminAuswahl">
              <option :value="WERKSTATT">{{ t('admin.termine.werkstatt') }}</option>
              <optgroup :label="t('admin.termine.groupCourses')">
                <option v-for="k in terminKurse.kurse" :key="k.id" :value="k.id">{{ k.title }}</option>
              </optgroup>
              <optgroup :label="t('admin.termine.groupProjects')">
                <option v-for="k in terminKurse.projekte" :key="k.id" :value="k.id">{{ k.title }}</option>
              </optgroup>
              <option :value="EIGENER_LINK">{{ t('admin.termine.ownLink') }}</option>
            </select>
          </label>
          <p v-if="terminForm.vorgeschlagen" class="muted termin-vorschlag">{{ t('admin.termine.suggestion') }}</p>
          <label v-if="terminForm.auswahl === WOCHEN_KURS" class="field">
            <span>{{ t('admin.termine.week') }}</span>
            <select v-model="terminForm.woche" class="termin-woche" @change="onTerminAuswahl">
              <option :value="null">{{ t('admin.termine.noWeek') }}</option>
              <option v-for="w in WOCHEN" :key="w.nr" :value="w.nr">{{ wochenTopic(w.nr) }}</option>
            </select>
          </label>
          <label class="field">
            <span>{{ t('admin.termine.col.topic') }}</span>
            <input v-model="terminForm.topic" class="termin-topic" autocomplete="off">
          </label>
          <label v-if="terminForm.auswahl === EIGENER_LINK" class="field">
            <span>{{ t('admin.termine.link') }}</span>
            <input v-model="terminForm.link" class="termin-link-input" autocomplete="off" placeholder="/kurs/python-12-wochen-grundkurs">
          </label>
          <label class="field field-checkbox">
            <input v-model="terminForm.recurring" type="checkbox" class="termin-recurring">
            <span>{{ t('admin.termine.recurring') }}</span>
          </label>
          <label v-if="!terminForm.recurring" class="field">
            <span>{{ t('admin.termine.col.date') }}</span>
            <input v-model="terminForm.dateIso" type="date" class="termin-datum">
          </label>
          <template v-else>
            <label class="field">
              <span>{{ t('admin.termine.validFrom') }}</span>
              <input v-model="terminForm.validFrom" type="date" class="termin-valid-from">
            </label>
            <label class="field">
              <span>{{ t('admin.termine.validUntil') }}</span>
              <input v-model="terminForm.validUntil" type="date">
            </label>
          </template>
          <div class="field-row">
            <label class="field">
              <span>{{ t('admin.termine.from') }}</span>
              <input v-model="terminForm.start" type="time" class="termin-start">
            </label>
            <label class="field">
              <span>{{ t('admin.termine.until') }}</span>
              <input v-model="terminForm.end" type="time" class="termin-end">
            </label>
          </div>
          <label class="field">
            <span>{{ t('admin.termine.col.location') }}</span>
            <select v-model="terminForm.ort" class="termin-ort">
              <option v-for="o in terminOrte" :key="o.id" :value="o.name">{{ o.name }}</option>
              <option :value="NEUER_ORT">{{ t('admin.termine.newPlace') }}</option>
            </select>
          </label>
          <label v-if="terminForm.ort === NEUER_ORT" class="field">
            <span>{{ t('admin.termine.newPlaceName') }}</span>
            <input v-model="terminForm.neuerOrt" class="termin-neuer-ort" autocomplete="off">
          </label>
          <button
            v-else-if="selectedOrt"
            type="button"
            class="btn-link danger termin-ort-entfernen"
            @click="removeTerminOrt(selectedOrt)"
          >{{ t('admin.termine.removePlace') }}</button>
          <p class="muted termin-preview">{{ terminPreview }}</p>
          <label class="field field-checkbox">
            <input v-model="terminForm.cancelled" type="checkbox" class="termin-cancelled">
            <span>{{ t('admin.termine.cancelled') }}</span>
          </label>
          <p v-if="terminFormError" class="error">{{ terminFormError }}</p>
          <div class="modal-actions">
            <button type="button" class="btn-secondary" @click="closeTerminForm">{{ t('admin.cancel') }}</button>
            <button type="button" class="btn-primary" :disabled="terminBusy" @click="saveTermin">
              {{ terminBusy ? t('admin.working') : t('admin.save') }}
            </button>
          </div>
        </div>
      </div>
    </template>
  </section>
</template>

<script>
import { ref, computed, onMounted } from 'vue';
import { useLanguage } from '../composables/useLanguage.js';
import { assetUrl } from '../utils/assetUrl';
import BetaBadge from '../components/BetaBadge.vue';
import AdminStolperstellen from '../components/AdminStolperstellen.vue';
import { DEV_SKIP_CHECKS } from '../composables/devSkipChecks.js';
import {
  adminToken as token,
  setAdminToken,
  adminLogin,
  adminDevLogin,
  listUsers,
  createUser,
  updateUser,
  resetUserPassword,
  grantProject,
  deleteUser,
  listTermine,
  createTermin,
  updateTermin,
  deleteTermin,
  listTerminOrte,
  deleteTerminOrt,
} from '../composables/useAdminApi.js';
import {
  WOCHEN,
  WOCHEN_KURS,
  WERKSTATT,
  EIGENER_LINK,
  NEUER_ORT,
  wochenTopic,
  terminKursOptionen,
  neuesTerminForm,
  terminFormAus,
  terminPayload,
  topicFuer,
  linkFuer,
} from '../composables/useTerminForm.js';
import { completedCourseEntry } from '../composables/useInteractiveProgress.js';

// Gleiches Wildcard-Glob wie useProjectBadges.js: Die Lektions-IDs eines Projekt-Kurses kennt nur
// das Frontend, der Server bekommt sie für die Gutschrift geschickt.
const lessonJsonModules = import.meta.glob('../../content/*/lessons.json');

export default {
  name: 'AdminView',
  components: { BetaBadge, AdminStolperstellen },
  setup() {
    const { t, lang } = useLanguage();
    const password = ref('');
    const users = ref([]);
    // Einmal-Passwort nach einem Reset — nur im Speicher, verschwindet beim Ausblenden/Neuladen.
    const resetResult = ref(null);
    const busy = ref(false);
    const error = ref('');
    const formOpen = ref(false);
    const formError = ref('');
    const editing = ref(null);
    const form = ref({ username: '', ageGroup: 'kinder', password: '' });

    // Projekt gutschreiben: Liste der Projekt-Kurse wird beim ersten Öffnen geladen.
    const projects = ref([]);
    const grantUser = ref(null);
    const grantCourseId = ref('');
    const grantError = ref('');
    const grantResult = ref(null);

    const activeTab = ref('users');
    const termine = ref([]);
    const terminBusy = ref(false);
    const terminError = ref('');
    const terminFormOpen = ref(false);
    const terminFormError = ref('');
    const editingTermin = ref(null);
    const terminForm = ref(neuesTerminForm([]));
    const terminOrte = ref([]);
    const terminKurse = computed(() => terminKursOptionen(adminKurse.value));
    const selectedOrt = computed(() => terminOrte.value.find((o) => o.name === terminForm.value.ort) || null);
    const terminPreview = computed(() => {
      const p = terminPayload(terminForm.value);
      return [p.date, p.time, p.location].filter(Boolean).join(' · ');
    });

    const fillTopicAndLink = () => {
      const f = terminForm.value;
      if (f.auswahl === EIGENER_LINK) return;
      f.topic = topicFuer(f, adminKurse.value);
      f.link = linkFuer(f);
    };
    const onTerminAuswahl = () => {
      terminForm.value.vorgeschlagen = false;
      if (terminForm.value.auswahl !== WOCHEN_KURS) terminForm.value.woche = null;
      fillTopicAndLink();
    };

    const refreshTerminOrte = async () => {
      try {
        terminOrte.value = (await listTerminOrte()).orte || [];
      } catch (e) {
        terminFormError.value = e.message || t('admin.error');
      }
    };

    const removeTerminOrt = async (ort) => {
      const ok = window.confirm(t('admin.termine.confirmRemovePlace').replace('{name}', ort.name));
      if (!ok) return;
      try {
        await deleteTerminOrt(ort.id);
        await refreshTerminOrte();
        terminForm.value.ort = terminOrte.value[0]?.name || NEUER_ORT;
      } catch (e) {
        terminFormError.value = e.message || t('admin.error');
      }
    };

    const ageLabel = (g) => (g === 'jugendliche' ? t('admin.age.jugendliche') : t('admin.age.kinder'));

    const formatDate = (iso) => {
      if (!iso) return '—';
      try {
        return new Date(iso).toLocaleString(lang.value === 'en' ? 'en-GB' : 'de-DE');
      } catch {
        return iso;
      }
    };

    const refresh = async () => {
      if (!token.value) return;
      busy.value = true;
      error.value = '';
      try {
        const data = await listUsers();
        users.value = data.users || [];
      } catch (e) {
        if (e.status === 401) {
          setAdminToken('');
        }
        error.value = e.message || t('admin.error');
      } finally {
        busy.value = false;
      }
    };

    const refreshTermine = async () => {
      if (!token.value) return;
      terminBusy.value = true;
      terminError.value = '';
      try {
        const data = await listTermine();
        termine.value = data.termine || [];
      } catch (e) {
        if (e.status === 401) {
          setAdminToken('');
        }
        terminError.value = e.message || t('admin.error');
      } finally {
        terminBusy.value = false;
      }
    };

    const login = async () => {
      busy.value = true;
      error.value = '';
      try {
        const data = await adminLogin(password.value);
        setAdminToken(data.token);
        password.value = '';
        await Promise.all([refresh(), refreshTermine()]);
      } catch (e) {
        error.value = e.message || t('admin.error');
      } finally {
        busy.value = false;
      }
    };

    const logout = () => {
      setAdminToken('');
      users.value = [];
      resetResult.value = null;
      termine.value = [];
    };

    const openCreate = () => {
      editing.value = null;
      form.value = { username: '', ageGroup: 'kinder', password: '' };
      formError.value = '';
      formOpen.value = true;
    };

    const openEdit = (u) => {
      editing.value = u;
      form.value = { username: u.username, ageGroup: u.ageGroup, password: '' };
      formError.value = '';
      formOpen.value = true;
    };

    const closeForm = () => {
      formOpen.value = false;
      formError.value = '';
    };

    const save = async () => {
      busy.value = true;
      formError.value = '';
      try {
        if (editing.value) {
          const payload = {
            username: form.value.username,
            ageGroup: form.value.ageGroup,
          };
          if (form.value.password) payload.password = form.value.password;
          await updateUser(editing.value.id, payload);
        } else {
          await createUser({
            username: form.value.username,
            ageGroup: form.value.ageGroup,
            password: form.value.password,
          });
        }
        closeForm();
        await refresh();
      } catch (e) {
        formError.value = e.message || t('admin.error');
      } finally {
        busy.value = false;
      }
    };

    const remove = async (u) => {
      const ok = window.confirm(t('admin.confirmDelete').replace('{name}', u.username));
      if (!ok) return;
      busy.value = true;
      error.value = '';
      try {
        await deleteUser(u.id);
        await refresh();
      } catch (e) {
        error.value = e.message || t('admin.error');
      } finally {
        busy.value = false;
      }
    };

    const openGrant = async (u) => {
      grantError.value = '';
      grantResult.value = null;
      grantUser.value = u;
      if (projects.value.length) return;
      try {
        const kurse = await (await fetch(assetUrl('kurse.json'))).json();
        projects.value = kurse.filter((k) => k.type === 'projekt');
        grantCourseId.value = projects.value[0]?.id || '';
      } catch (e) {
        grantError.value = e.message || t('admin.error');
      }
    };

    const closeGrant = () => {
      grantUser.value = null;
      grantError.value = '';
    };

    const grant = async () => {
      const course = projects.value.find((p) => p.id === grantCourseId.value);
      if (!course || !grantUser.value) return;
      busy.value = true;
      grantError.value = '';
      try {
        const loader = lessonJsonModules[`../../content/${course.contentPath}/lessons.json`];
        const lessons = loader ? (await loader()).default || [] : [];
        if (!lessons.length) throw new Error(t('admin.error'));
        const { key, value } = completedCourseEntry(course.contentPath, course.id, lessons.map((l) => l.id));
        await grantProject(grantUser.value.id, key, value);
        grantResult.value = { username: grantUser.value.username, course: course.title };
        closeGrant();
      } catch (e) {
        grantError.value = e.message || t('admin.error');
      } finally {
        busy.value = false;
      }
    };

    const resetPassword = async (u) => {
      const ok = window.confirm(t('admin.confirmReset').replace('{name}', u.username));
      if (!ok) return;
      busy.value = true;
      error.value = '';
      resetResult.value = null;
      try {
        const data = await resetUserPassword(u.id);
        resetResult.value = { username: u.username, password: data.temporaryPassword };
        await refresh();
      } catch (e) {
        error.value = e.message || t('admin.error');
      } finally {
        busy.value = false;
      }
    };

    // Ein Ort, der nicht (mehr) in der Liste steht, erscheint als „Neuer Ort“ mit vorausgefülltem Namen.
    const applyOrt = () => {
      const f = terminForm.value;
      if (!f.ort && terminOrte.value.length) f.ort = terminOrte.value[0].name;
      if (f.ort && f.ort !== NEUER_ORT && !terminOrte.value.some((o) => o.name === f.ort)) {
        f.neuerOrt = f.ort;
        f.ort = NEUER_ORT;
      }
      if (!f.ort) f.ort = NEUER_ORT;
    };

    const openCreateTermin = async () => {
      editingTermin.value = null;
      terminFormError.value = '';
      await refreshTerminOrte();
      terminForm.value = neuesTerminForm(termine.value);
      fillTopicAndLink();
      applyOrt();
      terminFormOpen.value = true;
    };

    const openEditTermin = async (terminItem) => {
      editingTermin.value = terminItem;
      terminFormError.value = '';
      await refreshTerminOrte();
      terminForm.value = terminFormAus(terminItem, adminKurse.value);
      applyOrt();
      terminFormOpen.value = true;
    };

    const closeTerminForm = () => {
      terminFormOpen.value = false;
      terminFormError.value = '';
    };

    const saveTermin = async () => {
      terminBusy.value = true;
      terminFormError.value = '';
      try {
        const payload = terminPayload(terminForm.value);
        if (!payload.date) throw new Error(t('admin.termine.dateMissing'));
        if (!terminForm.value.start) throw new Error(t('admin.termine.timeMissing'));
        if (editingTermin.value) {
          await updateTermin(editingTermin.value.id, payload);
        } else {
          await createTermin(payload);
        }
        closeTerminForm();
        await refreshTermine();
      } catch (e) {
        terminFormError.value = e.message || t('admin.error');
      } finally {
        terminBusy.value = false;
      }
    };

    const removeTermin = async (terminItem) => {
      const ok = window.confirm(t('admin.termine.confirmDelete').replace('{topic}', terminItem.topic));
      if (!ok) return;
      terminBusy.value = true;
      terminError.value = '';
      try {
        await deleteTermin(terminItem.id);
        await refreshTermine();
      } catch (e) {
        terminError.value = e.message || t('admin.error');
      } finally {
        terminBusy.value = false;
      }
    };

    // Alle Kurse, die nicht verlinkten zuerst (sonst Reihenfolge wie in kurse.json).
    const adminKurse = ref([]);
    const loadKurse = async () => {
      try {
        const response = await fetch(assetUrl('kurse.json'));
        const kurse = await response.json();
        adminKurse.value = [...kurse.filter((k) => k.unlisted), ...kurse.filter((k) => !k.unlisted)];
      } catch (e) {
        console.error('Could not load kurse:', e);
      }
    };

    // Dev-Modus (npm run dev:skip-checks): ohne Passwort anmelden. Laeuft die API ohne
    // DEV_SKIP_ADMIN_LOGIN=1, schlaegt das fehl und es bleibt beim normalen Login-Formular.
    const devLogin = async () => {
      if (!DEV_SKIP_CHECKS || token.value) return;
      try {
        const data = await adminDevLogin();
        setAdminToken(data.token);
      } catch {
        /* normales Login-Formular */
      }
    };

    onMounted(async () => {
      await devLogin();
      await Promise.all([refresh(), refreshTermine(), loadKurse()]);
    });

    return {
      t, token, password, users, busy, error, formOpen, formError, editing, form,
      ageLabel, formatDate, login, logout, openCreate, openEdit, closeForm, save, remove,
      resetPassword, resetResult,
      projects, grantUser, grantCourseId, grantError, grantResult, openGrant, closeGrant, grant,
      activeTab, termine, terminBusy, terminError, terminFormOpen, terminFormError, editingTermin, terminForm,
      openCreateTermin, openEditTermin, closeTerminForm, saveTermin, removeTermin,
      terminOrte, terminKurse, selectedOrt, terminPreview, onTerminAuswahl, removeTerminOrt,
      WOCHEN, WOCHEN_KURS, WERKSTATT, EIGENER_LINK, NEUER_ORT, wochenTopic,
      adminKurse,
    };
  },
};
</script>

<style scoped>
.admin-page {
  max-width: 900px;
  margin: 0 auto;
  padding: 24px 20px 48px;
}

.admin-intro {
  color: var(--text-muted);
  margin: 0 0 20px;
}

.admin-login-card,
.modal-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 20px;
  max-width: 420px;
  max-height: calc(100vh - 32px);
  overflow-y: auto;
}

.field {
  display: flex;
  flex-direction: column;
  gap: 6px;
  margin-bottom: 14px;
}

.field input,
.field select {
  padding: 10px 12px;
  border: 1px solid var(--border-strong);
  border-radius: 6px;
  font-size: 1em;
}

.admin-toolbar {
  display: flex;
  gap: 10px;
  margin-bottom: 16px;
}

.admin-tabs {
  display: flex;
  gap: 4px;
  margin-bottom: 16px;
  border-bottom: 1px solid var(--border);
}

.admin-tab {
  border: none;
  background: none;
  padding: 10px 16px;
  font-weight: 600;
  color: var(--text-muted);
  cursor: pointer;
  border-bottom: 2px solid transparent;
}

.admin-tab.active {
  color: var(--brand-text);
  border-bottom-color: var(--brand-text);
}

.field-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}

.termin-vorschlag {
  margin: -8px 0 14px;
  font-size: 0.9em;
}

.termin-ort-entfernen {
  margin: -6px 0 14px;
  padding: 0;
}

.termin-preview {
  margin: 0 0 14px;
  font-weight: 600;
}

.field-checkbox {
  flex-direction: row;
  align-items: center;
  gap: 8px;
}

.field-checkbox input {
  width: auto;
}

.badge {
  display: inline-block;
  font-size: 0.8em;
  font-weight: 600;
  padding: 2px 8px;
  border-radius: 999px;
  margin-right: 6px;
}

.badge-cancelled {
  background: var(--danger-bg);
  color: var(--danger-text);
}

.badge-unlisted {
  background: var(--surface-muted);
  color: var(--text-muted);
  margin-right: 6px;
}

.badge-recurring {
  background: #eaf3fd;
  color: #1a5fb4;
}

.btn-primary,
.btn-secondary {
  border: none;
  border-radius: 6px;
  padding: 10px 16px;
  font-weight: 600;
  cursor: pointer;
}

.btn-primary {
  background: var(--primary-purple, #4a2274);
  color: #fff;
}

.btn-secondary {
  background: var(--surface-muted);
  color: var(--text);
}

.btn-primary:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.admin-table {
  width: 100%;
  border-collapse: collapse;
  background: var(--surface);
}

.admin-table th,
.admin-table td {
  text-align: left;
  padding: 10px 12px;
  border-bottom: 1px solid var(--border);
}

.actions {
  white-space: nowrap;
}

.btn-link {
  background: none;
  border: none;
  color: var(--brand-text);
  cursor: pointer;
  font-weight: 600;
  margin-right: 10px;
  padding: 0;
}

.btn-link.danger {
  color: var(--danger-text);
}

.error {
  color: var(--danger-text);
  background: var(--danger-bg);
  padding: 8px 10px;
  border-radius: 6px;
}

.muted {
  color: var(--text-muted);
}

.reset-result {
  background: #eef7ee;
  border: 1px solid #b7dfb9;
  border-radius: 6px;
  padding: 10px 12px;
  margin-bottom: 14px;
}

.reset-result p {
  margin: 0 0 6px;
}

.temp-password {
  font-family: monospace;
  font-size: 1.25em;
  margin-left: 6px;
  user-select: all;
}

.must-change-badge {
  display: inline-block;
  margin-left: 6px;
  padding: 1px 6px;
  border-radius: 10px;
  background: var(--warning-bg);
  color: var(--warning-text);
  font-size: 0.78em;
  font-weight: 600;
}

.modal-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.4);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 16px;
}

.modal-actions {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  margin-top: 8px;
}
</style>
