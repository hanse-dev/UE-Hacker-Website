import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import CourseDetail from '../views/CourseDetail.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/kurs/python-12-wochen-grundkurs',
    name: 'CourseDetail',
    component: CourseDetail,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
