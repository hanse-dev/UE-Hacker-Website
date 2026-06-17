import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import CourseDetail from '../views/CourseDetail.vue';
import Teaser from '../views/Teaser.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/kurs/:id',
    name: 'CourseDetail',
    component: CourseDetail,
    props: true,
  },
  {
    path: '/teaser',
    name: 'Teaser',
    component: Teaser,
    meta: { fullscreen: true },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
