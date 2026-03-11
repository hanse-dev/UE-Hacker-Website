<template>
  <div id="app-container">
    <header class="app-header">
      <router-link to="/" class="header-title-link">
        <div class="header-title">
          <img src="@/assets/logo.png" alt="Übergangshacker Logo" class="header-logo">
          <h1>Übergangshacker</h1>
        </div>
      </router-link>
      <nav>
        <router-link v-if="showHomeLink" to="/">Home</router-link>
        <router-link :to="{ path: '/', hash: '#kurse-uebersicht' }">Kurse</router-link>
      </nav>
    </header>

    <main class="app-main" v-if="!isCourseDetail">
      <router-view />
    </main>
    <div v-else class="app-main">
      <router-view />
    </div>

    <footer class="app-footer">
      <p>&copy; 2026 Übergangshacker. Alle Rechte vorbehalten.</p>
    </footer>
  </div>
</template>

<script>
import { computed } from 'vue';
import { useRoute } from 'vue-router';

export default {
  name: 'App',
  setup() {
    const route = useRoute();
    const showHomeLink = computed(() => route.path !== '/');
    const isCourseDetail = computed(() => route.path.startsWith('/kurs/'));
    return { showHomeLink, isCourseDetail };
  },
};
</script>
