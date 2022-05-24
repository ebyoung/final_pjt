<template>
  <div>
    <h1>둘러보기</h1>

    <v-btn :disabled='sortedByLikes' @click="getSortedByLikes">좋아요순</v-btn>
    <v-btn :disabled='sortedByComments' @click="getSortedByComments">댓글순</v-btn>
    <v-btn :disabled='sortedByDate' @click="getSortedByDate">최신순</v-btn>

    <v-row>
      <v-col v-for="review in reviews" :key="review.pk"
      cols="2">
        <!-- 작성자 -> 프로필 이동 링크 -->
        <!-- ReviewItem.vue로 넘겨줘서 카드 형태로 만들지...? -->
    <!-- https://vuetifyjs.com/en/components/images/#grid -->
        <ReviewItem :review="review"/>
      </v-col>
    </v-row>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import ReviewItem from '@/components/reviews/ReviewItem'

  export default {
    name: 'ReviewList',
    data: () => ({
      sortedByLikes: true,
      sortedByComments: false,
      sortedByDate: false,
    }),
    components: {
      ReviewItem,
    },

    computed: {
      ...mapGetters(['reviews', ]),
    },
    methods: {
      ...mapActions(['fetchReviews', 'sortReviewsByLikes', 'sortReviewsByComments', 'sortReviewsByDate', ]),
      getSortedByLikes() {
        this.sortReviewsByLikes()
        this.sortedByLikes = true
        this.sortedByComments= false
        this.sortedByDate= false
      },
      getSortedByComments() {
        this.sortReviewsByComments()
        this.sortedByLikes = false
        this.sortedByComments= true
        this.sortedByDate= false
      },
      getSortedByDate() {
        this.sortReviewsByDate()
        this.sortedByLikes = false
        this.sortedByComments= false
        this.sortedByDate= true
      },
    },
    created() {
      this.fetchReviews()
    },
  }
</script>

<style>
</style>
