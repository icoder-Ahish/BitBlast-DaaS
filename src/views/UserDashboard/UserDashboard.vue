<template>
  <!-- Nav and sidenav -->

  <div class="py-4 container-fluid">
    <div class="row">
      <div class="col-lg-12">
        <div class="row">
          <div class="col-lg-3 col-md-6 col-12">
            <card
              :title="stats.project.title"
              :value="stats.project.value"
              :percentage="stats.project.percentage"
              :iconClass="stats.project.iconClass"
              :iconBackground="stats.project.iconBackground"
              :detail="stats.project.detail"
              directionReverse
            ></card>
          </div>

          <div class="col-lg-3 col-md-6 col-12">
            <card
              :title="stats.cluster.title"
              :value="stats.cluster.value"
              :percentage="stats.cluster.percentage"
              :iconClass="stats.cluster.iconClass"
              :iconBackground="stats.cluster.iconBackground"
              :detail="stats.cluster.detail"
              directionReverse
            ></card>
          </div>
        </div>

        <!-- <div class="row">
              <div class="col-lg-7 mb-lg">
                line chart 
                <div class="card z-index-2">
                  <gradient-line-chart />
                </div>
              </div>
              <div class="col-lg-5">
                <carousel />
              </div>
            </div> -->

        <div class="row mt-4">
          <div class="col-lg-14 mb-lg-0 mb-4">
            <div class="card">
              <div class="card-header">Welcome User</div>
              <div class="card-body">
                <h5 class="card-title">
                  Empower Your Data Journey with BitBlast!!
                </h5>
                <p class="card-text">
                  Experience the transformational power of BitBlast as it
                  propels your data journey forward!
                </p>
                <argon-button color="success" size="md" variant="gradient"
                  >Create New Cluster</argon-button
                >
              </div>
            </div>
          </div>
          <div class="col-lg-5">
            <!-- <categories-card /> -->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import Card from "@/examples/Cards/Card.vue";
// import GradientLineChart from "@/examples/Charts/GradientLineChart.vue";
// import Carousel from "./components/Carousel.vue";
import ArgonButton from "@/components/ArgonButton.vue";

// import CategoriesCard from "./components/CategoriesCard.vue";

export default {
  name: "user-dashboard",
  data() {
    return {
      stats: {
        project: {
          title: "All Project",
          value: "12",
          percentage: "",
          iconClass: "ni ni-project-coins",
          detail: "since today",
          iconBackground: "bg-gradient-primary",
        },
        cluster: {
          title: "All Clusters",
          value: "23",
          percentage: "",
          iconClass: "ni ni-world",
          iconBackground: "bg-gradient-danger",
          detail: "since today",
        },
        provider: {
          title: "All Providers",
          value: "6",
          percentage: "",
          iconClass: "ni ni-paper-diploma",
          percentageColor: "text-danger",
          iconBackground: "bg-gradient-success",
          detail: "since today",
        },
        user: {
          title: "All cluster",
          value: "30",
          percentage: "",
          iconClass: "ni ni-cart",
          iconBackground: "bg-gradient-warning",
          detail: "since today",
        },
      },
      sales: {
        us: {
          country: "Projects",
          sales: 12,
          value: "$20",
          bounce: "29.9%",
        },
        germany: {
          country: "Clusters",
          sales: "23",
          value: "$44",
          bounce: "40.22%",
        },
        britain: {
          country: "cluster",
          sales: "23",
          value: "$19",
          bounce: "23.44%",
        },
        brasil: {
          country: "Providers",
          sales: "6",
          value: "$14",
          bounce: "32.14%",
        },
      },
    };
  },
  components: {
    Card,
    ArgonButton,
    // GradientLineChart,

    // CategoriesCard,
  },
};
</script>
