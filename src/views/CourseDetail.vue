<template>
  <section class="course-detail">
    <h1>12-Wochen Python Grundkurs</h1>
    <div v-if="description" v-html="description" class="course-description"></div>

    <div v-for="(week, index) in weeks" :key="index" class="week-section">
      <h2>{{ week.title }}</h2>
      <div v-html="week.content"></div>
      <div v-if="week.downloads.length > 0" class="downloads-section">
        <h4>Downloads</h4>
        <ul>
          <li v-for="(file, fileIndex) in week.downloads" :key="fileIndex">
            <a :href="file.url" download>{{ file.name }}</a>
          </li>
        </ul>
      </div>
    </div>
  </section>
</template>

<script>
import { ref, onMounted } from 'vue';
import fm from 'front-matter';
import { marked } from 'marked';

export default {
  name: 'CourseDetail',
  setup() {
    const description = ref('');
    const weeks = ref([]);

    onMounted(async () => {
      // Load description
      try {
        const descModule = await import('../../content/python-12-wochen-grundkurs/beschreibung.md?raw');
        description.value = marked(descModule.default);
      } catch (e) {
        console.error('Could not load course description:', e);
      }

      // Load weekly content
      const weekModules = import.meta.glob('../../content/python-12-wochen-grundkurs/woche-*/*.md', { query: '?raw' });
      const downloadModules = import.meta.glob('../../content/python-12-wochen-grundkurs/woche-*/*.*', { query: '?url', import: 'default' });
      const weeklyContent = {};

      // 1. Process all markdown files first
      const markdownPromises = Object.entries(weekModules).map(async ([path, loader]) => {
        const weekMatch = path.match(/woche-(\d+)/);
        if (weekMatch) {
          const weekNum = parseInt(weekMatch[1], 10);
          const rawContent = (await loader()).default;
          const parsed = fm(rawContent);
          weeklyContent[weekNum] = {
            title: parsed.attributes.title || `Woche ${weekNum}`,
            content: marked(parsed.body),
            downloads: [],
          };
        }
      });
      await Promise.all(markdownPromises);

      // 2. Process all download files
      const downloadPromises = Object.entries(downloadModules).map(async ([path, loader]) => {
        if (path.endsWith('.md')) return;
        const weekMatch = path.match(/woche-(\d+)/);
        if (weekMatch) {
          const weekNum = parseInt(weekMatch[1], 10);
          if (weeklyContent[weekNum]) {
            const url = await loader();
            weeklyContent[weekNum].downloads.push({
              name: path.split('/').pop(),
              url: url,
            });
          }
        }
      });
      await Promise.all(downloadPromises);

      weeks.value = Object.values(weeklyContent).sort((a, b) => {
        const weekA = parseInt(a.title.match(/\d+/) || 0, 10);
        const weekB = parseInt(b.title.match(/\d+/) || 0, 10);
        return weekA - weekB;
      });
    });

    return {
      description,
      weeks,
    };
  },
};
</script>

<style scoped>
.course-detail {
  padding: 20px;
}
.course-description {
  margin-bottom: 40px;
  font-size: 1.1em;
}
.week-section {
  margin-bottom: 30px;
  padding: 20px;
  background-color: #f9f9f9;
  border-left: 4px solid #ffd700;
}
.downloads-section h4 {
  margin-top: 20px;
  border-top: 1px solid #eee;
  padding-top: 15px;
}
.downloads-section ul {
  list-style-type: none;
  padding: 0;
}
.downloads-section li a {
  text-decoration: none;
  color: #ff4136;
}
</style>
