import Vue from 'vue';
import App from './App.vue';
import 'normalize.css';
import '@fontsource/roboto';
import '@fontsource/roboto/500.css';
import '@fontsource/roboto/700.css';
import Multiselect from 'vue-multiselect';
import 'vue-multiselect/dist/vue-multiselect.min.css';

Vue.config.productionTip = false;

Vue.component('multiselect', Multiselect);

new Vue({
	render: (h) => h(App),
}).$mount('#app');
