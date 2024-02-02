<template>
  <div
    class="collapse navbar-collapse w-auto h-auto h-100"
    id="sidenav-collapse-main"
  >
    <ul class="navbar-nav">
      <li class="nav-item" v-if="username === 'admin'">
        <sidenav-item
          url="/admin-dashboard"
          :class="getRoute() === 'admin-dashboard' ? 'active' : ''"
          :navText="'Dashboard'"
        >
          <template v-slot:icon>
            <i class="ni ni-tv-2 text-primary text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>
      <li class="nav-item" v-else>
        <sidenav-item
          url="/admin-dashboard"
          :class="getRoute() === 'admin-dashboard' ? 'active' : ''"
          :navText="'Overview'"
        >
          <template v-slot:icon>
            <i class="ni ni-tv-2 text-primary text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>

      <!-- <li class="nav-item">
        <sidenav-item
          url="/tables"
          :class="getRoute() === 'tables' ? 'active' : ''"
          :navText="this.$store.state.isRTL ? 'الجداول' : 'Tables'"
        >
          <template v-slot:icon>
            <i
              class="ni ni-calendar-grid-58 text-warning text-sm opacity-10"
            ></i>
          </template>
        </sidenav-item>
      </li> -->

      <!-- <li class="nav-item">
        <sidenav-item
          url="/billing"
          :class="getRoute() === 'billing' ? 'active' : ''"
          :navText=" 'Billing'"
        >
          <template v-slot:icon>
            <i class="ni ni-credit-card text-success text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li> -->

      <li class="nav-item" v-if="username === 'admin'">
        <sidenav-item
          url="/Clusters-Management"
          :class="getRoute() === 'Clusters' ? 'active' : ''"
          :navText="'Clusters Management'"
        >
          <template v-slot:icon>
            <i class="ni ni-umbrella-13 text-info text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>
      <li class="nav-item" v-else>
        <sidenav-item
          url="/Clusters"
          :class="getRoute() === 'Clusters' ? 'active' : ''"
          :navText="'Clusters '"
        >
          <template v-slot:icon>
            <i class="ni ni-umbrella-13 text-info text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>

      <li class="nav-item" v-if="username === 'admin'">
        <sidenav-item
          url="/Project-Management"
          :class="getRoute() === 'Projects' ? 'active' : ''"
          :navText="'Projects Management'"
        >
          <template v-slot:icon>
            <i class="ni ni-vector text-info text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>
      <li class="nav-item" v-else>
        <sidenav-item
          url="/Projects"
          :class="getRoute() === 'Projects' ? 'active' : ''"
          :navText="'Projects '"
        >
          <template v-slot:icon>
            <i class="ni ni-vector text-info text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>

      <li class="nav-item" v-if="username === 'admin'">
        <sidenav-item
          url="/User-Management"
          :class="getRoute() === 'User-Management' ? 'active' : ''"
          :navText="'User Management'"
        >
          <template v-slot:icon>
            <i class="ni ni-ui-04 text-info text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>
      <li class="nav-item" v-else>
        <sidenav-item
          url="/User-Management"
          :class="getRoute() === 'User-Management' ? 'active' : ''"
          :navText="'Providers'"
        >
          <template v-slot:icon>
            <i class="ni ni-ui-04 text-info text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>

      <li class="mt-3 nav-item" v-if="username === 'admin'">
        <h6
          class="text-xs ps-4 text-uppercase font-weight-bolder opacity-6"
          :class="this.$store.state.isRTL ? 'me-4' : 'ms-2'"
        >
          Monitoring & Backup
        </h6>
      </li>
      <li class="mt-3 nav-item" v-else>
        <h6
          class="text-xs ps-4 text-uppercase font-weight-bolder opacity-6"
          :class="this.$store.state.isRTL ? 'me-4' : 'ms-2'"
        >
          Monitoring & Backup
        </h6>
      </li>
      <li class="nav-item" v-if="username === 'admin'">
        <sidenav-item
          url="/profile"
          :class="getRoute() === 'profile' ? 'active' : ''"
          :navText="'Monitoring'"
        >
          <template v-slot:icon>
            <i class="ni ni-single-02 text-dark text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>
      <li class="nav-item" v-else>
        <sidenav-item
          url="/profile"
          :class="getRoute() === 'profile' ? 'active' : ''"
          :navText="'Monitoring'"
        >
          <template v-slot:icon>
            <i class="ni ni-single-02 text-dark text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>
      <li class="nav-item" v-if="username === 'admin'">
        <sidenav-item
          url="/signin"
          :class="getRoute() === 'signin' ? 'active' : ''"
          :navText="'Backup'"
        >
          <template v-slot:icon>
            <i class="ni ni-money-coins text-danger text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>
      <li class="nav-item" v-else>
        <sidenav-item
          url="/signin"
          :class="getRoute() === 'signin' ? 'active' : ''"
          :navText="'Backup'"
        >
          <template v-slot:icon>
            <i class="ni ni-money-coins text-danger text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>
    </ul>
  </div>
  <div class="pt-2 mx-3 mt-3 sidenav-footer">
    <sidenav-card :class="cardBg" textPrimary="Need Help?" />
  </div>
</template>
<script>
import SidenavItem from "./SidenavItem.vue";
import SidenavCard from "./SidenavCard.vue";

export default {
  name: "SidenavList",
  props: {
    cardBg: String,
  },
  data() {
    return {
      title: "BitBlast",
      controls: "dashboardsExamples",
      isActive: "active",

      username: "adminn",
    };
  },
  components: {
    SidenavItem,
    SidenavCard,
  },
  methods: {
    getRoute() {
      const routeArr = this.$route.path.split("/");
      return routeArr[1];
    },
  },
};
</script>
