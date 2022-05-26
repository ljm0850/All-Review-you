import drf from '@/api/drf'
import router from '@/router'
import axios from 'axios'
export default {
  state: {
    commentlist:[],
    selectMovieId:'',
  },

  getters: {
    commentList: state => state.commentlist,
    selectMovieId: state => state.selectMovieId
  },

  mutations: {
    SET_COMMENT_LIST:(state,ls) => state.commentlist = ls,
    ADD_COMMENT_LIST:(state,comment) => state.commentlist.push(comment),
    REMOVE_COMMENT_LIST:(state,index) => state.commentlist.splice(index,1),
    SET_MOVIE_ID:(state,selectId) => state.selectMovieId = selectId 
  },

  actions: {
    createReview({getters,dispatch},credentials){
      axios({
        url:drf.reviews.reviewcreate(),
        method:'post',
        data: credentials,
        headers: getters.authHeader,
      })
      .then(()=> {
        router.push({name:'board'})
        dispatch('saveTopList')
        
      })
      .catch(err => {
        console.error(err.response)
        alert("잘못된 접근입니다.")
      })
    },

    updateReview({getters,dispatch},credentials){
      getters
      axios({
        url:drf.reviews.reviewdetail(),
        method:'put',
        data: credentials,
        headers: getters.authHeader,
      })
      .then(()=> {
        router.push({name:'board'})
        dispatch('saveTopList')
      })
      .catch(err => {
        console.error(err.response)
        alert("잘못된 접근입니다.")
      })
    },

    createComment({getters,commit},credentials){
      axios({
        url:drf.reviews.reviewcomment(),
        method:'post',
        data:credentials,
        headers: getters.authHeader
      })
      .then((res)=>{
        commit('ADD_COMMENT_LIST',res.data)
      })
    },

    saveCommentList({commit},ls) {
      commit('SET_COMMENT_LIST',ls)
      
    },
    removeComment({getters,commit},ob){

      axios({
        url:drf.reviews.commentdetail(),
        method:'delete',
        headers: getters.authHeader,
        params: {
          "pk":ob.commentid
        }
      })
      .then(()=>{
        commit('REMOVE_COMMENT_LIST',ob.index)
      })

    },
    
    saveMovieId({commit},id){
      commit('SET_MOVIE_ID',id)
    }

  },
}