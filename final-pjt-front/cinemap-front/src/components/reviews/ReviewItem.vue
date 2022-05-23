<template>
  <v-hover v-slot="{ hover }">
    <v-card width='200px' :elevation="hover ? 16 : 2">
      <router-link 
        :to="{ name: 'profile', params: { username: review.user.username } }">
        <!-- 작성자 프로필 사진 추가!!!! -->
          <v-avatar
            color="indigo"
            size="36"
          >
            <img :src="HOST + review.user.profile_image" alt="">
          </v-avatar>
        {{ review.user.username }}
      </router-link>
      
      <!-- 글 이동 링크 (영화 포스터)) -->
      <router-link 
        :to="{ name: 'review', params: {reviewPk: review.pk} }">
        <v-img width="100%" :src="review.movie_poster" alt="포스터"></v-img>
      </router-link>

      <!-- 댓글 개수/좋아요 개수 -->
      <p>댓글: {{ review.review_comments_count }}</p>
      <p>좋아요: {{ review.review_likes_count }}</p>
    </v-card>
  </v-hover>
</template>

<script>
export default {
  name: 'ReviewItem',
  props: {
    review: Object,
  },
  data: () => ({
      HOST: 'http://localhost:8000',
  }),

}
</script>

<style>

</style>