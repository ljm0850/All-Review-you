<template>
  <div class="card col-6 col-lg-3 col-xl-2">
    <img v-if="page==='home'" :src="posterPath" alt="영화 포스터" @click="searchTitle(movie.title)">
    <img v-if="page==='board'" :src="posterPath" alt="영화 포스터" @click="createReview()">
    <div class="card-body">
      <h5 class="card-title">{{ movie.title }}</h5>
    </div>
</div>
</template>

<script>
import drf from '@/api/drf'
import {mapActions} from 'vuex'
export default {
  name: 'AdminRecommend',
  props: {
    movie: Object,
    page: String,
  },
  computed: {
    posterPath() {
      return drf.movies.poster() + this.movie.poster_path
    }
  },
  methods:{
    ...mapActions(['searchTitle']),
    createReview(){
      this.$router.push({ name: 'reviewcreate', params: {MoviePk:this.movie.pk } })
    },
  }
}
</script>

<style>

</style>