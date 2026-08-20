<template>
  <section class="admin-page">
    <h1>{{ t('admin.title') }}</h1>
    <p class="admin-intro">{{ t('admin.intro') }}</p>

    <div v-if="!token" class="admin-login-card">
      <label class="field">
        <span>{{ t('admin.adminPassword') }}</span>
        <input
          v-model="password"
          type="password"
          autocomplete="current-password"
          @keydown.enter="login"
        >
      </label>
      <p v-if="error" class="error">{{ error }}</p>
      <button type="button" class="btn-primary" :disabled="busy" @click="login">
        {{ busy ? t('admin.working') : t('admin.login') }}
      </button>
    </div>

    <template v-else>
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
    </template>
  </section>
</template>

<script>
import { ref, onMounted } from 'vue';
import { useLanguage } from '../composables/useLanguage.js';
import {
  getAdminToken,
  setAdminToken,
  adminLogin,
  listUsers,
  createUser,
  updateUser,
  deleteUser,
} from '../composables/useAdminApi.js';

export default {
  name: 'AdminView',
  setup() {
    const { t, lang } = useLanguage();
    const token = ref(getAdminToken());
    const password = ref('');
    const users = ref([]);
    const busy = ref(false);
    const error = ref('');
    const formOpen = ref(false);
    const formError = ref('');
    const editing = ref(null);
    const form = ref({ username: '', ageGroup: 'kinder', password: '' });

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
          token.value = '';
        }
        error.value = e.message || t('admin.error');
      } finally {
        busy.value = false;
      }
    };

    const login = async () => {
      busy.value = true;
      error.value = '';
      try {
        const data = await adminLogin(password.value);
        setAdminToken(data.token);
        token.value = data.token;
        password.value = '';
        await refresh();
      } catch (e) {
        error.value = e.message || t('admin.error');
      } finally {
        busy.value = false;
      }
    };

    const logout = () => {
      setAdminToken('');
      token.value = '';
      users.value = [];
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

    onMounted(refresh);

    return {
      t, token, password, users, busy, error, formOpen, formError, editing, form,
      ageLabel, formatDate, login, logout, openCreate, openEdit, closeForm, save, remove,
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
