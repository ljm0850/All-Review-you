<template>
<div v-if="isProfile" class="container my-3 cus-blur">
  <div v-if="sameUser" class="row">
    <div class="fa-solid fa-address-book fa-4x my-3"></div>
    <div class="fa-solid my-3">
    m y - p r o f i l e
    </div>
  </div>
  <div v-if="!sameUser" class="row">
    <div class="fa-solid fa-address-book fa-4x my-3"></div>
    <div class="fa-solid my-3">
    {{username}}' s - p r o f i l e
    </div>
  </div>
  <div class="row justify-content-center">
  <div class="col-1 fa-solid fa-user-plus"> {{profile.data.followings.length}}</div>
  <div class="col-1 fa-solid fa-users"> {{profile.data.followers}}</div>
  <div class="col-1 fa-solid fa-thumbs-up"> {{this.profile.data.rank_point}}</div>
  </div>
  <div v-if="!followed" class="btn cus-item-color2 cus-blur" @click="requestFollow(username)">follow</div>
  <div v-if="followed" class="btn cus-item-color2 cus-blur" @click="requestFollow(username)">unfollow</div>
  <div v-if='!isList'>
    <ReviewItem 
    v-for="reviewitem in reviewlist"
    :key="reviewitem.id"
    :Reviewitem="reviewitem"
    />
  </div>

  <div class="accordion">
    <div class="accordion-item cus-blur">
      <h2 class="accordion-header" id="headingOne">
        <button class="cus-blur" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
          who is following '{{ username }}'
        </button>
      </h2>
      <div v-if='isFollowList'>
    <FollowItem v-for="(followuser) in followlist"
    :key="followuser"
    :followuser="followuser"/>
  </div>
    </div>
  </div>

  <div v-if="sameUser" class="accordion">
    <div class="accordion-item cus-blur">
      <h2 class="accordion-header" id="headingOne">
        <button class="cus-blur" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="true" aria-controls="collapseOne">
          My follow list
        </button>
      </h2>
      <div v-if='isFollowList'>
    <FollowingItem v-for="(followuser) in followinglist"
    :key="followuser"
    :followuser="followuser"/>
  </div>
    </div>
  </div>

  <router-link v-if='sameUser' class="btn cus-item-color2 cus-blur" :to="{ name: 'userupdate', params: {username: this.username} }">정보 수정하기</router-link>
  <form v-if="isSuperUser">
    <div><input v-model="page" type="number" max="1000" min="0" required /></div>
    <button @click.prevent="setMovie" class="btn cus-item-color2 cus-blur">영화 정보 업데이트</button>
  </form>
</div>  
</template>

<script>
import _ from 'lodash'
import axios from 'axios'
import drf from '@/api/drf'
import { mapGetters,mapActions} from 'vuex'
import ReviewItem from '@/components/ReviewItem.vue'
import FollowItem from '@/components/FollowItem.vue'
import FollowingItem from '@/components/FollowingItem.vue'
export default {
  name: 'ProfileView',
  props:['username'],
  components: {
      ReviewItem,FollowItem,FollowingItem
    },
  data() {
    return {
      profile: {},
      page: 0,
    }
  },
  computed: {
    ...mapGetters(['currentUser',]),
    isSuperUser: function() {
      return this.profile.data.is_superuser
    },
    sameUser: function(){
      return Boolean(this.username === this.currentUser.username)
    },

    reviewlist: function(){
      return this.profile.reviews
    },
    followlist: function(){
      return this.profile.followlist
    },

    followinglist: function(){
      return this.profile.data.followings
    },

    isList: function(){
      return _.isEmpty(this.reviewlist)
    },

    isFollowList: function(){
      return ! _.isEmpty(this.followlist)
    },

    isProfile: function(){
      return !_.isEmpty(this.profile)
    },

    followed: function(){
      const temp = []
      this.followlist.forEach((followitem)=>
        temp.push(followitem.username)
      )
      if (temp.includes(this.currentUser.username)){
        return true
      }
      return false
    },
  },
  watch:{
    '$route': 'getProfile'
  },
  methods: {
    ...mapGetters(['authHeader']),
    ...mapActions(['requestFollow']),
    getProfile() {
      axios({
        url: drf.accounts.profile(),
        headers: this.authHeader(),
        method: 'get',
        params: {
          you: this.username,
        }
      })
        .then(res => {
          this.profile = res.data
        })
        .catch(res => {
          this.$router.push({name:'login'})
          console.log(res)
        })
    },
  
    requestFollow(username){
      axios({
        url: drf.accounts.follow(),
        method: 'post',
        data: {
          "username": username
        },
        headers: this.authHeader(),
      })
      .then(()=>{
        this.getProfile()
      })
        .catch(err =>{
        console.log(err)
        alert('사용자 없습니다. 관리자에게 문의하세요')
      })
    },
      setMovie() {
      axios({
        url: drf.movies.setmovie(),
        method: 'post',
        data: {
          page: this.page,
        },
        headers: this.authHeader(),
      })
      .then(()=>{
        alert('업데이트 완료')
      })
        .catch(err =>{
        console.log(err)
        alert('업데이트 실패')
      })
    }  


  },
  created() {
    this.getProfile()
  }

}
</script>

<style>

</style>