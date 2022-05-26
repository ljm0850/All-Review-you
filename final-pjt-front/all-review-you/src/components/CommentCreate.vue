<template>
  <div class="cus-blur">
      <form @submit.prevent="[createComment(credentials)]">
        <div class="m-3">
        <label class="form-label fs-5" for="content">댓글 작성</label>
        <input class="form-control" v-model="credentials.content" type="text" id="content" required/>
      </div>
      <div>
        <button class="btn cus-item-color2 cus-blur">작성 하기</button>
      </div>
    </form>
  </div>

</template>

<script>
import {mapActions} from 'vuex'
export default {
  name:"CommentCreate",
  data() {
    return {
      credentials: {
        review: this.pk,
        content:''
      }
    }
  },
  props:{
    pk:String
  },

  methods: {
    ...mapActions(['createComment']),
  }
}
</script>

<style>

</style>