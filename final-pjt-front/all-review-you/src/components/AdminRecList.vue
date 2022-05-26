<template>
  <div class="container cus-blur">
    <div class="fa-solid"> R e c o m m e n d - L i s t</div>
    <div class="btn cus-item-color2 cus-blur" @click="saveAdminList()">others</div>
    <div class="row justify-content-center">
      <AdminRecommend class="cus-item cus-item-color1" v-for="movie in adminList" :key="movie.title" :movie="movie" :page="page" />
    </div>
  </div>
</template>

<script>
import AdminRecommend from '@/components/AdminRecommend.vue'
import {mapGetters,mapActions} from 'vuex'
export default {
  name:'AdminRecList',
  components:{AdminRecommend},
  props: {
    page: String,
  },
  computed: {
    ...mapGetters(['adminList']),
  },
  methods: {
    ...mapActions(['saveAdminList']),
  },
}
</script>

<style>

</style>