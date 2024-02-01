<template>
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
          <div class="col-lg-3 col-md-6 col-12">
            <card
              :title="stats.provider.title"
              :value="stats.provider.value"
              :percentage="stats.provider.percentage"
              :iconClass="stats.provider.iconClass"
              :iconBackground="stats.provider.iconBackground"
              :percentageColor="stats.provider.percentageColor"
              :detail="stats.provider.detail"
              directionReverse
            ></card>
          </div>
          <div class="col-lg-3 col-md-6 col-12">
            <card
              :title="stats.user.title"
              :value="stats.user.value"
              :percentage="stats.user.percentage"
              :iconClass="stats.user.iconClass"
              :iconBackground="stats.user.iconBackground"
              :detail="stats.user.detail"
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
              <div class="p-3 pb-0 card-header">
                <div class="d-flex justify-content-between">
                  <h6 class="mb-2">See all Details</h6>
                </div>
              </div>
              <!-- Tables -->
              <div class="table-responsive">
                <table class="table align-items-center">
                  <tbody>
                    <tr v-for="(sale, index) in sales" :key="index">
                      <td class="w-30">
                        <div class="px-2 py-1 d-flex align-items-center">
                          <div>
                            <!-- <img alt="img" /> -->
                          </div>
                          <div class="ms-4">
                            <p class="mb-0 text-xs font-weight-bold">Name:</p>
                            <h6 class="mb-0 text-sm">{{ sale.country }}</h6>
                          </div>
                        </div>
                      </td>
                      <td>
                        <div class="text-center">
                          <p class="mb-0 text-xs font-weight-bold">Count:</p>
                          <h6 class="mb-0 text-sm">{{ sale.sales }}</h6>
                        </div>
                      </td>
                      <td>
                        <div class="text-center">
                          <p class="mb-0 text-xs font-weight-bold">Value:</p>
                          <h6 class="mb-0 text-sm">{{ sale.value }}</h6>
                        </div>
                      </td>
                      <!-- <td class="text-sm align-middle">
                          <div class="text-center col">
                            <p class="mb-0 text-xs font-weight-bold">Bounce:</p>
                            <h6 class="mb-0 text-sm">{{ sale.bounce }}</h6>
                          </div>
                        </td> -->
                    </tr>
                  </tbody>
                </table>
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
    // GradientLineChart,

    // CategoriesCard,
  },
};
</script>
