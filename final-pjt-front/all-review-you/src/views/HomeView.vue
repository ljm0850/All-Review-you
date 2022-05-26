<template>
  <div class="my-2 row">
    <Youtube />
    <TopList page="home"/>
    <AdminRecList page="home"/>
  </div>
</template>

<script>
import TopList from '@/components/TopList.vue'
import AdminRecList from '@/components/AdminRecList.vue'
import Youtube from '@/components/Youtube.vue'

export default {
  name: 'HomeView',
  components: { TopList, Youtube, AdminRecList },
  computed: {
 
  },
}
</script>
