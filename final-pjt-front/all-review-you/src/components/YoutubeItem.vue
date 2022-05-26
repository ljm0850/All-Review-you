<template>
  <div class="video-list-wrap">
      <img :src="videoImgUrl" alt="youtube-thumbnail" @click="selectVideo(video)">
      <div class="media-body">
      </div>
  </div>
</template>

<script>
import _ from 'lodash'
import {mapActions} from 'vuex'
export default {
  name: 'YoutubeItem',
  props: {
    video: Object,
  },
  methods: {
    ...mapActions(['selectVideo']),
  },
  computed: {
    videoImgUrl () {
      return this.video.snippet.thumbnails.default.url
    },
    videoTitle() {return _.unescape(this.video.snippet.title)}
  }

}
</script>

<style>

</style>