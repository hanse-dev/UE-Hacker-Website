<template>
  <div class="partner-box">
    <template v-if="!isLoggedIn">
      <p class="partner-hint">{{ t('partner.loginFirst') }}</p>
    </template>

    <template v-else-if="partner">
      <p class="partner-linked">
        👥 {{ t('partner.linked') }}
        <strong class="partner-names">{{ user.username }} + {{ partner.username }}</strong>
      </p>
      <p class="partner-hint">{{ t('partner.linkedHint') }}</p>
      <button type="button" class="partner-unlink" @click="unlink">{{ t('partner.unlink') }}</button>
    </template>

    <template v-else>
      <button v-if="!open" type="button" class="partner-open" @click="open = true">
        👥 {{ t('partner.open') }}
      </button>
      <form v-else class="partner-form" @submit.prevent="submit">
        <p class="partner-hint">{{ t('partner.formHint') }}</p>
        <label>
          <span>{{ t('partner.username') }}</span>
          <input v-model="username" class="partner-username" type="text" autocomplete="off" autocapitalize="off">
        </label>
        <label>
          <span>{{ t('partner.password') }}</span>
          <!-- new-password: Der Browser soll hier nicht das Passwort der angemeldeten Person einsetzen. -->
          <input v-model="password" class="partner-password" type="password" autocomplete="new-password">
        </label>
        <p v-if="error" class="partner-error" role="alert">{{ error }}</p>
        <div class="partner-actions">
          <button type="submit" class="partner-submit" :disabled="busy || !username || !password">
            {{ busy ? t('partner.working') : t('partner.submit') }}
          </button>
          <button type="button" class="partner-cancel" @click="cancel">{{ t('partner.cancel') }}</button>
        </div>
      </form>
    </template>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useAuth } from '../composables/useAuth';
import { useInteractiveProgress } from '../composables/useInteractiveProgress';
import { useLanguage } from '../composables/useLanguage';
import { usePartner } from '../composables/usePartner';

// Zwei Accounts an einem Rechner: Die zweite Person trägt sich hier ein, danach landet der Stand
// dieses Kurses (abgeschlossene Lektionen und einzelne Haken) in beiden Accounts.
export default {
  name: 'PartnerBox',
  props: {
    variant: { type: String, required: true },
    courseId: { type: String, required: true },
  },
  setup(props) {
    const { t } = useLanguage();
    const { user, isLoggedIn } = useAuth();
    const { mergeState, storageKey } = useInteractiveProgress(props.variant, props.courseId);
    const { partner, link, unlink } = usePartner(props.variant);

    const open = ref(false);
    const username = ref('');
    const password = ref('');
    const busy = ref(false);
    const error = ref('');

    const cancel = () => {
      open.value = false;
      username.value = '';
      password.value = '';
      error.value = '';
    };

    const submit = async () => {
      busy.value = true;
      error.value = '';
      try {
        const partnerState = await link(username.value, password.value, storageKey);
        // Beide Stände zusammenführen. Das Speichern schreibt das Ergebnis in beide Accounts.
        mergeState(partnerState);
        cancel();
      } catch (e) {
        const key = `partner.error.${e.code || 'network'}`;
        error.value = t(key) === key ? t('partner.error.network') : t(key);
      } finally {
        busy.value = false;
      }
    };

    return { t, user, isLoggedIn, partner, unlink, open, username, password, busy, error, submit, cancel };
  },
};
</script>

<style scoped>
.partner-box {
  margin-top: 16px;
  padding: 12px;
  border: 1px solid var(--border);
  border-radius: 8px;
  font-size: 0.9em;
}

.partner-hint {
  margin: 0 0 8px 0;
  color: var(--text-muted);
}

.partner-linked {
  margin: 0 0 6px 0;
}

.partner-names {
  display: block;
}

.partner-form label {
  display: block;
  margin-bottom: 8px;
}

.partner-form label span {
  display: block;
  margin-bottom: 2px;
}

.partner-form input {
  width: 100%;
  box-sizing: border-box;
  padding: 6px 8px;
  border: 1px solid var(--border-strong);
  border-radius: 6px;
  font: inherit;
}

.partner-error {
  margin: 0 0 8px 0;
  color: var(--danger-text);
}

.partner-actions {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.partner-open,
.partner-submit,
.partner-cancel,
.partner-unlink {
  padding: 6px 12px;
  border: 1px solid var(--brand-text);
  border-radius: 6px;
  background: transparent;
  color: var(--brand-text);
  font: inherit;
  cursor: pointer;
}

.partner-open {
  width: 100%;
}

.partner-submit {
  background: var(--primary-purple);
  color: #fff;
}

.partner-submit:disabled {
  opacity: 0.6;
  cursor: default;
}
</style>
