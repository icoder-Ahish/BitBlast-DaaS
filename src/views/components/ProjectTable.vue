<template>
    <div class="card">
      <div class="card-header pb-0">
        <h6> Projects info </h6>
      </div>
  
      <div class="card-body px-0 pt-0 pb-2">
        <div class="table-responsive p-0">
          <table class="table align-items-center mb-0">
            <thead>
              <tr>
                <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7"> Projects Name & ID </th>
            
                <th
                  class="text-center text-uppercase text-secondary text-xxs font-weight-bolder opacity-7"
                > Created On</th>
                <th
                  class="text-center text-uppercase text-secondary text-xxs font-weight-bolder opacity-7"
                > Updated On</th>
                
                <th class="text-secondary opacity-7"></th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>
                  <div class="d-flex px-2 py-1">
                    <div>
                      <img
                        src="../../assets/img/db-png.png"
                        class="avatar avatar-sm me-3"
                        alt="user1"
                      />
                    </div>
                    <div class="d-flex flex-column justify-content-center">
                      <h6 class="mb-0 text-sm">66</h6>
                      <p class="text-xs text-secondary mb-0">Project_name</p>
                    </div>
                  </div>
                </td>
               
                <td class="align-middle text-center">
                  <span class="text-secondary text-xs font-weight-bold">23/04/24</span>
                </td>
                <td class="align-middle text-center">
                  <span class="text-secondary text-xs font-weight-bold">23/04/24</span>
                </td>
                <td class="align-middle">
                  <a
                    href="javascript:;"
                    class="text-secondary font-weight-bold text-xs"
                    data-toggle="tooltip"
                    data-original-title="Edit user"
                  >Edit</a>
                </td>
              </tr>
              <tr>
                <td>
                  <div class="d-flex px-2 py-1">
                    <div>
                      <img
                        src="../../assets/img/db-png.png"
                        class="avatar avatar-sm me-3"
                        alt="user1"
                      />
                    </div>
                    <div class="d-flex flex-column justify-content-center">
                      <h6 class="mb-0 text-sm">66</h6>
                      <p class="text-xs text-secondary mb-0">Demo33</p>
                    </div>
                  </div>
                </td>

                <td class="align-middle text-center">
                  <span class="text-secondary text-xs font-weight-bold">23/04/24</span>
                </td>
                <td class="align-middle text-center">
                  <span class="text-secondary text-xs font-weight-bold">23/04/24</span>
                </td>
                <td class="align-middle">
                  <a
                    href="javascript:;"
                    class="text-secondary font-weight-bold text-xs"
                    data-toggle="tooltip"
                    data-original-title="Edit user"
                  >Edit</a>
                </td>
              </tr>
  
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "Projects-table",
  };
  </script>
  