<template>
  <div class="cus-blur">
    <div class="detail fs-4">
      <div>{{ videoTitle }}</div>
    </div>
    <div class="ratio ratio-16x9">
      <iframe :src="videoSrc" frameborder="0"></iframe>
    </div>
      <div>{{ videoDescription }}</div>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'
export default {
  name: 'VideoDetail',
  computed: {
    ...mapGetters(['selectedVideo','videoSrc','videoTitle','videoDescription']),
  },
  methods: {
    
  }
}
</script>

<style>

</style>