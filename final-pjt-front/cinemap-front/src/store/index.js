import Vue from 'vue'
import Vuex from 'vuex'

import accounts from './modules/accounts'
import reviews from './modules/reviews'
import movies from './modules/movies'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: { accounts, reviews, movies },
})
