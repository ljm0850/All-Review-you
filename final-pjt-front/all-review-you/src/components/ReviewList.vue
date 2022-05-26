<template>
<div class="container cus-blur">
  <div v-if='isList'>
    <h3>리뷰가... 아직 없어요</h3>
  </div>
  <div v-if='!isList'>
    <ReviewItem 
    v-for="reviewitem in reviewlist"
    :key="reviewitem.id"
    :Reviewitem="reviewitem"
    />
  </div>
</div>
</template>

<script>
import ReviewItem from '@/components/ReviewItem.vue'

import axios from 'axios'
import drf from '@/api/drf'
import _ from 'lodash'



  export default {
    name: 'ReviewList',
    components: {
      ReviewItem,
    },
    data() {
      return {
        reviewlist: {},
      }
    },
    computed: {
      isList() {
        return _.isEmpty(this.reviewlist)
      },
    },
    methods: {
      getReview() {
        axios({
          url: drf.reviews.reviewindex(),
          method: 'get',
        })
          .then(res => {
            this.reviewlist = res.data
          })
          .catch(res => {
            console.log(res)
            alert("리뷰가 없습니다. 리뷰를 작성해보세요")
          })
      },
    },
    created() {
      this.getReview()
    }
  }

</script>

<style>

</style>