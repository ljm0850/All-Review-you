<template>
<div class="row cus-item my-5">
  <div v-if="idx == 0" class="col-2 fa-solid fa-crown text-warning">  
  </div>
  <div v-if="idx != 0" class="col-2 fa-solid text-dark">
    {{ idx + 1 }}  
  </div>
  <div class="col-7 fa-solid m-0"> 
    <router-link :to="{ name: 'profile', params: {username: rankitem.username} }" class="text-decoration-none text-dark cus-title">{{ rankitem.username }}</router-link>    
  </div>
    <div class="col-1 fa-solid text-dark">{{ rankitem.rank_point }}</div>
    <div class="col-1 fa-solid fa-thumbs-up"></div>


</div>
</template>

<script>
  export default {
    name: 'RankItem',
    props: {
      rankitem: Object,
      idx: Number,
    },
    data() {
      return {
        
      }
    },
  }

</script>

<style>
</style>