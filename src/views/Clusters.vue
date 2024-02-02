<template>
  <div class="py-4 container-fluid">
    <div class="row">
      <div class="col-lg-12">
        <div class="row">
          <div class="col-lg-3 col-md-6 col-12">
            <card
              :title="stats.money.title"
              :value="stats.money.value"
              :percentage="stats.money.percentage"
              :iconClass="stats.money.iconClass"
              :iconBackground="stats.money.iconBackground"
              :detail="stats.money.detail"
              directionReverse
            >
            </card>
          </div>
          <!-- 
          <div class="col-lg-3 col-md-12 col-12">
              <div class="mb-4 card">
                <div class="p-3 card-body">
                  <div class="px-4">
                    <div class="mb-3 mt-4">
                      
                    
                   
                      <router-link to="/cluster-create">
                        <argon-button color="success" size="md" variant="gradient"
                        >Create New Cluster</argon-button>
                      </router-link>

                    </div>
                  </div>
                </div>
              </div>
            </div> -->

          <div class="py-4 container-fluid">
            <div class="row">
              <div class="col-12">
                <authors-table />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Card from "@/examples/Cards/Card.vue";
import AuthorsTable from "./components/AuthorsTable.vue";
// import ArgonButton from "@/components/ArgonButton.vue";

export default {
  name: "Cluster",
  components: {
    Card,
    AuthorsTable,
    // ArgonButton
  },
  data() {
    return {
      stats: {
        money: {
          title: "All Clusters",
          value: "12",
          percentage: "",
          iconClass: "ni ni-money-coins",
          detail: "since today",
          iconBackground: "bg-gradient-primary",
        },
      },
    };
  },
};
</script>
