import { createRouter,createWebHistory } from "vue-router";
import App  from "..//App.vue"
import Auction from "../views/Auction.vue"
import Product from "../views/Product.vue"
// Import doesnt work.
// Try typing import name of file.


const routes = [
    // { path: '/',name:'App', component: App, },
    { path: '/Auction',name:'Auction',component:Auction,},
    {path:'/Product', name:'Product',component:Product,}, 
  ]
const router = createRouter({
    // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
    history: createWebHistory(),
    routes // short for `routes: routes`
  })


  
  
export {router}