<template>
<div class="container my-3 cus-blur">
  <div class="fa-solid">r e v i e w</div>
  <div class="row cus-blur">
    <form @submit.prevent="createReview(credentials)">
      <div class="m-3">
        <label class="form-label fa-solid" for="title"> t i t l e</label>
        <input class="form-control" v-model="credentials.title" type="text" id="title" required/>
      </div>
      <div class="m-3">
        <label class="form-label fa-solid" for="content"> c o n t e n t</label>
        <input class="form-control" v-model="credentials.content" type="text" id="content" required />
      </div>
      <div class="m-3">
        <label class="form-label fa-solid" for="point"> s c o r e </label>
        <input class="form-control" v-model="credentials.point" type="number" max="10" min="0" id="point" required />
      </div>
      <div>
        <button class="btn cus-item-color2 cus-blur">submit</button>
      </div>
    </form>
  </div>
</div> 
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
export default {
  name:'ReviewCreate',

  data() {
      return {
        credentials: {
          movie: '',
          title: '',
          content: '',
          point: '',
        },
      }
    },

  computed: {
    ...mapGetters(['selectMovieId']),
  },
  methods: {
    ...mapGetters(['isLoggedIn']),
    ...mapActions(['createReview','saveMovieId'])
  },
  created() {
    if (!this.isLoggedIn()) {
      this.$router.push({name : 'login'})
    }
    if (this.$route.params.MoviePk){
      this.saveMovieId(this.$route.params.MoviePk)
    }
    this.credentials.movie = this.selectMovieId
  }
}
</script>

<style>

</style>