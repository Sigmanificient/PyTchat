import { createWebHistory, createRouter } from "vue-router";

const index = [
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
  routes: index,
});

export default router;
