<template>
  <div>
    <br>
    <p class="text-overline font-weight-bold ms-3 mt-5 text-center">새로운 review😃</p>
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
