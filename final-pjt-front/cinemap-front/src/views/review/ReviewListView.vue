<template>
  <div>
    <br>
    <div class="d-flex justify-center">
      <v-chip x-large color="purple lighten-4" class="my-edit
        mt-5 my-5 px-5 text-center purple--text">😃 Reviews </v-chip>
    </div>
    <!-- v-menu 쓸 수 있음! -->
    <br>
  
    <v-card class="my-card mx-auto mb-4 pt-4" width="1300" elevation="15" shaped >
      <div class="d-flex justify-end me-5">
        <v-btn-toggle rounded color="deep-purple accent-3" group class="me-5">
          <v-btn text v-if='sortedByLikes' color="purple" @click="getSortedByLikes">좋아요 수</v-btn>
          <v-btn text v-else :disabled='sortedByLikes' @click="getSortedByLikes">좋아요 수</v-btn>
          <v-btn text v-if='sortedByComments' color="purple" @click="getSortedByComments">댓글 수</v-btn>
          <v-btn text v-else :disabled='sortedByComments' @click="getSortedByComments">댓글 수</v-btn>
          <v-btn text v-if='sortedByDate' color="purple" @click="getSortedByDate">new </v-btn>
          <v-btn text v-else :disabled='sortedByDate' @click="getSortedByDate">new </v-btn>
        </v-btn-toggle>
      </div>
      <v-divider inset></v-divider>
      <br>
      <v-container fluid>
        <v-row dense class="ms-5">
          <v-col cols="3" v-for="review in reviews" :key="review.pk"
          >
            <ReviewItem :review="review"/>
            <br>
          </v-col>
            
        </v-row>
      </v-container>
    </v-card>


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

<style scoped>

.my-card {
  background-color: #f3e5f5af
}

.my-edit {
  /* font-family: 'Inconsolata', monospace; */
    font-family: 'Source Code Pro', monospace;
    font-weight: bolder;
    font-size: 40px;
}
</style>
