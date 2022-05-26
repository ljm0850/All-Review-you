<template>
  <div class="list-group cus-blur">
    <YoutubeItem class="cus-item"
      v-for="video in videos"
      :key="video.etag"
      :video="video"
    />
  </div>
</template>

<script>
import YoutubeItem from "@/components/YoutubeItem.vue"
import { mapGetters } from 'vuex'
export default {
  name: 'YoutubeList',
  components:{ YoutubeItem },
  computed:{
    ...mapGetters(['videos'])
  },
}
</script>

<style>

</style>