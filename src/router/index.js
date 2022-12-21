import {
  createRouter,
  createWebHashHistory
} from 'vue-router'
import Layout from '@/views/Layout.vue'
import Home  from '@/views/Home/Home.vue'

// import SignUp from "@/views/auth/SignUp";
// import SignIn from "@/views/auth/SignIn";
// import ForgotPassword from "@/views/auth/ForgotPassword";
// import Confirm from "@/views/auth/Confirm";
// import NotFound from "@/views/NotFound";
// import Settings from "@/views/auth/Settings";
// import store from "../store/index.js";

// const Login = () => import('@/views/Login.vue')
const Category = () => import('@/views/Category/Category.vue')
const Subcategory = () => import('@/views/Category/Subcategory.vue')
const Search = () => import('@/views/Search.vue')
// const SignUp = () => import("@/views/auth/SignUp.vue")
// const SignIn = () => import("@/components/auth/SignInForm.vue")

import SignUp from "@/views/auth/SignUp";
import SignIn from "@/views/auth/SignIn";
import ForgotPassword from "@/views/auth/ForgotPassword";
import Confirm from "@/views/auth/Confirm";
import NotFound from "@/views/NotFound";
import Settings from "@/views/auth/Settings";
import Contacts from "@/views/contacts/Contacts";
import AddContact from "@/views/contacts/AddContact";
import EditContact from "@/views/contacts/EditContact";
import DeleteContact from "@/views/contacts/DeleteContact";
import store from "../store/index.js";

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
      {
        path:'/search/:keyword',
        component:Search
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
      }
    ],
    meta: {
      requiresAuth: false,
    },
  },
  // {
  //   path: "/forgotpassword",
  //   name: "ForgotPassword",
  //   component: ForgotPassword,
  // },
  // { path: "/confirm", name: "Confirm", component: Confirm },
  // {
  //   path: "/settings",
  //   name: "Settings",
  //   component: Settings,
  //   beforeEnter: isAuthenticated,
  //   meta: {
  //     requiresAuth: true,
  //   },
  // },
  // {
  //   path: "/entry",
  //   name: "entry",
  //   component: Layout,
  //   beforeEnter: isAuthenticated,
  //   children:[
  //     {
  //       path:'/entry/',
  //       component:Home
  //     },
  //     {
  //       path:'/entry/search/:keyword',
  //       component:Search
  //     },
  //     {
  //       path:'/entry/category/:id/subcat/:subid',
  //       component:Subcategory
  //     },
  //     {
  //       path:'/category/:id',
  //       component:Category,
  //       children:[
  //       ]
  //     }
  //   ],
  //   meta: {
  //     requiresAuth: true,
  //   },
  // },

  // { path: "/:notFound(.*)", component: NotFound },
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