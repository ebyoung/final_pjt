<template>
  <div>
    <MovieTrailer :videoKey='currentMovie? currentMovie.video_key : targetMovie.video_key' class="trailer"/>
    <h2><span @click="moveToRecom(currentMovie? currentMovie.movie_id : targetMovie.movie_id)">Recommendations</span></h2>
    <RecomList :movie='targetMovie' @changeTrailer='changeTrailer' class="list"/>
  </div>
</template>

<script>
import MovieTrailer from '@/components/recommendations/MovieTrailer.vue'
import RecomList from '@/components/recommendations/RecomList.vue'
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'recomView',
  components: {
    MovieTrailer, RecomList,
  },
  data() {
    return {
      movieId: parseInt(this.$route.params.movieId),
      currentMovie: false,
    }
  },
  computed: {
    ...mapGetters(['movies', ]),
    targetMovie() {
      const target = this.movies.filter(movie => movie.movie_id === this.movieId)[0]
      return target
    },
  },

  methods: {
    ...mapActions(['fetchMovies', 'getUserRecommendations', 'moveToRecom']),
    changeTrailer(currentMovie) {
      this.currentMovie = currentMovie
    }
  },
  created() {
    this.fetchMovies(this.movieId)
  },
}
</script>

<style scoped>
.trailer {
  position: absolute;
  margin-top: -67px;
  z-index: 0;
}

.list {
  position: relative;
  top: 100%;
  width: 100%;
  opacity: 30%;
  z-index: 1;
}

.list:hover {
  opacity: 80%;
}

h2{
  position: relative;
  top: 100%;
  left: 38%;
  width: 25%;
  font-size: 3vmin;
  text-align: center;
  color: #484848;
  font-size: 3vmin;
  font-weight: bold;
  font-family: monospace;
  letter-spacing: 7px;
  cursor: pointer;
}

h2 span{
  transition: .5s linear
}
h2:hover span:nth-child(1){
  margin-right: 5px
}
/* h2:hover span:nth-child(1):before{
  content: "Additional ";
} */

h2:hover span{
  color: #fff;
  font-size: 4vmin;
  text-shadow: 0 0 10px #fff,
               0 0 20px #fff, 
               0 0 40px #fff;
}
</style>
