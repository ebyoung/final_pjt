<template>
  <form @submit.prevent="onSubmit">
    <div>
      <v-autocomplete
        chips
        deletable-chips
        filled
        rounded
        solo
        v-model="newReview.movie_title"
        :items="moviesTitle"
      ></v-autocomplete>
      <!-- <label for="movie-title">movie title: </label> -->
      <!-- <input v-model="newReview.movie_title" type="text" id="movie-title" /> -->
    </div>
    
    <div>
      <!-- movie_poster -->
      <v-img v-if="newReview.movie_title" :src="moviePoster" max-width="300px"></v-img>
    </div>
      <!-- vote(별점) -->
      <v-rating
        v-model="newReview.vote"
        background-color="grey lighten-2"
        color="orange"
        hover
        large
      ></v-rating>
    <div>
      <!-- <v-textarea
            outlined
            label="Outlined textarea"
          ></v-textarea> -->
      <label for="content">content: </label>
      <textarea v-model="newReview.content" type="text" id="content"></textarea>
    </div>
    <div>
      <button>{{ action }}</button>
    </div>
  </form>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'


  export default {
    name: 'ReviewForm',
    props: {
      review: Object,
      action: String,
    },
    data() {
      return {
        newReview: {
          movie_title: this.review.movie_title,
          vote: this.review.vote,
          content: this.review.content,
        }
      }
    },

    computed: {
      ...mapGetters(['movies', 'watchDay']),
      moviesTitle() {
        return this.movies.map(movie => movie.title)
      },
      moviePoster() {
        const posterPath = this.movies.filter(movie => this.newReview.movie_title === movie.title)[0].poster_path
        return 'https://image.tmdb.org/t/p/w500/' + posterPath
      },
    },

    methods: {
      ...mapActions(['createReview', 'updateReview', 'fetchMovies']),
      onSubmit() {
        if (this.action === 'create') {
          this.createReview({
            ...this.newReview,
            movie_poster: this.moviePoster,
            watch_day: this.watchDay
            })
        } else if (this.action === 'update') {
          const payload = {
            reviewPk: this.review.id,
            ...this.newReview,
            movie_poster: this.moviePoster,
            watch_day: this.review.watch_day,
          }
          this.updateReview(payload)
        }
      },
    },

    created() {
      this.fetchMovies()
    }
  }
</script>

<style>


</style>
