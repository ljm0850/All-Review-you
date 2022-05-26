import Vue from 'vue'
import Vuex from 'vuex'

// import reviews from './modules/reviews'
import accounts from './modules/accounts'
import movies from './modules/movies'
import youtubes from './modules/youtubes'
import reviews from './modules/reviews'
Vue.use(Vuex)
import createPersistedState from 'vuex-persistedstate'

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],

  modules: { accounts,movies,youtubes,reviews },
})
