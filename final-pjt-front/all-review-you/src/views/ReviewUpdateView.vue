<template>
<div class="container my-3 cus-blur">
  <div class="fa-solid"> r e v i e w - u p d a t e</div>
  <div  class="row cus-blur">
  <form @submit.prevent="updateReview(credentials)">
    <div class="m-3">
      <label class="form-label fa-solid" for="title"> t i t l e </label>
      <input class="form-control" v-model="credentials.title" type="text" id="title" required/>
    </div>
    <div class="m-3">
      <label class="form-label fa-solid" for="content">c o n t e n t </label>
      <input class="form-control" v-model="credentials.content" type="text" id="content" required />
    </div>
    <div class="m-3">
      <label class="form-label fa-solid" for="point"> s c o r e</label>
      <input class="form-control" v-model="credentials.point" type="number" max="10" min="0" id="point" required />
    </div>
    <div>
      <button class="btn cus-item-color2 cus-blur">update</button>
    </div>
  </form>
  </div>

  

</div>  
</template>

<script>
import {mapActions} from 'vuex'
export default {
  name:'ReviewCreate',

  data() {
      return {
        credentials: {
          pk: `${this.$route.params.reviewId}`,
          title: `${this.$route.params.title}`,
          content: `${this.$route.params.content}`,
          point: `${this.$route.params.point}`,
        },
      }
    },

  computed: {

  },
  methods: {
    ...mapActions(['updateReview'])
  }
}
</script>

<style>

</style>