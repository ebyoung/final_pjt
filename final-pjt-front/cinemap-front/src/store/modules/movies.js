import axios from 'axios'
import drf from '@/api/drf'
// import router from '@/router'
// import _ from 'lodash'


export default {
  // namespaced: true,
  state: {
    movies: [],
    targetMovie: {},
  },

  getters: {
    movies: state => state.movies,
    targetMovie: state => state.targetMovie,
  },

  mutations: {
    SET_MOVIES: (state, movies) => state.movies = movies,
    SET_TARGET_MOVIE: (state, targetMovie) => state.targetMovie = targetMovie,
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
    getMovie({ commit, getters }, movieId) {
      const targetMovie = getters.movies.filter(movie => movie.movie_id === movieId)[0]
      commit('SET_TARGET_MOVIE', targetMovie)
    },
  },
}
