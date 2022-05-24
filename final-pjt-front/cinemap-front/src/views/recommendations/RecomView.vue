<template>
  <div>
    <MovieTrailer :videoKey='currentMovie? currentMovie.video_key : targetMovie.video_key' class="trailer"/>
    <h1 class="jt --debug">
      <span class="jt__row">
        <span class="jt__text">{{ currentMovie? currentMovie.title : targetMovie.title }}</span>
      </span>
      <span class="jt__row jt__row--sibling" aria-hidden="true">
        <span class="jt__text">{{ currentMovie? currentMovie.title : targetMovie.title }}</span>
      </span>
      <span class="jt__row jt__row--sibling" aria-hidden="true">
        <span class="jt__text">{{ currentMovie? currentMovie.title : targetMovie.title }}</span>
      </span>
      <span class="jt__row jt__row--sibling" aria-hidden="true">
        <span class="jt__text">{{ currentMovie? currentMovie.title : targetMovie.title }}</span>
      </span>
    </h1>
    <RecomList :movie='targetMovie' @changeTrailer='changeTrailer' class="list"/>
    <h2>Recommendations</h2>
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
    ...mapActions(['fetchMovies', 'getUserRecommendations']),
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
  margin-top: -130px;
  z-index: 0;
}

.list {
  position: relative;
  top: 65%;
  width: 100%;
  opacity: 30%;
  z-index: 1;
}

.list:hover {
  opacity: 80%;
}

h2 {
  position: relative;
  top: 60%;
  font-size: 3vmin;
  text-align: center;
  color: grey;
}

@import url('https://fonts.googleapis.com/css2?family=Staatliches&display=swap');

.jt {
  position: relative;
  /* left: 5%;
  top: 10%; */
  text-align: center;
  top: 60%;
  font-size: 10vmin;
  font-family: 'Staatliches', sans-serif;
  text-transform: uppercase;
  font-display: swap;
  text-shadow: 0 0 10px tomato;
  white-space: nowrap;
}

.jt__row {
  display: block;
}
.jt__row:nth-child(1) {
  clip-path: polygon(-10% 75%, 110% 75%, 110% 110%, -10% 110%);
}
.jt__row:nth-child(2) {
  clip-path: polygon(-10% 50%, 110% 50%, 110% 75.3%, -10% 75.3%);
}
.jt__row:nth-child(3) {
  clip-path: polygon(-10% 25%, 110% 25%, 110% 50.3%, -10% 50.3%);
}
.jt__row:nth-child(4) {
  clip-path: polygon(-10% 0%, 110% 0%, 110% 25.3%, -10% 25.3%);
}

.jt__row.jt__row--sibling {
  position: absolute;
  top: 0;
  left: 0;
  user-select: none;
  width: 100%;
}

.jt__text {
  display: block;
  transform-origin: bottom left;
  animation: moveIn 3s 0s cubic-bezier(.36, 0, .06, 1) alternate infinite;
}

.jt__row:nth-child(1) .jt__text {
  transform: translateY(-1em);
}
.jt__row:nth-child(2) .jt__text {
  transform: translateY(-1.1em) scaleY(1.1);
}
.jt__row:nth-child(3) .jt__text {
  transform: translateY(-1.2em) scaleY(1.2) ;
}
.jt__row:nth-child(4) .jt__text {
  transform: translateY(-1.3em) scaleY(1.3) ;
}
.jt__row:nth-child(5) .jt__text {
  transform: translateY(-1.4em) scaleY(1.4) ;
}
.jt__row:nth-child(6) .jt__text {
  transform: translateY(-1.5em) scaleY(1.5) ;
}

@keyframes moveIn {
  50%, 100% { 
    transform: translateY(0em)
  }
  0%   { 
  opacity: 0; 
  filter: blur(10px);
  
  }
  100% { 
  opacity: 1; 
  filter: blur(0px);
  }
}



.debug .jt__row:nth-child(even) {
  color: black;
  background: white;
}
.debug .jt__row:nth-child(odd) {
  color: white;
  background: black;
}

* { box-sizing: border-box }

/* html, body {
  margin: 0;
  background: black;
  color: tomato;
  height: 100%;
} */

/* body {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
} */
</style>
