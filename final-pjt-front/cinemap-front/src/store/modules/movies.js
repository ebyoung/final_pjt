import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'
// import _ from 'lodash'


export default {
  // namespaced: true,
  state: {
    movies: [],
    targetMovie: {},
    userRecommendations: {},
    mapMovies: [],
  },

  getters: {
    movies: state => state.movies,
    targetMovie: state => state.targetMovie,
    userRecommendations: state => state.userRecommendations,
    mapMovies: state => state.mapMovies,
  },

  mutations: {
    SET_MOVIES: (state, movies) => state.movies = movies,
    SET_TARGET_MOVIE: (state, targetMovie) => state.targetMovie = targetMovie,
    SET_USER_RECOMMENDATIONS: (state, userRecommendations) => state.userRecommendations = userRecommendations,
    SET_MAP_MOVIES: (state, mapMovies) => state.mapMovies = mapMovies,
  },

  actions: {
    fetchMovies({ commit, getters }) {
      axios({
        url: drf.movies.movies(),
        method: 'get',
        headers: getters.authHeader,
      })
      .then(res => {
        commit('SET_MOVIES', res.data)
      })
    },
    fetchTargetMovies({ commit, getters }, movieId) {
      const targetMovie = getters.movies.filter(movie => movie.movie_id === movieId)[0]
      commit('SET_TARGET_MOVIE', targetMovie)
    },

    getUserRecommendations({ commit, getters }) {
      axios({
        url: drf.movies.recommendations(),
        method: 'get',
        headers: getters.authHeader,
      })
      .then(res => {
        commit('SET_USER_RECOMMENDATIONS', res.data)
      })
    },

    moveToRecom(store, movieId) {
      router.push({ name:'recomView', params: { movieId } }).catch(()=>{})
      router.go()
    },

    getMapMovies({ commit, getters }) {
      axios({
        url: drf.movies.mapMovies(),
        method: 'get',
        headers: getters.authHeader,
      })
      .then(res => {
        commit('SET_MAP_MOVIES', res.data)
      })
    }
  },
}
