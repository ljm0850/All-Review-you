import drf from '@/api/drf'
import axios from 'axios'
import _ from 'lodash'

export default {
  state:{
    adminList: {},
    topList : {},
    ytbTitle : '',
  },
  getters:{
    adminList: state => state.adminList,
    topList: state => state.topList,
    ytbTitle: state => state.ytbTitle,
    emptyAdminList: state => _.isEmpty(state.adminList)
  },
  mutations: {
    SET_ADMIN_LIST:(state,movies) => state.adminList = movies,
    SET_TOP_LIST:(state,movies) => state.topList = movies,
    SET_YTB_TITLE:(state,title) => state.ytbTitle = title,
  },

  actions: {
    saveAdminList({ commit },) {
      axios({
        url: drf.movies.getmovie(),
        method: 'get'
      })
      .then(res=> {
        commit('SET_ADMIN_LIST', res.data)
      })
    },
    
    saveTopList({ commit },) {
      axios({
        url: drf.movies.best(),
        method: 'get'
      })
      .then(res=> {
        commit('SET_TOP_LIST', res.data)
      })
    },
    saveYtbTitle({ commit }, title) {
      commit('SET_YTB_TITLE', title)
    },
    
  },
}