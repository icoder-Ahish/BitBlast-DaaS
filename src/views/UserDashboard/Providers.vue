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

          <div class="py-4 container-fluid">
            <div class="row">
              <div class="col-12">
                <authors-table />
              </div>
            </div>
          </div>

          <div class="py-4 container-fluid">
            <div class="row">
              <div class="col-12">
                <authors-table />
              </div>
            </div>
          </div>

          <div class="py-4 container-fluid">
            <div class="row">
              <div class="col-12">
                <authors-table />
              </div>
            </div>
          </div>

          <div class="py-4 container-fluid">
            <div class="row">
              <div class="col-12">
                <authors-table />
              </div>
            </div>
          </div>

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
import AuthorsTable from "@/views/components/ProjectTable.vue";
// import ArgonInput from "@/components/ArgonInput.vue";
// import ArgonButton from "@/components/ArgonButton.vue";

export default {
  name: "Cluster",
  components: {
    Card,
    AuthorsTable,
    // ArgonInput,
    // ArgonButton,
  },
  data() {
    return {
      stats: {
        money: {
          title: "All Providers",
          value: "1",
          percentage: "35%",
          iconClass: "ni ni-money-coins",
          detail: "since today",
          iconBackground: "bg-gradient-primary",
        },
      },
    };
  },
};
</script>
