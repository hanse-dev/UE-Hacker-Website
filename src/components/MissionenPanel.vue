<template>
  <div v-if="missionen.length > 0" class="missionen-panel">
    <div class="missionen-panel-header" @click="expanded = !expanded">
      <span class="missionen-title">{{ t('mission.panel.title') }}</span>
      <span class="missionen-toggle">{{ expanded ? '−' : '+' }}</span>
    </div>
    <div v-show="expanded" class="missionen-panel-content">
      <div class="missionen-list">
        <div
          v-for="m in missionen"
          :key="m.id"
          class="mission-item"
          :class="{ claimed: isClaimed(m.id) }"
        >
          <span class="mission-label">{{ m.label }}</span>
          <span class="mission-info">{{ m.points }} {{ pointUnit }} + {{ m.item }}</span>
          <div class="mission-actions">
            <button v-if="!isClaimed(m.id)" @click.stop="claimMission(m)" class="btn-claim">
              {{ t('mission.claim') }}
            </button>
            <template v-else>
              <span class="mission-claimed">✅</span>
              <button @click.stop="unclaimMission(m)" class="btn-unclaim" :title="t('mission.unclaim')">↩</button>
            </template>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted, watch } from 'vue';
import { useFortschritt } from '../composables/useFortschritt';
import { assetUrl } from '../utils/assetUrl';
import { useLanguage } from '../composables/useLanguage.js';

export default {
  name: 'MissionenPanel',
  props: {
    weekNumber: { type: Number, required: true },
    variant:    { type: String, default: null },
    courseId:   { type: String, default: null },
  },
  setup(props) {
    const { t, lang } = useLanguage();
    const expanded = ref(false);
    const rewardsManifest = ref(null);
    const { claimMission: doClaimMission, unclaimMission: doUnclaimMission, isClaimed: checkClaimed } = useFortschritt();

    const pointUnit = computed(() => {
      const units = {
        abenteuer: t('unit.adventure'),
        pferde:    t('unit.horses'),
        scifi:     t('unit.scifi'),
      };
      return units[props.variant] || t('unit.default');
    });

    const missionen = computed(() => {
      if (!rewardsManifest.value || !props.variant || props.courseId !== 'python-12-wochen-grundkurs') return [];
      const weekData = rewardsManifest.value[props.courseId]?.[props.variant]?.[String(props.weekNumber)];
      if (!weekData) return [];
      const missions = (weekData.missions || []).map((m, i) => ({ ...m, label: `${t('mission.label')} ${i + 1}` }));
      const bosses  = (weekData.bossQuests || []).map((m, i) => ({ ...m, label: `${t('mission.boss.label')} ${i + 1}` }));
      return [...missions, ...bosses];
    });

    const isClaimed   = (id) => checkClaimed(props.variant, id);
    const claimMission   = (m) => doClaimMission(props.variant, m.id, m.points, m.item, m.label);
    const unclaimMission = (m) => doUnclaimMission(props.variant, m.id);

    const loadManifest = async () => {
      try {
        const file = lang.value === 'en' ? 'rewards-manifest-en.json' : 'rewards-manifest.json';
        const res = await fetch(assetUrl(file));
        if (res.ok) rewardsManifest.value = await res.json();
      } catch (e) { /* silent */ }
    };

    onMounted(loadManifest);
    watch(lang, loadManifest);

    return { expanded, missionen, pointUnit, isClaimed, claimMission, unclaimMission, t };
  },
};
</script>

<style scoped>
.missionen-panel {
  background: #fffbeb;
  border: 1px solid #fde68a;
  border-radius: 8px;
  margin-bottom: 12px;
  overflow: hidden;
}

.missionen-panel-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 16px;
  cursor: pointer;
  user-select: none;
  transition: background 0.15s;
}

.missionen-panel-header:hover { background: #fef3c7; }

.missionen-title { font-weight: 600; font-size: 0.9em; color: #92400e; }
.missionen-toggle { font-size: 1.1em; color: #92400e; font-weight: bold; }

.missionen-panel-content { padding: 6px 16px 12px; border-top: 1px solid #fde68a; }

.missionen-list { display: flex; flex-direction: column; gap: 6px; margin-top: 6px; }

.mission-item {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 8px;
  padding: 7px 10px;
  background: white;
  border-radius: 6px;
  border: 1px solid #f3f4f6;
  font-size: 0.85em;
}

.mission-item.claimed { background: #f0fdf4; border-color: #bbf7d0; }

.mission-label { font-weight: 600; color: #374151; min-width: 80px; }
.mission-info  { color: #4b5563; flex: 1; }
.mission-actions { display: flex; align-items: center; gap: 6px; margin-left: auto; }

.btn-claim {
  background: #fbbf24; color: #1f2937; border: none;
  padding: 4px 12px; border-radius: 5px; font-size: 0.85em;
  font-weight: 600; cursor: pointer; transition: background 0.15s;
}
.btn-claim:hover { background: #f59e0b; }

.btn-unclaim {
  background: transparent; color: #9ca3af; border: 1px solid #d1d5db;
  padding: 3px 8px; border-radius: 4px; font-size: 0.8em; cursor: pointer;
}
.btn-unclaim:hover { background: #fee2e2; color: #dc2626; border-color: #fca5a5; }

.mission-claimed { color: #16a34a; font-size: 1em; }
</style>
