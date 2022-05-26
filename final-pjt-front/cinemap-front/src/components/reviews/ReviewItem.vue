<template>
  <v-hover v-slot="{ hover }">
    <v-card width="300px" :elevation="hover ? 16 : 2" shaped color="deep-purple lighten-4">
      <v-row class="ms-4">
        <v-chip class="mt-4 mb-1" @click="moveToProfile(review.user.username)" color="purple lighten-5" text-color="purple">
          <v-avatar color="purple" size="60">
          <img :src="HOST + review.user.profile_image" alt=""></v-avatar>
          <span class="ms-2 font-weight-bold text-button">
            {{ review.user.username }}</span>
        </v-chip>
      </v-row>
      <br>
      
      <!-- 글 이동 링크 (영화 포스터)) -->
      <router-link 
        :to="{ name: 'review', params: {reviewPk: review.pk} }">
        <v-img class="mx-auto rounded" width="90%" height="400px" :src="review.movie_poster" alt="포스터"
        gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"></v-img>
      </router-link>


      <!-- 댓글 개수/좋아요 개수 -->
      <v-card-actions class="mt-2 mb-5 me-5">
        <v-spacer></v-spacer>
        <v-badge class="me-2" color="deep-purple npm" :content="likeCounts" :value="likeCounts" overlap>
          <font-awesome-icon icon="fa-solid fa-heart" color="red" size="xl"/>
        </v-badge>
        <v-badge class="ms-2" color="#D500F9" :content="commentCounts" :value="commentCounts" overlap>
          <font-awesome-icon icon="fa-solid fa-comment-dots" color="#B388FF" size="xl"/>
        </v-badge>
        <br>
        <br>
      </v-card-actions>
    </v-card>
  </v-hover>

</template>

<script>
import router from '@/router'

export default {
  name: 'ReviewItem',
  props: {
    review: Object,
  },
  data: () => ({
      HOST: 'http://localhost:8000',
      
  }),
  computed: {

    likeCounts() {
        return this.review.review_likes_count
      },
    commentCounts() {
      return this.review.review_comments_count
    }
  },

  methods: {

    moveToProfile(username) {
      router.push({ name:'profile', params: { username: username }})
    },
  }

}
</script>

<style>

</style>