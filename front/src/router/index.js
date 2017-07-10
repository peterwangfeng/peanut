import Vue from 'vue';
import Router from 'vue-router';
import VueResource from 'vue-resource';
import Login from '@/components/login';
import Home from '@/components/Home';
import First from '@/components/first';
import Second from '@/components/second';
import Third from '@/components/third';
import Fourth from '@/components/fourth';
import {MessageBox} from 'element-ui';
import {Notification} from 'element-ui';
Vue.use(Router);
Vue.use(VueResource);

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'login',
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

Vue.http.interceptors.push((request, next) => {
  let Token = window.localStorage.getItem('token');
  Vue.http.headers.common['Authorization'] = `Token ${Token}`;
  next(response => {
    let status = String(response.status);
    let code = response.data.code;
    if (code === 2005) {
      Notification.warning({
        title: '提示',
        message: '验证过期,请重新登录',
      });
      router.push({name: 'login'});
    }
    if (status.indexOf('4') === 0) {
      // MessageBox({ title: '错误', message: '请求错误' });
    } else if (status.indexOf('5') === 0) {
      MessageBox({title: '错误', message: '服务器错误'});
    }
    return response;
  });
});

export default router;




