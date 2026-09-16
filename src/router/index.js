import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import CourseDetail from '../views/CourseDetail.vue';
import Teaser from '../views/Teaser.vue';
import AdminView from '../views/AdminView.vue';
import WeekTourView from '../views/experiment/WeekTourView.vue';

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
  {
    path: '/admin',
    name: 'Admin',
    component: AdminView,
  },
  {
    // Unverlinktes Experiment (nicht Teil des regulären Kurses) - siehe HANDOFF.md 3.33
    // für das Vorbild dieses Musters. Nur per direkter URL erreichbar.
    path: '/experiment/wochen-tour',
    name: 'WeekTourExperiment',
    component: WeekTourView,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
