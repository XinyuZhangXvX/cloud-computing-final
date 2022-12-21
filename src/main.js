import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
// 引入初始化样式
import '@/assets/styles/base.css'

// 引入elementui
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

// 引入全局组件
import myElement from '@/components/library'
import BaseCard from "./components/ui/BaseCard";
import BaseSpinner from "./components/ui/BaseSpinner";
import BaseMessage from "./components/ui/BaseMessage";


createApp(App).use(store).use(router).use(ElementPlus).use(myElement).component("base-card", BaseCard).component("base-spinner", BaseSpinner)
.component("base-message", BaseMessage).mount('#app')
