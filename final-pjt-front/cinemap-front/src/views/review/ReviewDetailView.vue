<template>
  <div>
    <v-card class="mx-auto my-12" max-width="1200">
      <div class="d-flex ms-2 my-3">
        <v-avatar color="grey" size="60">
        <img :src="getProfileImage" alt=""></v-avatar>
        <h1 class="ms-2"><button @click="moveToProfile(getUsername)">
            {{ getUsername }}
          </button></h1>
      </div>
      
          
        <!-- user profile_image, username -->
      <!-- 
      <br> --> 
      <v-row>
        <v-col>
          <v-img
            height="741" width="500"
            :src="review.movie_poster"
          ></v-img>
        </v-col>

        <v-col class="my-auto mx-2">
          <v-card-title class="d-flex justify-space-between">
            <span> 
              <h2 class="d-inline">{{ review.movie_title }}</h2>
              <span class="mx-2">
                
                <v-badge color="deep-purple npm" :content="likeCounts" :value="likeCounts" overlap>
                  <button @click="likeReview(reviewPk)" >
                    <font-awesome-icon v-if="isLike" icon="fa-solid fa-heart" color="red" size="xl"/>
                    <font-awesome-icon v-else icon="fa-solid fa-heart" color="grey" size="xl"/>
                  </button>
                </v-badge>
                
                <!-- <span class="ms-1">+{{ review.review_likes_count }}</span> -->
              </span>
            </span>
            <span v-if="isAuthor">
              <router-link :to="{ name: 'reviewEdit', params: { reviewPk } }">
                <button>
                  <font-awesome-icon icon="fa-solid fa-pen-to-square" />      
                </button>
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

            <!-- <div class="my-4 text-subtitle-1">
              $ • Italian, Cafe
            </div> -->
            <br>
            <br>
            <v-sheet color="grey lighten-4"
              class = "py-3 px-4"
              rounded
              elevation="1"
              min-height="300"
              width="500">
              {{ review.content }}
            </v-sheet>
            <br>
            <!-- review Edit/Delete UI -->
            <div v-if="isAuthor" class="d-flex justify-end my-2" >
              <button @click="deleteReview(reviewPk)" small>
                <font-awesome-icon icon="fa-regular fa-trash-can" size="lg"/>
              </button>
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

<style></style>
