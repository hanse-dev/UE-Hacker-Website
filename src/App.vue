<template>
  <div id="app-container">
    <header class="app-header">
      <div class="header-title">
        <img src="@/assets/logo.png" alt="Übergangshacker Logo" class="header-logo">
        <h1>Übergangshacker</h1>
      </div>
      <nav>
        <router-link to="/">Home</router-link>
        <router-link to="/kurs/python-12-wochen-grundkurs">Kurse</router-link>
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
export default {
  name: 'App',
};
</script>
