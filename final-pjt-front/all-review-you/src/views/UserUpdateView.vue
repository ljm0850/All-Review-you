<template>
  <div class="container my-3 cus-blur">
    <p class="fa-solid">{{ this.username }} ' s - u p d a t e - p a g e</p>
    <div class="row cus-blur">
      <form>
        <div class="m-3">
          <label class="form-label fa-solid" for="first-name"> f i r s t - n a m e </label>
          <input class="form-control" v-model="info.first_name" type="text" id="first-name" required />
        </div>

        <div class="m-3">
          <label class="form-label fa-solid" for="last-name"> l a s t - n a m e </label>
          <input class="form-control" v-model="info.last_name" type="text" id="last-name" required />
        </div>
        <button class="btn cus-item-color2 cus-blur" @click.prevent="changeInfo">change information</button>
      </form>
    </div>
    <div class="row cus-blur">
      <form>
        <div class="m-3">
          <label class="form-label fa-solid" for="new-password1"> n e w - p a s s w o r d </label>
          <input class="form-control" v-model="credentials.new_password1" type="password" id="new-password1" required />
        </div>

        <div class="m-3">
          <label class="form-label fa-solid" for="new-password2">n e w - p a s s w o r d - c h e c k </label>
          <input class="form-control" v-model="credentials.new_password2" type="password" id="new-password2" required />
        </div>
        <button class="btn cus-item-color2 cus-blur" @click.prevent="changePassword"> change password</button>
      </form>
    </div>
  </div>
    
</template>

<script>
import axios from 'axios'
import drf from '@/api/drf'
import { mapGetters } from 'vuex'
export default {
  name: 'UserUpdateView',
  props: ['username'],

  data() {
    return {
    info: {
      email: '',
      first_name: '',
      last_name: '',
    }, 
    credentials: {
      new_password1: '',
      new_password2: '',
    },
    }
  },
  methods: {
    ...mapGetters(['authHeader', 'currentUser']),
    changePassword() {
      axios({
        url: drf.accounts.changepassword(),
        headers: this.authHeader(),
        method: 'post',
        data: this.credentials,
      })
        .then(res => {
          console.log(res)
          alert("비밀번호 변경 완료")
        })
        .catch(err => {
          console.log(err)
          alert("잘못된 요청입니다")
        })   
    },

    changeInfo() {
      axios({
        url: drf.accounts.currentUserInfo(),
        method: 'patch',
        headers: this.authHeader(),
        data: this.info,    
      })
        .then(res =>{
          console.log(res)
          alert("정보 변경 완료")
        })
        .catch(err => {
          console.log(err)
          alert("정보 변경 실패")
        })
    },

    getInfo() {
      const info = this.currentUser()
        this.info.email = info.email
        this.info.first_name = info.first_name
        this.info.last_name = info.last_name
    },
  },

  created() {
    this.getInfo()
  },
}
</script>

<style>

</style>