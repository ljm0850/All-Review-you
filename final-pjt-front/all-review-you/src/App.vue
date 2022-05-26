<template>
  <div id="app" class="container">
    <div class="row">
      <NavBar/>
      <div class="container">
        <div class="row">
          <div class="col-12 col-xs-12 col-md-3">
            <RankList/>
          </div>
          <div class="col-12 col-xs-12 col-md-9">
            <router-view/>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import RankList from '@/components/RankList.vue'
import { mapActions,mapGetters } from 'vuex'
  export default {
    name: 'App',
    components: {
       NavBar,
       RankList,
    },
    computed: {
      ...mapGetters(['emptyAdminList'])
    },
    methods: {
    ...mapActions(['saveTopList','saveAdminList']),
    },
    created(){
    this.saveTopList()
    if (this.emptyAdminList){
      this.saveAdminList()
    }
  }
  }
</script>

<style>
body {
  text-align: center;
  font-family: "Do Hyeon", sans-serif;
}

/* 스크롤바 */
body::-webkit-scrollbar {
  width: 15px;
  height: 15px;
}
body::-webkit-scrollbar-thumb {
  background-color: rgb(48,18,82);
  border-radius: 8px;
}
body::-webkit-scrollbar-track {
  background-color: rgb(149,81,112);
}
/* 배경 색 */
body { 
    background: linear-gradient(-15deg, rgb(69,26,117), rgb(149,81,112), rgb(255,217,159), white);
    background-size: 200% 300%;
    animation: gradient 3s ease-in-out infinite;
}

@keyframes gradient {
  0% { background-position: 0% 50%;}
  50% { background-position: 100% 50%;}
  100% { background-position: 0% 50%;}
  }

/* 블러 박스 */
.cus-blur {
  padding: 10px;
  margin: 10px;
  border-style: solid;
  border-color: rgba( 255, 255, 255, 0.3 );
  border-radius: 10px;
  background-color: rgba( 255, 255, 255, 0.1 );
}
.cus-blur2 {
  padding: 10px;
  margin: 10px;
  border-style: solid;
  border-color: rgba( 255, 255, 255, 0.3 );
  border-radius: 10px;
  background-color: rgba(255, 255, 255, 0.8 );
}
img {
  margin: 0px;
  padding: 0px;
  border-radius: 10px;
}
/* item 관리 */
.cus-item {
  margin: 5px;
  padding: 5px;
}
.cus-item-color1 {
  background-color: rgba(48,18,82,0.1);
}
.cus-item-color2 {
  background-color: rgba(120,66,90,0.1);
}
.cus-item-color2:hover {
  background-color: rgba(120,66,90,0.2);
}

.cus-item-color3 {
  background-color: rgba(255,201,116,0.1);
}
.cus-item-color1:hover {
  background-color: rgba(255,201,116,0.1);
}
.cus-title {
  background-color: rgba(255,255,255,0.1);
  border-radius: 10px;
}
.cus-title:hover {
  background-color: rgba(255,255,255,0.5);
  border-radius: 5px;
}
.cus-curs {
  cursor: pointer;
}
.cus-non:active {
  background-color:rgba(255,255,255,0.1);
}
</style>
