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
    path: '/kurs/:id',
    name: 'CourseDetail',
    component: CourseDetail,
    props: true,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
