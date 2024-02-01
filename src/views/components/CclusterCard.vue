<template>
  <div class="card">
    <div class="card-header pb-0 px-3">
      <h6 class="mb-0">Select the type of cluster you want to use</h6>
    </div>
    <div class="card-body pt-4 p-3">
      <ul class="list-group">
        <li
          class="list-group-item border-0 d-flex p-4 mb-2 bg-gray-100 border-radius-lg"
        >
          <div class="d-flex flex-column">
            <h6 class="mb-3 text-sm">Cluster type</h6>
            <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4" style="width: 106.6667%">
              <div class="col">
                <div
                  class="h-100 selected w-100 bg-white border-4 rounded-md text-center text-wrap   p-3 
            {{ selectedType === 'Standalone' ? 'selected' : '' }}"
                >
                  <label for="Standalone" class="">
                    <input
                      type="radio"
                      class="visually-hidden"
                      id="Standalone"
                      value="Standalone"
                      v-model="selectedType"
                      @change="updateType"
                    />
                    <p class="pt-2 text-info font-size-18 text-wrap">
                      Standalone cluster
                    </p>
                    <p class="pt-4 text-gray-500 text-sm text-wrap ">
                      A Standalone Node Cluster refers to a cluster
                      configuration in a distributed computing environment where
                      all cluster components, such as databases, services, or
                      applications, run on a Standalone node or machine.
                    </p>
                  </label>
                </div>
              </div>
              <div class="col">
                <div
                  class="h-100 bg-white border-4 rounded-md text-center p-3 
            {{ selectedType === 'multiple' ? 'selected' : '' }}"
                >
                  <label for="multiple">
                    <input
                      type="radio"
                      id="multiple"
                      class="visually-hidden"
                      value="multiple"
                      v-model="selectedType"
                      @change="updateType"
                    />
                    <p class="pt-2 text-info font-size-18 text-wrap">
                      Primary/Standby High Availability
                    </p>
                    <p class="text-gray-500 text-sm text-wrap">
                      A Primary/Standby High Availability (HA) Cluster refers to
                      a configuration in a distributed computing environment
                      where two nodes (or more) operate in tandem to provide
                      fault tolerance and redundancy.
                    </p>
                  </label>
                </div>
              </div>
            </div>
          </div>
        </li>
        <li
          class="list-group-item border-0 d-flex p-4 mb-2 mt-3 bg-gray-100 border-radius-lg"
        >
          <div class="d-flex flex-column">
            <h6 class="mb-3 text-sm">Providers</h6>

            <div
              class="row row-cols-1 row-cols-md-2 g-4"
              style="width: 66.6667%"
            >
              <!-- Cloudstack Provider -->
              <div class="col">
                <div
                  class="bg-white border-4 rounded-md text-center p-3
            {{ selectedProvider === 'Cloudstack' ? 'selected' : '' }}"
                >
                  <label>
                    <input
                      type="radio"
                      class="visually-hidden"
                      id="Cloudstack"
                      value="Cloudstack"
                      v-model="selectedProvider"
                      @change="updateProvider"
                    />
                    <img
                      class="object-contain max-w-full rounded-lg"
                      src="@/assets/img/apple-icon.png"
                      alt=""
                    />
                  </label>
                </div>
              </div>

              <!-- Harvester Provider -->
              <div class="col">
                <div
                  class="ml-md-4 bg-white border-4 rounded-md text-center p-3
            {{ selectedProvider === 'Harvester' ? 'selected' : '' }}"
                >
                  <label>
                    <input
                      type="radio"
                      class="visually-hidden"
                      id="Harvester"
                      value="Harvester"
                      v-model="selectedProvider"
                      @change="updateProvider"
                    />
                    <img
                      class="object-contain max-w-full rounded-lg"
                      src="@/assets/img/apple-icon.png"
                      alt=""
                    />
                  </label>
                </div>
              </div>

              <!-- Vmware Provider -->
              <div class="col">
                <div
                  class="bg-white border-4 rounded-md text-center p-3
            {{ selectedProvider === 'Vmware' ? 'selected' : '' }}"
                >
                  <label>
                    <input
                      type="radio"
                      class="visually-hidden"
                      id="Vmware"
                      value="Vmware"
                      v-model="selectedProvider"
                      @change="updateProvider"
                    />
                    <img
                      class="object-contain max-w-full rounded-lg"
                      src="@/assets/img/apple-icon.png"
                      alt=""
                    />
                  </label>
                </div>
              </div>

              <!-- Kubernetes Provider -->
              <div class="col">
                <div
                  class="ml-md-4 bg-white border-4 rounded-md text-center p-3
            {{ selectedProvider === 'Kubernetes' ? 'selected' : '' }}"
                >
                  <label>
                    <input
                      type="radio"
                      class="visually-hidden"
                      id="Kubernetes"
                      value="Kubernetes"
                      v-model="selectedProvider"
                      @change="updateProvider"
                    />
                    <img
                      class="object-contain max-w-full rounded-lg"
                      src="@/assets/img/apple-icon.png"
                      alt=""
                    />
                  </label>
                </div>
              </div>

              <!-- Nutanix Provider -->
              <div class="col">
                <div
                  class="bg-white border-4 rounded-md text-center p-3
            {{ selectedProvider === 'Nutanix' ? 'selected' : '' }}"
                >
                  <label>
                    <input
                      type="radio"
                      class="visually-hidden"
                      id="Nutanix"
                      value="Nutanix"
                      v-model="selectedProvider"
                      @change="updateProvider"
                    />
                    <img
                      class="object-contain max-w-full rounded-lg"
                      src="@/assets/img/apple-icon.png"
                      alt=""
                    />
                  </label>
                </div>
              </div>

              <!-- Openstack Provider -->
              <div class="col">
                <div
                  class="ml-md-4 bg-white border-4 rounded-md text-center p-3
            {{ selectedProvider === 'Openstack' ? 'selected' : '' }}"
                >
                  <label>
                    <input
                      type="radio"
                      class="visually-hidden"
                      id="Openstack"
                      value="Openstack"
                      v-model="selectedProvider"
                      @change="updateProvider"
                    />
                    <img
                      class="object-contain max-w-full rounded-lg"
                      src="@/assets/img/apple-icon.png "
                      alt=""
                    />
                  </label>
                </div>
              </div>
            </div>
          </div>
        </li>
      </ul>
      <argon-button color="success" size="md" variant="gradient">
        NEXT
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
  }
};
</script>
