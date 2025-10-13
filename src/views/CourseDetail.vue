<template>
  <section class="course-detail" v-if="course">
    <h1>{{ course.title }}</h1>
    <div v-if="description" v-html="description" class="course-description"></div>

    <!-- Upcoming Appointments Section -->
    <div class="appointments-section" v-if="courseTermine.length > 0">
      <h3>Nächste Termine für diesen Kurs</h3>
      <div class="termine-list-local">
        <div v-for="termin in courseTermine" :key="termin.id" class="termin-card-local">
          <h4>{{ termin.date }}</h4>
          <p><strong>Uhrzeit:</strong> {{ termin.time }}</p>
          <p><strong>Ort:</strong> {{ termin.location }}</p>
          <p v-if="termin.topic"><strong>Thema:</strong> {{ termin.topic }}</p>
        </div>
      </div>
    </div>

    <div class="table-of-contents" v-if="weeks.length > 0">
      <h3>Inhaltsverzeichnis</h3>
      <ol>
        <li v-for="(week, index) in weeks" :key="`toc-${index}`">
          <a :href="`#woche-${index + 1}`">{{ week.title }}</a>
        </li>
      </ol>
    </div>

    <div v-for="(week, index) in weeks" :key="index" class="week-section" :id="`woche-${index + 1}`">
      <div class="week-section-inner">
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
    </div>
  </section>
  <div v-else>
      <p>Kurs wird geladen...</p>
  </div>
</template>

<script>
import { ref, onMounted, computed } from 'vue';
import fm from 'front-matter';
import { marked } from 'marked';

export default {
  name: 'CourseDetail',
  props: {
    id: {
      type: String,
      required: true,
    },
  },
  setup(props) {
    const course = ref(null);
    const description = ref('');
    const weeks = ref([]);
    const courseTermine = ref([]);

    const isWeeklyCourse = computed(() => {
        return props.id === 'python-12-wochen-grundkurs';
    });

    const parseDate = (dateString) => {
      const datePart = dateString.split(', ')[1];
      if (!datePart) return null;
      const parts = datePart.split('.');
      if (parts.length !== 3) return null;
      return new Date(`20${parts[2]}`, parts[1] - 1, parts[0]);
    };

    onMounted(async () => {
      // Load course data from JSON
      try {
        const response = await fetch('/kurse.json');
        const kurse = await response.json();
        course.value = kurse.find(k => k.id === props.id);
      } catch (e) {
        console.error('Could not load courses:', e);
      }

      if (course.value) {
        // Load description
        try {
          const descModule = await import(`../../content/${course.value.contentPath}/beschreibung.md?raw`);
          description.value = marked(descModule.default);
        } catch (e) {
          console.error('Could not load course description:', e);
          description.value = '<p>Die Beschreibung für diesen Kurs konnte nicht geladen werden.</p>';
        }

        // Load appointments for this course
        try {
            const response = await fetch('/termine.json');
            const allTermine = await response.json();
            const today = new Date();
            today.setHours(0, 0, 0, 0);

            courseTermine.value = allTermine
                .filter(termin => {
                    const terminDate = parseDate(termin.date);
                    return !termin.cancelled && termin.link.startsWith(`/kurs/${props.id}`) && terminDate && terminDate >= today;
                })
                .sort((a, b) => parseDate(a.date) - parseDate(b.date));
        } catch (e) {
            console.error('Could not load appointments:', e);
        }

        // Load weekly content only for the 12-week course
        if (isWeeklyCourse.value) {
            const weekModules = import.meta.glob('../../content/python-12-wochen-grundkurs/woche-*/*.md', { query: '?raw' });
            const downloadModules = import.meta.glob('../../content/python-12-wochen-grundkurs/woche-*/*.*', { query: '?url', import: 'default' });
            const weeklyContent = {};

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
        }
      }
    });

    return {
      course,
      description,
      weeks,
      isWeeklyCourse,
      courseTermine,
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

.table-of-contents {
  background-color: #fdfdfd;
  border: 1px solid #eee;
  padding: 20px;
  margin-bottom: 40px;
  border-radius: 8px;
}

.table-of-contents h3 {
  margin-top: 0;
  border-bottom: 2px solid #ffd700;
  padding-bottom: 10px;
}

.table-of-contents ol {
  padding-left: 20px;
  margin: 0;
}

.table-of-contents li {
  margin-bottom: 10px;
}

.table-of-contents a {
  text-decoration: none;
  color: #333;
}

.table-of-contents a:hover {
  color: #ff4136;
}

.appointments-section {
  background-color: #f9f9f9;
  border: 1px solid #eee;
  padding: 20px;
  margin-bottom: 40px;
  border-radius: 8px;
}

.appointments-section h3 {
  margin-top: 0;
  border-bottom: 2px solid #ffd700;
  padding-bottom: 10px;
}

.termin-card-local {
  background: #fff;
  border: 1px solid #ddd;
  padding: 15px;
  margin-bottom: 15px;
  border-radius: 8px;
}

.termin-card-local h4 {
    margin-top: 0;
}

</style>