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
        <div class="lang-switcher">
          <button :class="{ active: lang === 'de' }" @click="setLang('de')">DE</button>
          <button :class="{ active: lang === 'en' }" @click="setLang('en')">EN</button>
        </div>
      </nav>
    </header>

    <main class="app-main" v-if="!isCourseDetail">
      <router-view />
    </main>
    <div v-else class="app-main">
      <router-view />
    </div>

    <footer class="app-footer">
      <p>{{ t('footer.copyright') }}</p>
    </footer>
  </div>
</template>

<script>
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import { useLanguage } from './composables/useLanguage.js';

export default {
  name: 'App',
  setup() {
    const route = useRoute();
    const showHomeLink   = computed(() => route.path !== '/');
    const isCourseDetail = computed(() => route.path.startsWith('/kurs/'));
    const isTeaser       = computed(() => route.path === '/teaser');
    const { lang, t, setLang } = useLanguage();
    return { showHomeLink, isCourseDetail, isTeaser, lang, t, setLang };
  },
};
</script>

<style scoped>
.lang-switcher {
  display: flex;
  gap: 2px;
  margin-left: 12px;
}

.lang-switcher button {
  background: transparent;
  border: 1px solid #ccc;
  padding: 3px 8px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.78em;
  font-weight: 600;
  color: #666;
  transition: all 0.15s;
}

.lang-switcher button:hover {
  border-color: #ff4136;
  color: #ff4136;
}

.lang-switcher button.active {
  background: #ff4136;
  border-color: #ff4136;
  color: white;
}
</style>
