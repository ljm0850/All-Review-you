<template>
<div class="my-3 cus-blur">
  <div class="row justify-content-center">
    <div @click="getRank" class="mx-0 fa-solid fa-chart-line">
    </div>
    <div class="fa-solid">
      R a n k - c h a r t
    </div>
  </div>
  <div v-if='!isList' class="mx-2">
    <RankItem v-for="(rankitem, idx) in ranklist"
    :key="rankitem.username"
    :rankitem="rankitem"
    :idx="idx"
    />
  </div>
</div>
</template>

<script>
import RankItem from '@/components/RankItem.vue'

import axios from 'axios'
import drf from '@/api/drf'
import _ from 'lodash'



  export default {
    name: 'RankList',
    components: {
      RankItem,
    },
    data() {
      return {
        ranklist: {},
      }
    },
    computed: {
      isList() {
        return _.isEmpty(this.ranklist)
      }
    },
    watch:{
      "$route":"getRank"
    },
    methods: {
      getRank() {
        axios({
          url: drf.accounts.ranking(),
          method: 'get',
        })
          .then(res => {
            this.ranklist = res.data
          })
          .catch(res => {
            console.log(res)
            alert("사용자가 없습니다. 회원가입 후 사용해주세요")
          })
      },
    },
    created() {
      this.getRank()
    }
  }

</script>

<style>
</style>