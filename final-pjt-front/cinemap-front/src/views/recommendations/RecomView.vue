<template>
  <div>
    <MovieTrailer :videoKey='currentVideoKey? currentVideoKey : targetMovie.video_key' class="trailer"/>
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
      currentVideoKey: false,
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
    ...mapActions(['fetchMovies', 'getUserRecommendations']),
    changeTrailer(videoKey) {
      this.currentVideoKey = videoKey
    }
  },
  created() {
    this.fetchMovies(this.movieId)
  },  
}
</script>

<style>
.trailer {
  /* position: absolute; */
}

.list {
  margin-left: 50px;
  margin-top: 100px;
  width: 10 0%;
  opacity: 30%;
}
</style>