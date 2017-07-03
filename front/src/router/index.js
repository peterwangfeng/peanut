import Vue from 'vue';
import Router from 'vue-router';
import Hello from '@/components/Hello';
import Login from '@/components/login';
import Home from '@/components/Home';
import First from '@/components/first';
import Second from '@/components/second';
import Third from '@/components/third';
import Fourth from '@/components/fourth';
Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'hello',
      component: Login
    }, {
      path: '/home',
      name: 'home',
      component: Home,
      children: [
        {
          path: 'first',
          component: First
        },
        {
          path: 'second',
          component: Second
        },
        {
          path: 'third',
          component: Third
        },
        {
          path: 'fourth',
          component: Fourth
        }
      ]
    }
  ]
});
