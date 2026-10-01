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
      </div>

      <section v-if="activeTab === 'users'">
        <div class="admin-toolbar">
          <button type="button" class="btn-secondary" @click="logout">{{ t('admin.logout') }}</button>
          <button type="button" class="btn-primary" @click="openCreate">{{ t('admin.create') }}</button>
        </div>

        <p v-if="error" class="error">{{ error }}</p>
        <p v-if="busy && !users.length" class="muted">{{ t('admin.loading') }}</p>

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
              <td>{{ u.username }}</td>
              <td>{{ ageLabel(u.ageGroup) }}</td>
              <td>{{ formatDate(u.updatedAt) }}</td>
              <td class="actions">
                <button type="button" class="btn-link" @click="openEdit(u)">{{ t('admin.edit') }}</button>
                <button type="button" class="btn-link danger" @click="remove(u)">{{ t('admin.delete') }}</button>
              </td>
            </tr>
          </tbody>
        </table>
        <p v-else-if="!busy" class="muted">{{ t('admin.empty') }}</p>
      </section>

      <section v-else class="admin-termine">
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

      <div v-if="terminFormOpen" class="modal-backdrop" @click.self="closeTerminForm">
        <div class="modal-card" role="dialog" aria-modal="true">
          <h2>{{ editingTermin ? t('admin.termine.editTitle') : t('admin.termine.createTitle') }}</h2>
          <label class="field">
            <span>{{ t('admin.termine.col.date') }}</span>
            <input v-model="terminForm.date" autocomplete="off" :placeholder="t('admin.termine.datePlaceholder')">
          </label>
          <label class="field">
            <span>{{ t('admin.termine.time') }}</span>
            <input v-model="terminForm.time" autocomplete="off" placeholder="17:30 - 18:30 Uhr">
          </label>
          <label class="field">
            <span>{{ t('admin.termine.col.location') }}</span>
            <input v-model="terminForm.location" autocomplete="off">
          </label>
          <label class="field">
            <span>{{ t('admin.termine.col.topic') }}</span>
            <input v-model="terminForm.topic" autocomplete="off">
          </label>
          <label class="field">
            <span>{{ t('admin.termine.link') }}</span>
            <input v-model="terminForm.link" autocomplete="off" placeholder="/kurs/python-12-wochen-grundkurs">
          </label>
          <label class="field field-checkbox">
            <input v-model="terminForm.cancelled" type="checkbox">
            <span>{{ t('admin.termine.cancelled') }}</span>
          </label>
          <label class="field field-checkbox">
            <input v-model="terminForm.recurring" type="checkbox">
            <span>{{ t('admin.termine.recurring') }}</span>
          </label>
          <template v-if="terminForm.recurring">
            <label class="field">
              <span>{{ t('admin.termine.validFrom') }}</span>
              <input v-model="terminForm.validFrom" type="date">
            </label>
            <label class="field">
              <span>{{ t('admin.termine.validUntil') }}</span>
              <input v-model="terminForm.validUntil" type="date">
            </label>
          </template>
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
import { ref, onMounted } from 'vue';
import { useLanguage } from '../composables/useLanguage.js';
import {
  adminToken as token,
  setAdminToken,
  adminLogin,
  listUsers,
  createUser,
  updateUser,
  deleteUser,
  listTermine,
  createTermin,
  updateTermin,
  deleteTermin,
} from '../composables/useAdminApi.js';

export default {
  name: 'AdminView',
  setup() {
    const { t, lang } = useLanguage();
    const password = ref('');
    const users = ref([]);
    const busy = ref(false);
    const error = ref('');
    const formOpen = ref(false);
    const formError = ref('');
    const editing = ref(null);
    const form = ref({ username: '', ageGroup: 'kinder', password: '' });

    const activeTab = ref('users');
    const termine = ref([]);
    const terminBusy = ref(false);
    const terminError = ref('');
    const terminFormOpen = ref(false);
    const terminFormError = ref('');
    const editingTermin = ref(null);
    const emptyTerminForm = () => ({
      date: '', time: '', location: '', topic: '', link: '',
      cancelled: false, recurring: false, validFrom: '', validUntil: '',
    });
    const terminForm = ref(emptyTerminForm());

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

    const openCreateTermin = () => {
      editingTermin.value = null;
      terminForm.value = emptyTerminForm();
      terminFormError.value = '';
      terminFormOpen.value = true;
    };

    const openEditTermin = (terminItem) => {
      editingTermin.value = terminItem;
      terminForm.value = {
        date: terminItem.date,
        time: terminItem.time,
        location: terminItem.location,
        topic: terminItem.topic,
        link: terminItem.link,
        cancelled: terminItem.cancelled,
        recurring: terminItem.recurring,
        validFrom: terminItem.validFrom || '',
        validUntil: terminItem.validUntil || '',
      };
      terminFormError.value = '';
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
        const payload = {
          date: terminForm.value.date,
          time: terminForm.value.time,
          location: terminForm.value.location,
          topic: terminForm.value.topic,
          link: terminForm.value.link,
          cancelled: terminForm.value.cancelled,
          recurring: terminForm.value.recurring,
          validFrom: terminForm.value.recurring ? (terminForm.value.validFrom || null) : null,
          validUntil: terminForm.value.recurring ? (terminForm.value.validUntil || null) : null,
        };
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

    onMounted(async () => {
      await Promise.all([refresh(), refreshTermine()]);
    });

    return {
      t, token, password, users, busy, error, formOpen, formError, editing, form,
      ageLabel, formatDate, login, logout, openCreate, openEdit, closeForm, save, remove,
      activeTab, termine, terminBusy, terminError, terminFormOpen, terminFormError, editingTermin, terminForm,
      openCreateTermin, openEditTermin, closeTerminForm, saveTermin, removeTermin,
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
  color: #555;
  margin: 0 0 20px;
}

.admin-login-card,
.modal-card {
  background: #fff;
  border: 1px solid #dee2e6;
  border-radius: 10px;
  padding: 20px;
  max-width: 420px;
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
  border: 1px solid #ced4da;
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
  border-bottom: 1px solid #dee2e6;
}

.admin-tab {
  border: none;
  background: none;
  padding: 10px 16px;
  font-weight: 600;
  color: #555;
  cursor: pointer;
  border-bottom: 2px solid transparent;
}

.admin-tab.active {
  color: var(--primary-purple, #4a2274);
  border-bottom-color: var(--primary-purple, #4a2274);
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
  background: #fdecea;
  color: #c0392b;
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
  background: #f1f3f5;
  color: #333;
}

.btn-primary:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.admin-table {
  width: 100%;
  border-collapse: collapse;
  background: #fff;
}

.admin-table th,
.admin-table td {
  text-align: left;
  padding: 10px 12px;
  border-bottom: 1px solid #eee;
}

.actions {
  white-space: nowrap;
}

.btn-link {
  background: none;
  border: none;
  color: var(--primary-purple, #4a2274);
  cursor: pointer;
  font-weight: 600;
  margin-right: 10px;
  padding: 0;
}

.btn-link.danger {
  color: #c0392b;
}

.error {
  color: #c0392b;
  background: #fdecea;
  padding: 8px 10px;
  border-radius: 6px;
}

.muted {
  color: #6c757d;
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
