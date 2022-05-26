<template>
<div class="row justify-content-between cus-blur cus-item-color3">
  <div class="col-1">
  <button class="btn cus-item-color2" @click="toDetail">Detail</button>
  </div>
  <div  class="col-9 align-self-center fs-3"> {{ Reviewitem.title }}</div>
  <div class="col-1 align-self-center fa-solid fa-heart"> {{ Reviewitem.like_users.length }}</div>
  <div class="col-1 align-self-center fa-solid fa-comment"> {{ commentlist.length }}</div>


</div>
</template>

<script>
import axios from 'axios'
import drf from '@/api/drf'
import {mapActions} from 'vuex'
  export default {
    name: 'ReviewItem',
    props: {
      Reviewitem: Object,
    },
    data() {
      return {
        commentlist: [],
      }
    },
    created() {
      this.getcomment()
    },
    methods: {
      ...mapActions(['saveCommentList']),
      getcomment() {
      axios({
        url: drf.reviews.reviewcomment(),
        method: 'get',
        params: {
          review: this.Reviewitem.id,
        }
      })
        .then(res => {
          this.commentlist = res.data
        })
      },

      toDetail(){
        this.saveCommentList(this.commentlist)
        this.$router.push({ name: 'reviewdetail', params: {pk: this.Reviewitem.id,} })
      },
    }
  }

</script>

<style>

</style>