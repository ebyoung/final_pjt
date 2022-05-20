<template>
  <div>
    <!-- user profile_image, username -->
    <!-- {{ review.movie_poster }} -->
    <h1>{{ review.movie_title }}</h1>
    <span>
      <v-rating
        :value="getVote"
        background-color="grey lighten-2"
        color="orange"
        readonly
        large
      ></v-rating>
    </span>

    <!-- 평점(vote) -> {{ review.vote }} -->
    <p>
      {{ review.content }}
    </p>
    <!-- review 좋아요 UI -->
    <div>
      <v-btn
        @click="likeReview(reviewPk)"
        class="mx-2" fab dark small color="pink">
        <v-icon dark>
          mdi-heart
        </v-icon>
      </v-btn>
      {{ review.review_likes_count }}
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
    <comment-list :comments="review.comment_set"></comment-list>

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
      getVote() {
      return this.review.vote
      },
    },

    methods: {
      ...mapActions([
        'fetchReview',
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
