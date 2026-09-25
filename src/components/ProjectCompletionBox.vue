<template>
  <div class="project-completion">
    <p class="completion-badge-hint">
      🏅
      <router-link to="/profil">{{ isLoggedIn ? t('lesson.viewBadge') : t('lesson.loginForBadge') }}</router-link>
    </p>
    <div class="completion-actions">
      <router-link to="/projekte" class="btn-next">{{ t('lesson.moreProjects') }}</router-link>
      <router-link v-if="nextCourseId" :to="'/kurs/' + nextCourseId" class="btn-next btn-next-secondary">
        {{ t('lesson.goToWeeklyCourse') }}
      </router-link>
    </div>
  </div>
</template>

<script>
import { useAuth } from '../composables/useAuth';
import { useLanguage } from '../composables/useLanguage';

export default {
  name: 'ProjectCompletionBox',
  props: {
    nextCourseId: {
      type: String,
      default: null,
    },
  },
  setup() {
    const { t } = useLanguage();
    const { isLoggedIn } = useAuth();
    return { t, isLoggedIn };
  },
};
</script>

<style scoped>
.completion-badge-hint {
  margin: 0 0 16px 0;
  font-size: 1em;
}

.completion-badge-hint a {
  color: var(--primary-purple, #4a2274);
  font-weight: 600;
}

.completion-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.btn-next {
  display: inline-block;
  background: var(--primary-purple, #4a2274);
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 6px;
  font-size: 16px;
  font-weight: 600;
  text-decoration: none;
  text-align: center;
  cursor: pointer;
}

.btn-next:hover {
  background: #3d1b5c;
}

.btn-next-secondary {
  background: transparent;
  color: var(--primary-purple, #4a2274);
  border: 2px solid var(--primary-purple, #4a2274);
}

.btn-next-secondary:hover {
  background: #f1eef7;
}
</style>
