<template>
  <div class="card">
    <div class="card-header pb-0 px-3">
      <h6 class="mb-0">Enter the Cluster Name and it's Password.</h6>
    </div>
    <div class="card-body pt-4 p-3">
      <ul class="list-group">
        <li
          class="list-group-item border-0 d-flex p-4 mb-2 bg-gray-100 border-radius-lg"
        >
          <div class="d-flex flex-column">
            <h6 class="mb-3 text-sm">Cluster Name and Password</h6>
            <form>
              <div class="form-group">
                <label for="Cluster_Name"> Cluster Name</label>
                <input
                  class="form-control"
                  type="password"
                  id="example-text-input"
                  placeholder="Enter Your Cluster Name"
                />
              </div>

              <div class="form-group">
                <label for="Postgres_Username"> Postgres Username</label>
                <input
                  type="email"
                  class="form-control"
                  id="Postgres_Username"
                  placeholder="Enter Your Postgres Username"
                />
              </div>

              <div class="form-group">
                <label for="Cluster_Name"> Your Password</label>
                <input
                  type="password"
                  class="form-control"
                  id="Password"
                  placeholder="Enter Your Password "
                />
              </div>
            </form>

            <h6 class="mb-3 text-sm">Database Type and Versions</h6>
            <select class="form-select" aria-label="Default select example">
              <option value="15" selected>15</option>
              <option value="14">14</option>
              <option value="13">13</option>
              <option value="12">12</option>
            </select>
          </div>
        </li>
      </ul>

      <argon-button color="success" size="md" variant="gradient">
        Create Cluster
      </argon-button>
    </div>
  </div>
</template>

<script>
import ArgonButton from "@/components/ArgonButton.vue";

export default {
  name: "billing-card",
  components: {
    ArgonButton,
  },
};
</script>
