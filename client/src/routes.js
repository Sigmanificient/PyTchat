import { createWebHistory, createRouter } from "vue-router";

const routes = [
  {
    path: "/",
    name: "home",
    component: () => import("@/pages/Home.vue"),
  },
  {
    path: "/tchat",
    name: "tchat",
    component: () => import("@/pages/Tchat.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
