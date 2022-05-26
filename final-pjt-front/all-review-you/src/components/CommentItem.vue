<template>
  <div class="container">
    <div class="fs-3"> {{ comment.content }}
      <div class="fa-solid fa-eraser cus-curs" v-if="sameUser" @click="removeComment({commentid:comment.id, index:idx})"></div>
    </div>
    <div class="mb-3">{{ createdDate }}</div>
  </div>

</template>

<script>
import {mapActions,mapGetters} from 'vuex'
export default {
  name: 'CommentItem',
  props: {
    comment: Object,
    idx: Number,
  },
  computed:{
    ...mapGetters(['commentList','currentUser']),
    sameUser(){
      return this.currentUser.pk === this.comment.user
    },
    createdDate(){
      return this.comment.created_at.slice(0,10)
    },
  },

  methods:{
    ...mapActions(['removeComment']),
  },
}
</script>

<style>

</style>