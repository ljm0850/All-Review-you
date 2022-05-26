<template>
<nav class="navbar navbar-expand-lg py-0">
  <div class="container-fluid">
    <div class="navbar-brand" href="#">
    <img alt="Vue logo" src="../assets/logo.png" width="100" height="10%" class="d-inline-block align-text-top rounded-circle">
    </div>
    <div class="d-flex">
      <div class="m-2 cus-title">
      <router-link to="/" class="fa-solid text-decoration-none text-dark fa-2x">H o m e</router-link> 
      </div>
      <div class="fa-solid fa-film fa-2x m-2">
        
      </div>
      <div class="m-2 cus-title">
      <router-link to="/board/" class="fa-solid text-decoration-none text-dark fa-2x">B o a r d</router-link>
      </div>
    </div>
    <ul class="nav-item dropdown my-0">
      <a class="nav-link dropdown-toggle fa-solid fa-rectangle-list text-decoration-none text-dark" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
        i n f o
      </a>
      <ul class="dropdown-menu cus-blur2" aria-labelledby="navbarDropdown">
        <div v-if="isLoggedIn" class="dropdown-item cus-blur mx-0 cus-non">
            <router-link :to="{ name: 'profile', params: {username: this.currentUser.username} }" class="fa-solid fa-circle-user text-decoration-none text-dark cus-non"> P r o f i l e</router-link>
        </div>
        <div v-if="isLoggedIn" class="dropdown-item cus-blur mx-0 cus-non">
          <router-link to="/logout" class="fa-solid fa-arrow-right-from-bracket text-decoration-none text-dark cus-non"> L o g o u t</router-link>
        </div>
        <div v-if="!isLoggedIn" class="dropdown-item cus-blur mx-0 cus-non">
          <router-link to="/login" class="fa-solid fa-key text-decoration-none text-dark cus-non"> L o g i n</router-link>
        </div>
        <div v-if="!isLoggedIn" class="dropdown-item cus-blur mx-0 cus-non">
          <router-link to="/signup" class="fa-solid fa-address-card text-decoration-none text-dark cus-non"> S i g n u p</router-link>
        </div>
      </ul>
    </ul>
  </div>
</nav>

</template>

<script>
  import { mapGetters } from 'vuex'
  export default {
    name: 'NavBar',
    computed: {
      ...mapGetters(['isLoggedIn', 'currentUser']),
      username() {
        return this.currentUser.username ? this.currentUser.username : 'guest'
      },
    },
  }
</script>

<style>

</style>