import drf from '@/api/drf'
import axios from 'axios'
import _ from 'lodash'
export default {
  state: {
    videos : [],
    selectedVideo: {},
    searchTitle : 'ssafy',
  },

  getters: {
    videos: state => state.videos,
    selectedVideo: state => state.selectedVideo,
    searchtitle: state => state.searchTitle, 
    videoSrc: state => drf.youtube.videoId()+state.selectedVideo.id.videoId,
    videoTitle: state => _.unescape(state.selectedVideo.snippet.title),
    videoDescription: state => _.unescape(state.selectedVideo.snippet.description),
    isSelectedVideo: state => !_.isEmpty(state.selectedVideo),
    isVideos: state => !_.isEmpty(state.videos),
  },

  mutations: {
    SET_VIDEOS: (state, videos) => state.videos = videos,
    SELECT_YTB: (state, ytb) => state.selectedVideo = ytb,
    SET_SEARCH_TITLE: (state, title) => state.searchTitle = title,
  },

  actions: {
    saveVideos({getters,commit}) {
      axios.get(drf.youtube.youtubeurl(), {
        params: {
          key: drf.youtube.apikey(),
          type: 'video',
          part: 'snippet',
          q: getters.searchtitle +' 리뷰',
        }
      })
      .then(res=>{
        commit('SET_VIDEOS', res.data.items)
      })
    },
    searchTitle({commit,dispatch},ytb) {
      commit('SET_SEARCH_TITLE',ytb)
      dispatch('saveVideos')
    },
    
    selectVideo({commit},ytb){
      commit('SELECT_YTB',ytb)
      
    },

  }
}