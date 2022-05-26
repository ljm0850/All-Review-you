<template>
  <div v-if="isReviewDetail" class="container my-3 cus-blur">
    <div class="row">
    <h1>{{ reviewDetail.movie.title }}</h1>
    <div class="fa-solid fa-face-grin-hearts fa-4x my-3 cus-curs" v-if="checklike" @click="inLikeList">
    </div>
    <div class="fa-solid fa-face-meh fa-4x my-3 cus-curs" v-if="!checklike" @click="inLikeList">
    </div>
    <div class="fa-soild mt-3">title</div>
    <div class="fs-2">{{ reviewDetail.title }}</div>
    <div class="my-3"></div>
    <div class="fa-soild mt-3">content</div>
    <div class="fs-3">{{ reviewDetail.content}}</div>
    <div class="my-3"></div>
    <div class="fa-soild mt-3">author</div>
    <div class="fs-5">{{ writer }}</div>
    <div class="my-3"></div>
    <div class="fa-soild mt-3">like!</div>
    <div class="fs-1">{{ reviewDetail.point}}</div>
    <div class="my-3"></div>
    <div>생성 시각: {{ createdDate }}</div>
    <div>수정 시각: {{ updatedDate }}</div>
    <div class="my-3"></div>
    <div class="my-3 fa-solid my-3">c o m m e n t s</div>

    <CommentItem v-for="(comment, idx) in commentList"
    :key="comment.id"
    :comment="comment"
    :idx="idx"
    />
    <div class="">
    <CommentCreate :pk='String(pk)' />
    </div>
    <div>
      <button v-if="sameUser" class="btn cus-item-color2 cus-blur" @click="updateReview()">update</button>
      <button v-if="sameUser" class="btn cus-item-color2 cus-blur" @click="deleteReview()">delete</button>
    </div>
    </div>
  </div>
</template>

<script>

import axios from 'axios'
import drf from '@/api/drf'
import CommentItem from '@/components/CommentItem.vue'
import CommentCreate from '@/components/CommentCreate.vue'
import { mapGetters } from 'vuex'
import _ from 'lodash'

export default {
  name: 'ReviewDetailView',
  components: {
    CommentItem,CommentCreate,
  },
  props: ['pk',],
  data() {
   return {
     page: 0,
     likeList: [],
     reviewDetail: {},
   }
  },
  computed:{
    ...mapGetters(['commentList']),
    sameUser(){
      return this.reviewDetail.user?.username === this.currentUser()?.username
    },
    writer(){
      return this.reviewDetail.user?.username
    },
    createdDate(){
      return this.reviewDetail?.created_at.slice(0,10)
    },
    updatedDate(){
      return this.reviewDetail?.updated_at.slice(0,10)
    },
    checklike() {
    const user = this.currentUser()
    return this.likeList.includes(user.pk)
    },

    isReviewDetail(){
      return ! _.isEmpty(this.reviewDetail)
    }
  },

  watch: {
    '$route' : 'getDetail'
  },
  methods: {
    deleteReview(){
      this.$router.push({ name: 'reviewdelete', params: {reviewId:this.reviewDetail.id} })
    },
    updateReview(){
      this.$router.push({ name: 'reviewupdate', params: {reviewId:this.reviewDetail.id, title:this.reviewDetail.title, content:this.reviewDetail.content} })
    },



    ...mapGetters(['currentUser', 'authHeader', 'isLoggedIn']),
    inLikeList() {
      const user = this.currentUser()

      axios({
        url: drf.reviews.reviewlike(),
        method: 'post',
        headers: this.authHeader(),
        data: {
          review: this.reviewDetail.id,
        },    
      })
        .then(res =>{
          console.log(res)
          if (this.likeList.includes(user.pk)) {
          const idx = this.likeList.indexOf(user.pk)
          this.likeList.splice(idx, 1)
          this.likestatus = false
          } else {
          this.likeList.push(user.pk)
          this.likestatus = true
          }
        })
        .catch(err => {
          console.log(err)
          alert("잘못된 요청입니다.")
        })      

      
    },
    getDetail() {
      axios({
        url: drf.reviews.reviewdetail(),
        method: 'get',
        headers: this.authHeader(),
        params: {
          pk: this.pk,
        },
      })
        .then(res => {
          this.reviewDetail = res.data
          this.likeList = res.data.like_users
        })
        .catch(err =>{
          console.log(err)
        })

    },
  },
  created() {
    if(!this.isLoggedIn()) {
      this.$router.push({name : 'login'})
    } else {
      this.getDetail()
    }

  }
 }
</script>

<style>

</style>