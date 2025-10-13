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
      </nav>
    </header>

    <main class="app-main">
      <router-view />
    </main>

    <footer class="app-footer">
      <p>&copy; 2025 Übergangshacker. Alle Rechte vorbehalten.</p>
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
    return { showHomeLink };
  },
};
</script>
