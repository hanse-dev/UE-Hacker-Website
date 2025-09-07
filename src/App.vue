<template>
  <div id="app-container">
    <header class="app-header">
      <h1>Uebergangshacker</h1>
      <nav>
        <router-link to="/">Home</router-link>
        <router-link to="/kurs/python-12-wochen-grundkurs">Kurse</router-link>
      </nav>
    </header>

    <main class="app-main">
      <router-view />
    </main>

    <footer class="app-footer">
      <p>&copy; 2025 Uebergangshacker. Alle Rechte vorbehalten.</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>
