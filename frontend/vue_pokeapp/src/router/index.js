import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue';
import Login from '../views/Login.vue';
import Register from "@/views/Register.vue";
import { jwtDecode } from "jwt-decode";

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: {requiresAuth: true}
  },
  {
    path: '/register',
    name: 'Register',
    component: Register,
  }
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
});

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token');

  if(token) {
    try {
      const decodedToken = jwtDecode(token);
      const isTokenExpired = decodedToken.exp * 1000 < Date.now();

      if(isTokenExpired) {
        localStorage.removeItem('token');
        next('/login');
      } else {
        next();
      }
    } catch (error) {
      localStorage.removeItem('token');
      next('/login');
    }
  } else if(to.matched.some(record => record.meta.requiresAuth)) {
    next('/login');
  } else {
    next();
  }
});

export default router
