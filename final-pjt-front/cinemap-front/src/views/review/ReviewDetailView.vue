<template>
  <v-card class="mx-auto my-12" max-width="1200">
    <v-row>
      <!-- user profile_image, username -->
      <!-- {{ review.movie_poster }} -->
      <v-col>
        <v-img
          height="800" width="400"
          :src="review.movie_poster"
        ></v-img>
      </v-col>

      <v-col class="my-auto">
        <v-card-title>
          <span>{{ review.movie_title }}</span>
          <span>
            <v-btn
              @click="likeReview(reviewPk)"
              class="mx-2" fab dark small color="pink">
              <v-icon dark>
                mdi-heart
              </v-icon>
            </v-btn>
            <span>{{ review.review_likes_count }}</span>
          </span>
        </v-card-title>

        <v-card-text>
          <v-row
            align="center"
            class="mx-0"
          >
            <v-rating
              :value="getVote"
              background-color="grey lighten-2"
              color="amber"
              readonly
              size="20"
            ></v-rating>
          </v-row>

          <!-- <div class="my-4 text-subtitle-1">
            $ • Italian, Cafe
          </div> -->
          <br>          
          <div>
            {{ review.content }}
          </div>
          <br>
          <!-- review Edit/Delete UI -->
          <div v-if="isAuthor">
            <router-link :to="{ name: 'reviewEdit', params: { reviewPk } }">
              <button>Edit</button>
            </router-link>
            |
            <button @click="deleteReview(reviewPk)">Delete</button>
          </div>
        </v-card-text>

        <v-divider class="mx-4"></v-divider>

        <v-card-title>Comments</v-card-title>

        <v-card-text>
          <comment-list :comments="review.comment_set"></comment-list>
        </v-card-text>
      </v-col>


    </v-row>
    

    


    <!-- <h1>{{ review.movie_title }}</h1>
    <span>
      <v-rating
        :value="getVote"
        background-color="grey lighten-2"
        color="orange"
        readonly
        size="30"
      ></v-rating>
    </span> -->

    <!-- <p>
      {{ review.content }}
    </p> -->

    <!-- <div>
      <v-btn
        @click="likeReview(reviewPk)"
        class="mx-2" fab dark small color="pink">
        <v-icon dark>
          mdi-heart
        </v-icon>
      </v-btn>
      {{ review.review_likes_count }}
    </div> -->
    
    
    <!-- <div v-if="isAuthor">
      <router-link :to="{ name: 'reviewEdit', params: { reviewPk } }">
        <button>Edit</button>
      </router-link>
      |
      <button @click="deleteReview(reviewPk)">Delete</button>
    </div> -->


  </v-card>
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
