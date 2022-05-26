<template>
<div class="container my-3">
  <ReviewList/>
  <TopList page="board"/>
  <AdminRecList page="board"/>
</div>  
</template>

<script>
import ReviewList from '@/components/ReviewList.vue'
import AdminRecList from '@/components/AdminRecList.vue'
import TopList from '@/components/TopList.vue'
export default {
  name: 'BoardView',
  components: {
    ReviewList, AdminRecList, TopList,
  },
}
</script>

<style>

</style>