<template>
<div>
  review delete
</div>  
</template>

<script>
import axios from 'axios'
import drf from '@/api/drf'

import { mapGetters,mapActions } from 'vuex'

export default {
  name: 'ReviewDeleteView',
  props: ['pk'],
  methods: {
    ...mapGetters(['isLoggedIn', 'authHeader']),
    ...mapActions(['saveTopList']),
    reviewdelete() {
      axios({
        url : drf.reviews.reviewdetail(),
        method : 'delete',
        headers: this.authHeader(),
        data: {
          pk: this.pk,
        }
      })
        .then(() => {
          this.saveTopList()
          this.$router.push({name : 'board'})
        })
        .catch(err =>{
          console.log(err)
        })
                
    }
  },
  computed: {
  },
  created() {
    if (this.isLoggedIn) {
      this.reviewdelete()
    } else {
      alert('잘못된 접근')
      this.$router.back()
    }
  },
}
</script>

<style>

</style>