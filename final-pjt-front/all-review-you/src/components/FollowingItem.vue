<template>
  <div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingOne" data-bs-parent="#accordionExample">
    <div class="accordion-body cus-blur">
      <router-link :to="{ name: 'profile', params: {username: followuser.username} }" class="text-decoration-none text-dark cus-title">{{ followuser.username }}</router-link>
    </div>
  </div>
</template>



<script>
export default {
  name: 'FollowItem',
  props: {
    followuser: Object
  }
}
</script>

<style>

</style>