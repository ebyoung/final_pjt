<template>
  <div>
    <v-card class="mx-auto my-12" color="purple lighten-5" max-width="1100" min-height="600" elevation="14" shaped>
      <v-row>
        <v-col v-if="newReview.movie_title" class="my-poster">
          <v-img  class="my-img mx-auto rounded"
            height="593" width="400" :src="moviePoster">
          </v-img>
        </v-col>
        <v-col v-else class="d-flex align-center justify-center">
          <div><span class="purple--text text-button">
            영화를 선택하시면 포스터가 짠!🤩</span></div>
        </v-col>

        <v-divider vertical inset></v-divider>

        <v-col>
          <v-row class="mt-3">
            <v-card-title class="pb-0 mx-5">
              <!-- <h2 class="d-inline">{{ review.movie_title }}</h2> -->  
              <v-autocomplete placeholder="영화를 검색해주세요!" label="영화를 검색해주세요!"
                  chips deletable-chips rounded solo full-width outlined filled color="purple" 
                  v-model="newReview.movie_title" background-color="purple lighten-5" menu-props="rounded"
                  :items="moviesTitle" 
                ></v-autocomplete>

            </v-card-title>
            <v-card-text class="mx-3">
              <v-rating class="mx-4"
                v-model="newReview.vote"
                background-color="grey"
                color="amber"
                hover
                medium
              ></v-rating>

              <v-container fluid class="mt-5">
                <v-textarea
                  clearable filled shaped
                  height="420" color="purple"
                  clear-icon="mdi-close-circle"
                  placeholder="영화 리뷰를 작성해주세요😎"
                  v-model="newReview.content" background-color="deep-purple lighten-4"
                ></v-textarea>
              </v-container>
              <div class="d-flex justify-end">
                <v-btn @click="onSubmit" text color="purple" >{{ action }}</v-btn>
              </div>
            </v-card-text>
          </v-row>
        </v-col>
      </v-row>
    </v-card>
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

<style scoped>
#list-19 {
  background-color: rgba(241, 211, 241, 0.935) !important;
}

.my-img {
  margin-top: 30px;
}


</style>