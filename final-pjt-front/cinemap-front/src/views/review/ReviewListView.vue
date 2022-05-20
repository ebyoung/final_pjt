<template>
  <div>
    <h1>둘러보기</h1>
    
    <!-- 인기 순대로 정렬 해야함!! -> store의 getters에서 -->


    <ul>
      <li v-for="review in reviews" :key="review.pk">
        <!-- 작성자 -> 프로필 이동 링크 -->
        <!-- ReviewItem.vue로 넘겨줘서 카드 형태로 만들지...? -->
        <router-link 
          :to="{ name: 'profile', params: { username: review.user.username } }">
          <!-- 작성자 프로필 사진 추가!!!! -->
          <!-- <img src= "review.user.profile_image" alt=""> -->
          {{ review.user.username }} : 
        </router-link>
        
        <!-- 글 이동 링크 (영화 포스터)) -->
        <router-link 
          :to="{ name: 'review', params: {reviewPk: review.pk} }">
          {{ review.movie_poster }}
        </router-link>

        <!-- 댓글 개수/좋아요 개수 -->
        =>
        ({{ review.comment_count }}) | +{{ review.like_count }}

      </li>
    </ul>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'ReviewList',
    computed: {
      ...mapGetters(['reviews'])
    },
    methods: {
      ...mapActions(['fetchReviews'])
    },
    created() {
      this.fetchReviews()
    },
  }
</script>

<style></style>
