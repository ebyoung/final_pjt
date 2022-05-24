<template>
  <div>
    <br>
    <div class="d-flex justify-center">
      <v-chip x-large color="purple lighten-4" class="my-new text-h4 font-weight-bold mt-5 my-5 px-5 text-center purple--text">😃 New Review </v-chip>
    </div>
    <review-form :review="review" action="create"></review-form>
  </div>
</template>

<script>
  import ReviewForm from '@/components/reviews/ReviewForm.vue'
  export default {
    name: 'ReviewNewView',
    components: { ReviewForm },
    data() {
      return {
        review: {
          pk: null,
          // 영화 이름을 넣어 줄건지?
          movie_title: '',
          // movie_poster: '',
          vote: 0,
          content: '',
          // watchDay: this.$route.params,
        }
      }
    },
  }
</script>

<style>
/* .my-new {
  margin-left: 23rem;
} */

</style>
