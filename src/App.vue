<template>
  <!-- Teaser: vollbild, kein Header/Footer -->
  <router-view v-if="isTeaser" />

  <div v-else id="app-container">
    <header class="app-header">
      <router-link to="/" class="header-title-link">
        <div class="header-title">
          <img src="@/assets/logo.png" alt="Übergangshacker Logo" class="header-logo">
          <h1>Übergangshacker</h1>
        </div>
      </router-link>
      <nav>
        <router-link v-if="showHomeLink" to="/">{{ t('nav.home') }}</router-link>
        <router-link :to="{ path: '/', hash: '#kurse-uebersicht' }">{{ t('nav.courses') }}</router-link>
        <router-link to="/projekte">{{ t('nav.projects') }}</router-link>
        <router-link v-if="isLoggedIn" to="/profil">{{ t('nav.profile') }}</router-link>
        <router-link v-if="isAdminLoggedIn" to="/admin">{{ t('nav.admin') }}</router-link>
        <button
          type="button"
          class="options-btn"
          :aria-label="t('settings.open')"
          :aria-expanded="settingsOpen"
          @click="openSettings"
        >
          {{ t('settings.open') }}
        </button>
      </nav>
    </header>

    <!-- Nur mit `npm run dev:skip-checks` (siehe composables/devSkipChecks.js), nie im Live-Betrieb. -->
    <p v-if="devSkipChecks" class="dev-skip-banner" role="status">{{ t('devSkip.banner') }}</p>

    <main class="app-main" v-if="!isCourseDetail">
      <router-view />
    </main>
    <div v-else class="app-main">
      <router-view />
    </div>

    <footer class="app-footer">
      <p>{{ t('footer.copyright') }}</p>
    </footer>

    <div
      v-if="settingsOpen"
      class="login-backdrop"
      @click.self="closeSettings"
    >
      <!-- Mit Einmal-Passwort angemeldet (mustChangePassword): Dialog lässt sich erst nach dem
           Passwortwechsel schließen, einziger Ausweg ist Abmelden. -->
      <div
        class="login-modal settings-modal"
        role="dialog"
        aria-modal="true"
        :aria-label="t('settings.title')"
      >
        <div class="settings-header">
          <h2>{{ showLoginForm ? t('auth.loginTitle') : showPasswordForm ? t('auth.changePassword') : t('settings.title') }}</h2>
          <button v-if="!mustChangePassword" type="button" class="settings-close" :aria-label="t('settings.close')" @click="closeSettings">
            ×
          </button>
        </div>

        <template v-if="!showLoginForm && !showPasswordForm">
          <section class="settings-section">
            <h3>{{ t('settings.language') }}</h3>
            <p class="settings-hint">{{ t('settings.languageHint') }}</p>
            <div class="lang-switcher modal-lang">
              <button type="button" :class="{ active: lang === 'de' }" @click="setLang('de')">DE</button>
              <button type="button" :class="{ active: lang === 'en' }" @click="setLang('en')">EN</button>
            </div>
            <p class="settings-current">
              {{ t('settings.currentLanguage') }}:
              <strong>{{ lang === 'de' ? t('settings.lang.de') : t('settings.lang.en') }}</strong>
            </p>
          </section>

          <section class="settings-section">
            <h3>{{ t('settings.account') }}</h3>
            <template v-if="isLoggedIn">
              <p class="settings-current">
                {{ t('settings.loggedInAs') }}:
                <strong>{{ user?.username }}</strong>
              </p>
              <p v-if="user?.ageGroup" class="settings-hint">
                {{ t('settings.ageGroup') }}:
                {{ user.ageGroup === 'kinder' ? t('admin.age.kinder') : t('admin.age.jugendliche') }}
              </p>
              <p class="settings-hint">{{ t('settings.syncOn') }}</p>
              <p v-if="passwordChanged" class="login-success" role="status">{{ t('auth.passwordChanged') }}</p>
              <div class="login-actions">
                <button type="button" class="auth-btn ghost change-password-btn" @click="openPasswordForm">
                  {{ t('auth.changePassword') }}
                </button>
                <button type="button" class="auth-btn ghost" @click="doLogout">{{ t('auth.logout') }}</button>
              </div>
            </template>
            <template v-else>
              <p class="settings-hint">{{ t('settings.syncOff') }}</p>
              <div class="login-actions">
                <button type="button" class="auth-btn primary" @click="showLoginForm = true">
                  {{ t('auth.login') }}
                </button>
              </div>
            </template>
          </section>
        </template>

        <template v-else-if="showPasswordForm">
          <form class="password-form" @submit.prevent="submitPassword">
            <p class="login-hint">{{ mustChangePassword ? t('auth.mustChangeHint') : t('auth.changePasswordHint') }}</p>
            <!-- Verstecktes Username-Feld, damit Passwort-Manager den Eintrag zuordnen (HANDOFF 3.64). -->
            <input
              type="text"
              name="username"
              autocomplete="username"
              :value="user?.username"
              readonly
              hidden
            >
            <!-- Direkt nach dem Login mit Einmal-Passwort ist es schon bekannt — nicht nochmal abfragen. -->
            <label v-if="!currentFromLogin" class="login-field">
              <span>{{ t('auth.currentPassword') }}</span>
              <input
                v-model="currentPassword"
                type="password"
                name="current-password"
                autocomplete="current-password"
              >
            </label>
            <label class="login-field">
              <span>{{ t('auth.newPassword') }}</span>
              <input
                v-model="newPassword"
                type="password"
                name="new-password"
                autocomplete="new-password"
              >
            </label>
            <label class="login-field">
              <span>{{ t('auth.newPasswordRepeat') }}</span>
              <input
                v-model="newPasswordRepeat"
                type="password"
                name="new-password-repeat"
                autocomplete="new-password"
              >
            </label>
            <p v-if="passwordFormError || authError" class="login-error">{{ passwordFormError || authError }}</p>
            <div class="login-actions">
              <button v-if="mustChangePassword" type="button" class="auth-btn ghost" @click="doLogout">
                {{ t('auth.logout') }}
              </button>
              <button v-else type="button" class="auth-btn ghost" @click="closePasswordForm">
                {{ t('auth.cancel') }}
              </button>
              <button type="submit" class="auth-btn primary" :disabled="authBusy">
                {{ authBusy ? t('auth.working') : t('auth.save') }}
              </button>
            </div>
          </form>
        </template>

        <template v-else>
          <form @submit.prevent="submitLogin">
            <p class="login-hint">{{ t('auth.loginHint') }}</p>
            <label class="login-field">
              <span>{{ t('auth.username') }}</span>
              <input
                v-model="loginUsername"
                name="username"
                autocomplete="username"
              >
            </label>
            <label class="login-field">
              <span>{{ t('auth.password') }}</span>
              <input
                v-model="loginPassword"
                type="password"
                name="password"
                autocomplete="current-password"
              >
            </label>
            <p v-if="authError" class="login-error">{{ authError }}</p>
            <div class="login-actions">
              <button type="button" class="auth-btn ghost" @click="showLoginForm = false">
                {{ t('auth.cancel') }}
              </button>
              <button type="submit" class="auth-btn primary" :disabled="authBusy">
                {{ authBusy ? t('auth.working') : t('auth.login') }}
              </button>
            </div>
          </form>
        </template>
      </div>
    </div>
  </div>
</template>

<script>
import { computed, onMounted, ref, watch } from 'vue';
import { useRoute } from 'vue-router';
import { useLanguage } from './composables/useLanguage.js';
import { DEV_SKIP_CHECKS } from './composables/devSkipChecks.js';
import { useAuth } from './composables/useAuth.js';
import { adminToken } from './composables/useAdminApi.js';

export default {
  name: 'App',
  setup() {
    const route = useRoute();
    const showHomeLink   = computed(() => route.path !== '/');
    const isCourseDetail = computed(() => route.path.startsWith('/kurs/'));
    const isTeaser       = computed(() => route.path === '/teaser');
    const isAdminLoggedIn = computed(() => !!adminToken.value);
    const { lang, t, setLang } = useLanguage();
    const {
      user,
      isLoggedIn,
      busy: authBusy,
      error: authError,
      login,
      changePassword,
      logout,
      restoreSession,
    } = useAuth();

    const settingsOpen = ref(false);
    const showLoginForm = ref(false);
    const loginUsername = ref('');
    const loginPassword = ref('');
    const showPasswordForm = ref(false);
    const currentPassword = ref('');
    const newPassword = ref('');
    const newPasswordRepeat = ref('');
    const passwordFormError = ref('');
    const passwordChanged = ref(false);
    const currentFromLogin = ref(false);
    const mustChangePassword = computed(() => isLoggedIn.value && Boolean(user.value?.mustChangePassword));

    const closePasswordForm = () => {
      showPasswordForm.value = false;
      currentFromLogin.value = false;
      currentPassword.value = '';
      newPassword.value = '';
      newPasswordRepeat.value = '';
      passwordFormError.value = '';
      authError.value = '';
    };

    const openPasswordForm = () => {
      closePasswordForm();
      passwordChanged.value = false;
      showPasswordForm.value = true;
    };

    const submitPassword = async () => {
      authError.value = '';
      passwordFormError.value = '';
      if (newPassword.value.length < 4) {
        passwordFormError.value = t('auth.passwordTooShort');
        return;
      }
      if (newPassword.value !== newPasswordRepeat.value) {
        passwordFormError.value = t('auth.passwordMismatch');
        return;
      }
      if (newPassword.value === currentPassword.value) {
        passwordFormError.value = t('auth.passwordSame');
        return;
      }
      const ok = await changePassword(currentPassword.value, newPassword.value);
      if (ok) {
        closePasswordForm();
        passwordChanged.value = true;
      }
    };

    // Einmal-Passwort aktiv (nach Login oder Seiten-Reload): Formular erzwingen.
    watch(mustChangePassword, (must) => {
      if (!must) return;
      settingsOpen.value = true;
      showPasswordForm.value = true;
      passwordChanged.value = false;
    }, { immediate: true });

    const openSettings = () => {
      if (mustChangePassword.value) return;
      showLoginForm.value = false;
      closePasswordForm();
      passwordChanged.value = false;
      authError.value = '';
      settingsOpen.value = true;
    };

    const closeSettings = () => {
      if (mustChangePassword.value) return;
      settingsOpen.value = false;
      showLoginForm.value = false;
      closePasswordForm();
      passwordChanged.value = false;
      loginUsername.value = '';
      loginPassword.value = '';
      authError.value = '';
    };

    const submitLogin = async () => {
      const ok = await login(loginUsername.value.trim(), loginPassword.value);
      if (ok) {
        if (mustChangePassword.value) {
          currentPassword.value = loginPassword.value;
          currentFromLogin.value = true;
        }
        loginUsername.value = '';
        loginPassword.value = '';
        showLoginForm.value = false;
      }
    };

    const doLogout = () => {
      closePasswordForm();
      passwordChanged.value = false;
      logout();
    };

    onMounted(() => {
      restoreSession();
    });

    return {
      devSkipChecks: DEV_SKIP_CHECKS,
      showHomeLink,
      isCourseDetail,
      isTeaser,
      isAdminLoggedIn,
      lang,
      t,
      setLang,
      user,
      isLoggedIn,
      settingsOpen,
      showLoginForm,
      authBusy,
      authError,
      openSettings,
      closeSettings,
      doLogout,
      loginUsername,
      loginPassword,
      submitLogin,
      showPasswordForm,
      currentPassword,
      newPassword,
      newPasswordRepeat,
      passwordFormError,
      passwordChanged,
      currentFromLogin,
      mustChangePassword,
      openPasswordForm,
      closePasswordForm,
      submitPassword,
    };
  },
};
</script>

<style scoped>
.options-btn {
  margin-left: 12px;
  background: transparent;
  border: 1px solid rgba(253, 248, 225, 0.55);
  padding: 5px 12px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.9em;
  font-weight: 700;
  color: var(--text-light);
}

.options-btn:hover,
.options-btn[aria-expanded='true'] {
  border-color: var(--accent-yellow);
  color: var(--accent-yellow);
}

.settings-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 0.5rem;
}

.settings-header h2 {
  margin: 0;
}

.settings-close {
  border: none;
  background: transparent;
  font-size: 1.6rem;
  line-height: 1;
  cursor: pointer;
  color: #888;
  padding: 0 4px;
}

.settings-close:hover {
  color: #333;
}

.settings-section {
  margin-top: 1.1rem;
  padding-top: 1rem;
  border-top: 1px solid #eee;
}

.settings-section:first-of-type {
  margin-top: 0.4rem;
  padding-top: 0;
  border-top: none;
}

.settings-section h3 {
  margin: 0 0 0.35rem;
  font-size: 1rem;
  color: #222;
}

.settings-hint {
  margin: 0 0 0.75rem;
  font-size: 0.88em;
  color: #666;
  line-height: 1.4;
}

.settings-current {
  margin: 0.6rem 0 0;
  font-size: 0.92em;
  color: #333;
}

.modal-lang {
  margin-left: 0;
}

.lang-switcher {
  display: flex;
  gap: 2px;
}

.lang-switcher button {
  background: transparent;
  border: 1px solid #ccc;
  padding: 5px 12px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.85em;
  font-weight: 700;
  color: #555;
  transition: all 0.15s;
}

.lang-switcher button:hover {
  border-color: var(--primary-purple);
  color: var(--primary-purple);
}

.lang-switcher button.active {
  background: var(--accent-yellow);
  border-color: var(--accent-yellow);
  color: var(--primary-purple);
}

.login-actions .auth-btn {
  background: transparent;
  border: 1px solid #ccc;
  padding: 4px 10px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.82em;
  font-weight: 600;
  color: #444;
}

.login-actions .auth-btn:hover {
  border-color: #ff4136;
  color: #ff4136;
}

.login-actions .auth-btn.primary {
  background: #ff4136;
  border-color: #ff4136;
  color: #fff;
}

.login-actions .auth-btn.primary:hover {
  filter: brightness(0.95);
  color: #fff;
}

.login-actions .auth-btn.ghost {
  border-color: #ddd;
}

.login-actions .auth-btn:disabled {
  opacity: 0.6;
  cursor: wait;
}

.login-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(20, 20, 20, 0.45);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 16px;
}

.login-modal {
  background: #fff;
  border-radius: 10px;
  padding: 1.4rem 1.5rem;
  width: min(400px, 100%);
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.18);
}

.login-modal h2 {
  margin: 0 0 0.4rem;
  font-size: 1.25rem;
  color: #222;
}

.login-hint {
  margin: 0 0 1rem;
  font-size: 0.9em;
  color: #666;
  line-height: 1.4;
}

.login-field {
  display: flex;
  flex-direction: column;
  gap: 4px;
  margin-bottom: 0.75rem;
  font-size: 0.9em;
  color: #333;
}

.login-field input {
  padding: 8px 10px;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-size: 1em;
}

.login-error {
  color: #c0392b;
  font-size: 0.88em;
  margin: 0 0 0.75rem;
}

.login-success {
  color: #1e7e34;
  font-size: 0.88em;
  margin: 0 0 0.75rem;
}

.login-actions {
  display: flex;
  justify-content: flex-end;
  gap: 8px;
  margin-top: 0.75rem;
}
.dev-skip-banner {
  margin: 0;
  padding: 8px 16px;
  text-align: center;
  font-size: 0.9em;
  background: #fff3cd;
  border-bottom: 1px solid #ffe69c;
  color: #664d03;
}
</style>
