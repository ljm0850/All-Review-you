<template>
  <div class="container cus-blur">
    <div class="fa-solid my-3">T o p ' s - L i s t </div>
    <div class="row justify-content-center">
      <TopRecommend class="cus-item cus-item-color2" v-for="movie in topList" :key="movie.title" :movie="movie" :page="page" />
    </div>
  </div>
</template>

<script>
import TopRecommend from '@/components/TopRecommend.vue'
import { mapGetters } from 'vuex'
export default {
  name:'TopList',
  props:{
    page: String,
  },
  components: { TopRecommend },
  computed: {
    ...mapGetters(['topList'])
  },
}
</script>

<style>

</style>