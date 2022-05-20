<template>
  <div>
    <!-- user profile_image, username -->
    <!-- {{ review.movie_poster }} -->
    <h1>{{ review.movie_title }}</h1>

    <!-- 평점(vote) -> {{ review.vote }} -->
    <p>
      {{ review.content }}
    </p>
    <!-- review 좋아요 UI -->
    <div>
      좋아요
      <button
        @click="likeReview(reviewPk)"
      >{{ likeCount }}</button>
    </div>
    
    <!-- review Edit/Delete UI -->
    <div v-if="isAuthor">
      <router-link :to="{ name: 'reviewEdit', params: { reviewPk } }">
        <button>Edit</button>
      </router-link>
      |
      <button @click="deleteReview(reviewPk)">Delete</button>
    </div>

    <!-- <hr> -->
    <hr />
    <!-- Comment UI -->
    <comment-list :comments="review.comments"></comment-list>

  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import CommentList from '@/components/reviews/CommentList.vue'



  export default {
    name: 'reviewDetail',
    components: { CommentList },
    data() {
      return {
        reviewPk: this.$route.params.reviewPk,
      }
    },
    computed: {
      ...mapGetters(['isAuthor', 'review']),
      likeCount() {
        return this.review.like_users?.length
      }
    },
    methods: {
      ...mapActions([
        'fetchreview',
        'likeReview',
        'deleteReview',
      ])
    },
    created() {
      this.fetchReview(this.reviewPk)
    },
  }
</script>

<style></style>
