<template>
  <form @submit.prevent="onSubmit">
    <div>
      <label for="movie-title">movie title: </label>
      <input v-model="newReview.movie_title" type="text" id="movie-title" />
    </div>
    
    <div>
      <!-- movie_poster -->

    </div>
      <!-- vote(별점) -->
      <v-rating
        v-model="newReview.vote"
        background-color="grey lighten-2"
        color="orange"
        hover
        large
      ></v-rating>
      <!-- <v-rating
        v-model="vote"
        background-color="grey lighten-2"
        color="warning"
        empty-icon="$mdiStarOutline"
        full-icon="$mdiStar"
        half-icon="$mdiStarHalfFull"
        hover
        length="5"
        size="30"
      ></v-rating> -->
    <div>
      <label for="content">content: </label>
      <textarea v-model="newReview.content" type="text" id="content"></textarea>
    </div>
    <div>
      <button>{{ action }}</button>
    </div>
  </form>
</template>

<script>
import { mapActions } from 'vuex'

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
          // movie_poster: this.review.movie_poster,
          vote: this.review.vote,
          content: this.review.content,
        }
      }
    },

    methods: {
      ...mapActions(['createReview', 'updateReview']),
      onSubmit() {
        if (this.action === 'create') {
          this.createReview(this.newReview)
        } else if (this.action === 'update') {
          const payload = {
            reviewPk: this.review.id,
            ...this.newReview,
          }
          this.updateReview(payload)
        }
      },
    },
  }
</script>

<style>


</style>
