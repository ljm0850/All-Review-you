<template>
  <div class="account-error-list">
    <div v-for="(errors, field) in authError" :key="field">
      <div>
        <div v-for="(error, idx) in errors" :key="idx">
          {{ error }}
        </div>
      </div>
    </div>

  </div>
</template>

<script>
  import { mapGetters } from 'vuex'
  
  export default {
    name: 'AccountErrorList',
    computed: {
      ...mapGetters(['authError'])
    },
  }
</script>

<style>
  .account-error-list {
    color: red;
  }
</style>
