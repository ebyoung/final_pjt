<template>
  <div>
    <h1>New Review</h1>
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

<style></style>
