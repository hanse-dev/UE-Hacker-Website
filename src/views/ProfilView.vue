<template>
  <div class="profil-view">
    <h1>{{ t('profil.title') }}</h1>

    <div v-if="!isLoggedIn" class="profil-login-required">
      <p>{{ t('profil.loginRequired') }}</p>
    </div>

    <template v-else>
      <p class="profil-greeting">{{ t('profil.greeting').replace('{name}', user?.username || '') }}</p>

      <section class="profil-badges">
        <h2>{{ t('profil.badges.title') }}</h2>
        <p class="profil-badges-hint">{{ t('profil.badges.hint') }}</p>

        <p v-if="loading" class="profil-loading">{{ t('profil.loading') }}</p>
        <div v-else class="badge-grid">
          <router-link
            v-for="badge in badges"
            :key="badge.id"
            :to="`/kurs/${badge.id}`"
            class="badge-card"
            :class="{ earned: badge.earned }"
          >
            <span class="badge-icon">{{ badge.earned ? '🏅' : '🔒' }}</span>
            <span class="badge-title">{{ lang === 'en' && badge.title_en ? badge.title_en : badge.title }}</span>
            <span class="badge-status">
              {{ badge.earned ? t('profil.badges.earned') : `${badge.completedCount}/${badge.totalLessons}` }}
            </span>
          </router-link>
        </div>
      </section>
    </template>
  </div>
</template>

<script>
import { onMounted, watch } from 'vue';
import { useAuth } from '../composables/useAuth.js';
import { useLanguage } from '../composables/useLanguage.js';
import { useProjectBadges } from '../composables/useProjectBadges.js';

export default {
  name: 'ProfilView',
  setup() {
    const { t, lang } = useLanguage();
    const { user, isLoggedIn } = useAuth();
    const { badges, loading, load } = useProjectBadges();

    onMounted(() => {
      if (isLoggedIn.value) load();
    });
    // Direkter Login-/Logout-Wechsel auf dieser Seite (ohne Neuladen) soll die Abzeichen sofort
    // laden bzw. den Login-Hinweis zeigen, nicht den Stand vom Seitenaufruf behalten.
    watch(isLoggedIn, (now) => {
      if (now) load();
    });

    return { t, lang, user, isLoggedIn, badges, loading };
  },
};
</script>

<style scoped>
.profil-view {
  max-width: 900px;
  margin: 0 auto;
  padding: 20px;
}

.profil-login-required {
  background: #f8f9fa;
  border: 1px solid #dee2e6;
  border-radius: 8px;
  padding: 20px;
  color: #555;
}

.profil-greeting {
  font-size: 1.1em;
  color: #333;
  margin-bottom: 32px;
}

.profil-badges h2 {
  margin-bottom: 4px;
}

.profil-badges-hint {
  color: #666;
  font-size: 0.9em;
  margin: 0 0 20px 0;
}

.profil-loading {
  color: #666;
}

.badge-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
  gap: 14px;
}

.badge-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  background: #f8f9fa;
  border: 1px solid #dee2e6;
  border-radius: 10px;
  padding: 18px 12px;
  text-align: center;
  text-decoration: none;
  transition: border-color 0.15s, transform 0.15s;
}

.badge-card:hover {
  border-color: var(--primary-purple, #4a2274);
  transform: translateY(-2px);
}

.badge-card.earned {
  border-color: #ffd700;
  background: linear-gradient(135deg, #fef9e7 0%, #fdebd0 100%);
}

.badge-icon {
  font-size: 2.2em;
}

.badge-title {
  font-weight: 600;
  color: #333;
  font-size: 0.95em;
}

.badge-status {
  font-size: 0.8em;
  color: #666;
}

.badge-card.earned .badge-status {
  color: #8a6d00;
  font-weight: 600;
}
</style>
