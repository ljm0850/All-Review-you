<template>
  <div class="container my-3 cus-blur">
    <div class="row">
      <div class="fa-solid fa-address-card fa-5x my-3"></div>
      <div class="fa-solid my-3">S i g n - u p</div>
    </div>
    <account-error-list class="text-danger" v-if="authError"></account-error-list>
    <form @submit.prevent="signup(credentials)">
      <div class="m-3">
        <label class="form-label fa-solid" for="username"> U s e r - n a m e </label>
        <input class="form-control" v-model="credentials.username" type="text" id="username" required/>
      </div>
      <div class="m-3">
        <label class="form-label fa-solid" for="password1"> P a s s w o r d </label>
        <input class="form-control" v-model="credentials.password1" type="password" id="password1" required />
      </div>
      <div class="m-3">
        <label class="form-label fa-solid" for="password2"> P a s s w o r d -  C o n f i r m a t i o n</label>
        <input class="form-control" v-model="credentials.password2" type="password" id="password2" required />
      </div>
      <div>
        <button class="btn cus-item-color2 cus-blur">Signup</button>
      </div>
    </form>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'SignupView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password1: '',
          password2: '',
        }
      }
    },
    computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['signup'])
    },
  }
</script>

<style></style>
