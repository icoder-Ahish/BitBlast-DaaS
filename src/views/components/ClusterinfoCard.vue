<template>
  <div class="card mt-4">
    <div class="card-header pb-0 p-3">
      <div class="row">
        <div class="col-6 d-flex align-items-center">
          <h6 class="mb-0">Create Cluster</h6>
        </div>
        <hr />
        <!-- <div class="col-6 text-end">
          <argon-button color="dark" variant="gradient">
            <i class="fas fa-plus me-2"></i>
            Add New Card
          </argon-button>
        </div> -->
      </div>
    </div>
    <div class="card-body p-3">
      <div class="row">
        <div class="col-md-13 mb-md-0 mb-4">
          <div
            class="card card-body border card-plain border-radius-lg d-flex align-items-center flex-row"
          >
            <div>
              <ul class="nav justify-content-center mt-4">
                <!-- Adjust mt-4 for the desired top space -->
                <li class="nav-item">
                  <router-link
                    class="nav-link"
                    :class="
                      getRoute() === 'Cluster-Create'
                        ? 'text-success'
                        : 'text-muted'
                    "
                    to="/Cluster-Create"
                    >Cluster Info</router-link
                  >
                  <hr
                    :class="
                      getRoute() === 'Cluster-Create'
                        ? 'text-success'
                        : 'text-muted'
                    "
                  />
                </li>
                <li class="nav-item">
                  <router-link
                    class="nav-link"
                    :class="
                      getRoute() === 'Cluster-Setting'
                        ? 'text-success'
                        : 'text-muted'
                    "
                    to="/Cluster-Setting"
                    >Cluster Setting</router-link
                  >
                  <hr
                    :class="
                      getRoute() === 'Cluster-Setting'
                        ? 'text-success'
                        : 'text-muted'
                    "
                  />
                </li>
                &nbsp; &nbsp;
                <li class="nav-item">
                  <a
                    href="#"
                    class="nav-link disabled"
                    aria-disabled="true"
                    :class="
                      getRoute() === 'cluster-dbconfig'
                        ? 'text-success'
                        : 'text-muted'
                    "
                    >DB Configuration</a
                  >
                  <hr />
                </li>
                &nbsp;
                <li class="nav-item">
                  <a href="#" class="nav-link disabled" aria-disabled="true"
                    >Additional Settings</a
                  >
                  <hr />
                </li>
              </ul>
            </div>
            <!-- <img class="w-10 me-3 mb-0" src="@/assets/img/logos/mastercard.png" alt="logo" /> -->
            <!-- <h6 class="mb-0">****&nbsp;&nbsp;&nbsp;****&nbsp;&nbsp;&nbsp;****&nbsp;&nbsp;&nbsp;7852</h6> -->
            <!-- <i
              class="fas fa-pencil-alt ms-auto text-dark cursor-pointer"
              data-bs-toggle="tooltip"
              data-bs-placement="top"
              title
              aria-hidden="true"
              data-bs-original-title="Edit Card"
              aria-label="Edit Card"
            ></i> -->

            <!-- <span class="sr-only">Edit Card</span> -->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import ArgonButton from "@/components/ArgonButton.vue";
import img1 from "@/assets/img/logos/mastercard.png";
import img2 from "@/assets/img/logos/visa.png";

export default {
  name: "payment-card",
  components: {
    // ArgonButton,
  },
  data() {
    return {
      img1,
      img2,
    };
  },
  methods: {
    getRoute() {
      const routeArr = this.$route.path.split("/");
      return routeArr[1];
    },
  },
};
</script>

<style scoped>
.hr_style {
  border: 1px solid green;
}
</style>
