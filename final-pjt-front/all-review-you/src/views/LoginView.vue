<template>
  <div class="container my-3 cus-blur">
    <div class="row">
    <div class="fa-solid fa-key fa-3x my-3"></div>
    <div class="fa-solid my-3"> L o g i n </div>
    </div>
    <account-error-list v-if="authError"></account-error-list>
    <form @submit.prevent="login(credentials)">
      <div class="m-3">
        <label for="username" class="form-label fa-solid"> u s e r - n a m e</label>
        <input v-model="credentials.username" type="text" id="username" class="form-control" required />
      </div>
      <div class="m-3">
        <label for="password" class="form-label fa-solid"> p a s s w o r d </label>
        <input v-model="credentials.password" type="password" id="password" class="form-control" required />
      </div>
      <button class="btn cus-item-color2 cus-blur">Login</button>
    </form>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'LoginView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password: '',
        }
      }
    },
  computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['login'])
    },
  }
</script>

<style></style>
