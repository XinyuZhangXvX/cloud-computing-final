import {
  createRouter,
  createWebHashHistory
} from 'vue-router'
import Layout from '@/views/Layout.vue'
import Home  from '@/views/Home/Home.vue'
const Category = () => import('@/views/Category/Category.vue')
const Subcategory = () => import('@/views/Category/Subcategory.vue')
const Search = () => import('@/views/Search.vue')
const Favorite = () => import('@/views/Favorite.vue')
const Questionnaire = () => import('@/views/Questionnaire.vue')

import SignUp from "@/views/auth/SignUp";
import SignIn from "@/views/auth/SignIn";
import Confirm from "@/views/auth/Confirm";
import NotFound from "@/views/NotFound";
import store from "../store/index.js";
import ForgotPassword from "@/views/auth/ForgotPassword";

const routes = [
  
  {
    
    path: '/',
    name: 'Layout',
    component: Layout,
    children:[
      {
        path:'/',
        name:"Home",
        component:Home
      },
      { path: "/signup", name: "SignUp", component: SignUp },
      { path: "/signin", name: "SignIn", component: SignIn },
      { path: "/confirm", name: "Confirm", component: Confirm },
      {
        path: "/forgotpassword",
        name: "ForgotPassword",
        component: ForgotPassword,
      },
      {
        path:'/search/:keyword',
        component:Search
      },
      {
        path: '/favorite',
        component: Favorite
      },
      {
        path: '/questionnaire',
        component: Questionnaire
      },
      {
        path:'/category/:id/subcat/:subid',
        component:Subcategory
      },
      {
        path:'/category/:id',
        component:Category,
        children:[
        ]
      },
      { path: "/:notFound(.*)", component: NotFound }
    ],
    meta: {
      requiresAuth: false,
    },
  },
];

const router = createRouter({
  // Hash模式
  history: createWebHashHistory(),
  routes
})

function isAuthenticated(to, from, next) {
  if (store.getters.isAuthenticated) {
    next();
  } else {
    next("/signin");
  }
}

export default router