import { createRouter, createWebHistory } from "vue-router";
import Dashboard from "../views/Dashboard.vue";
// import Tables from "../views/Tables.vue";
import Billing from "../views/UserDashboard/Billing.vue";
import ClusterSetting from "../views/UserDashboard/ClusterSetting.vue";

// Made by ashish
import Clusters from "../views/Clusters.vue";
import Projects from "../views/Projects.vue";
import UserManagement from "../views/UserMgmt.vue";
import Signin from "../views/Signin.vue";

import Profile from "../views/Profile.vue";

const routes = [
  {
    path: "/",
    name: "/",
    redirect: "/signin",
  },
  {
    path: "/admin-dashboard",
    name: "Dashboard",
    component: Dashboard,
  },
  // {
  //   path: "/tables",
  //   name: "Tables",
  //   component: Tables,
  // },
  {
    path: "/Cluster-Create",
    name: "Cluster-Create",
    component: Billing,
  },
  {
    path: "/Cluster-Setting",
    name: "Cluster-Setting",
    component: ClusterSetting,
  },

  {
    path: "/Clusters",
    name: "Clusters",
    component: Clusters,
  },
  {
    path: "/User-Management",
    name: "User-Management",
    component: UserManagement,
  },
  {
    path: "/Projects",
    name: "Projects",
    component: Projects,
  },

  {
    path: "/profile",
    name: "Profile",
    component: Profile,
  },
  {
    path: "/signin",
    name: "Signin",
    component: Signin,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  linkActiveClass: "active",
});

export default router;
