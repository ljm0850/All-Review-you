<template>
  <div v-if="isVideos" class="container">
    <div class="row justify-content-between">
      <div class="col-12 col-xs-12 col-md-9">
        <YoutubePlayer v-if="isSelectedVideo" />
      </div>
      <div class="col-12 col-xs-12 col-md-3">
        <YoutubeList />
      </div>
    </div>
  </div>
</template>

<script>
import YoutubeList from '@/components/YoutubeList.vue'
import YoutubePlayer from '@/components/YoutubePlayer.vue'
import {mapActions,mapGetters} from 'vuex'
export default {
  
  name:'YoutubeMain',
  components: { YoutubeList,YoutubePlayer },
  computed: {
    ...mapGetters(['isSelectedVideo','isVideos'])
  },
  methods: {
    ...mapActions(['saveVideos']),
  },
}
</script>

<style>

</style>