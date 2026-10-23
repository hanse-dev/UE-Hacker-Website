import { ref, computed, readonly } from 'vue';
import {
  changeUserPassword,
  clearUserSession,
  fetchMe,
  getUserInfo,
  getUserToken,
  loginUser,
  setUserSession,
} from './useAuthApi.js';
import { loadAccountProgress, syncNow } from './useProgressSync.js';
import { clearPartners } from './usePartner.js';

const user = ref(getUserInfo());
const token = ref(getUserToken());
const loginOpen = ref(false);
const busy = ref(false);
const error = ref('');

const isLoggedIn = computed(() => Boolean(token.value && user.value));

export function useAuth() {
  const openLogin = () => {
    error.value = '';
    loginOpen.value = true;
  };

  const closeLogin = () => {
    loginOpen.value = false;
    error.value = '';
  };

  const login = async (username, password) => {
    busy.value = true;
    error.value = '';
    try {
      const data = await loginUser(username, password);
      clearPartners();
      setUserSession(data.token, data.user);
      token.value = data.token;
      user.value = data.user;
      await loadAccountProgress();
      loginOpen.value = false;
      return true;
    } catch (e) {
      error.value = e.message || 'Login fehlgeschlagen.';
      return false;
    } finally {
      busy.value = false;
    }
  };

  const changePassword = async (currentPassword, newPassword) => {
    busy.value = true;
    error.value = '';
    try {
      // Der Server stellt ein frisches Token aus; alle älteren (auch auf anderen Geräten) verfallen.
      const data = await changeUserPassword(currentPassword, newPassword);
      setUserSession(data.token, data.user);
      token.value = data.token;
      user.value = data.user;
      return true;
    } catch (e) {
      error.value = e.message || 'Passwort konnte nicht geändert werden.';
      return false;
    } finally {
      busy.value = false;
    }
  };

  const logout = () => {
    clearPartners();
    clearUserSession();
    token.value = '';
    user.value = null;
    error.value = '';
  };

  const restoreSession = async () => {
    if (!token.value) return;
    try {
      const data = await fetchMe();
      user.value = data.user;
      setUserSession(token.value, data.user);
      await syncNow({ reason: 'restore' });
    } catch {
      logout();
    }
  };

  return {
    user: readonly(user),
    token: readonly(token),
    isLoggedIn,
    loginOpen,
    busy: readonly(busy),
    error,
    openLogin,
    closeLogin,
    login,
    changePassword,
    logout,
    restoreSession,
  };
}
