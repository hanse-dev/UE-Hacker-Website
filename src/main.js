import { createApp } from 'vue'
import App from './App.vue';
import router from './router';
import lerntext from './directives/lerntext';
import './style.css';

const app = createApp(App);

app.use(router);
app.directive('lerntext', lerntext);

app.mount('#app');
