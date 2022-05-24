<template>
  <div>
    <form @submit.prevent="onSubmit">
      <v-card class="mx-auto my-12" color="purple lighten-5" max-width="1200" min-height="800" elevation="14">
        <v-row>
          <v-col class="my-poster">
            <v-img v-if="newReview.movie_title" class="mx-auto" 
              height="741" width="500" :src="moviePoster">
            </v-img>
          </v-col>
          <v-divider vertical inset></v-divider>

          <v-col class="my-auto mx-2">
            <v-card-title class="d-flex justify-space-between">
              <!-- <h2 class="d-inline">{{ review.movie_title }}</h2> -->
              <div>
                <!-- input 길이 늘리기!!!! -->
                <v-autocomplete
                  chips deletable-chips filled rounded solo
                  v-model="newReview.movie_title"
                  :items="moviesTitle"
                ></v-autocomplete>
              </div>
              <br>
              <v-rating
                v-model="newReview.vote"
                background-color="grey"
                color="amber"
                hover
                large
              ></v-rating>
            </v-card-title>

          </v-col>
        </v-row>


      </v-card>

    </form>


    <form @submit.prevent="onSubmit">

        <!-- <label for="movie-title">movie title: </label> -->
        <!-- <input v-model="newReview.movie_title" type="text" id="movie-title" /> -->
      
        <!-- vote(별점) -->
      <div>
        <!-- <v-textarea
              outlined
              label="Outlined textarea"
            ></v-textarea> -->
        <label for="content">review: </label>
        <textarea v-model="newReview.content" type="text" id="content"></textarea>
      </div>
      <div>
        <button>{{ action }}</button>
      </div>
    </form>

  </div>
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
/* .my-poster {
  height:  800px;
} */

</style>
