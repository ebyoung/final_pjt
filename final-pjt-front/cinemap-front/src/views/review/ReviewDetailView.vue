<template>
  <div>
        <br>
    <div class="d-flex justify-center">
      <v-chip x-large color="purple lighten-4" class="my-review 
        mt-5 my-5 px-5 text-center purple--text">😃 Review </v-chip>
    </div>
    <!-- v-menu 쓸 수 있음! -->
    <br>
    <v-card class="mx-auto my-10" color="#f3e5f569" max-width="1100" elevation="14" shaped>
      <v-row class="ms-1">
        <v-chip class="ms-2 my-3" @click="moveToProfile(getUsername)" color="purple lighten-5" text-color="purple">
          <v-avatar color="purple" size="60">
          <img :src="getProfileImage" alt=""></v-avatar>
          <span class="ms-2 font-weight-bold text-button">
            {{ getUsername }}</span>
        </v-chip>
      </v-row>
      <v-divider class="mt-2 mb-3"></v-divider>
      <v-row>
        <v-col>
          <v-img class="mx-auto rounded"
            height="593" width="400"
            :src="review.movie_poster" 
          ></v-img>
        </v-col>
        <v-divider vertical inset></v-divider>

        <v-col class="my-auto mx-2">
          <v-card-title class="d-flex justify-space-between py-2">
            <span> 
              <h2 class="d-inline">{{ review.movie_title }}</h2>
              <span class="mx-2">
                
                <v-badge color="#F48FB1" :content="likeCounts" :value="likeCounts" overlap>
                  <button @click="likeReview(reviewPk)" >
                    <font-awesome-icon v-if="isLike" icon="fa-solid fa-heart" color="#F50057" size="xl"/>
                    <font-awesome-icon v-else icon="fa-solid fa-heart" color="grey" size="xl"/>
                  </button>
                </v-badge>
                
                <!-- <span class="ms-1">+{{ review.review_likes_count }}</span> -->
              </span>
            </span>
            <span v-if="isAuthor">
              <router-link :to="{ name: 'reviewEdit', params: { reviewPk } }">
                <v-btn icon color="deep-purple">
                  <font-awesome-icon icon="fa-solid fa-pen-to-square" size="lg"/>      
                </v-btn>
              </router-link>
            </span>
          </v-card-title>
          
          <v-card-text>
            <v-row
              align="center"
              class="mx-0 mt-1"
            >
              <v-rating
                :value="getVote"
                background-color="grey lighten-2"
                color="amber"
                readonly
                size="30"
              ></v-rating>
            </v-row>

          
            <br>
            <br>
            <div class="">
              <v-sheet color="deep-purple lighten-4"
                class = "py-3 px-4"
                shaped
                elevation="1"
                min-height="250"
                width="530">
                <p>{{ review.content }}</p>
              </v-sheet>
            </div>
            <br>
            <!-- review Edit/Delete UI -->
            <div v-if="isAuthor" class="d-flex justify-end my-2" >
              <v-btn icon @click="deleteReview(reviewPk)" small color="deep-purple">
                <font-awesome-icon icon="fa-regular fa-trash-can" size="lg"/>
              </v-btn>
            </div>
          </v-card-text>

          <v-divider class="mx-4"></v-divider>

          <v-card-title>
            <font-awesome-icon icon="fa-solid fa-comment-dots"/>
            <span class="ms-2">Comments</span>
            </v-card-title>

          <v-card-text>
            <comment-list :comments="review.comment_set"></comment-list>
          </v-card-text>
        </v-col>
      </v-row>
    </v-card>
  </div>
  
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import router from '@/router'
  import CommentList from '@/components/reviews/CommentList.vue'
  import drf from '@/api/drf'



  export default {
    name: 'reviewDetail',
    components: { CommentList },
    data() {
      return {
        reviewPk: this.$route.params.reviewPk,
        
      }
    },
    computed: {
      ...mapGetters(['isAuthor', 'isLike', 'review',]),
      getVote() {
      return this.review.vote
      },
      likeCounts() {
        return this.review.review_likes_count
      },
      getUsername() {
        return this.review.user?.username
      },
      getProfileImage() {
        return drf.accounts.profileImage(this.review.user?.profile_image)
      }
    },

    methods: {
      ...mapActions([
        'fetchReview',
        'likeReview',
        'deleteReview',
        // 'fetchProfile',
      ]),

      moveToProfile(username) {
        router.push({ name:'profile', params: { username } })
      },
    },
    created() {
      
      this.fetchReview(this.reviewPk)
      // this.fetchProfile(this.getUsername)
    },
  }
</script>

<style scoped>
.my-card {
  color: #f3e5f569

}
.my-review {
  /* font-family: 'Inconsolata', monospace; */
    font-family: 'Source Code Pro', monospace;
    font-weight: bolder;
    font-size: 40px;
}

</style>
