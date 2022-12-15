import {
  createRouter,
  createWebHashHistory
} from 'vue-router'
import Layout from '@/views/Layout.vue'
import Home  from '@/views/Home/Home.vue'
const Login = () => import('@/views/Login.vue')
const Category = () => import('@/views/Category/Category.vue')
const Subcategory = () => import('@/views/Category/Subcategory.vue')
const Search = () => import('@/views/Search.vue')


const routes = [
  {
    path: '/',
    name: 'Layout',
    component: Layout,
    children:[
      {
        path:'/',
        component:Home
      },{
        path:'/category/:id',
        component:Category,
        children:[
          {
            path:'/category/:id/subcat/:subid',
            component:Subcategory
          }
        ],
      },
      {
        path:'/search/:keyword',
        component:Search
      }
    ]
  }, {
    path: '/login',
    component: Login
  }

]

const router = createRouter({
  // Hash模式
  history: createWebHashHistory(),
  routes
})

export default router