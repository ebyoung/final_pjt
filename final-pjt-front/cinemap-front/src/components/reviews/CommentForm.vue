<template>
  <form @submit.prevent="onSubmit" class="comment-form">
    <div class="d-flex">
      <span class="d-flex me-2">
        <span>
          <v-avatar color="grey" size="47">
            <img :src="profileImage" alt=""></v-avatar>
        </span>
      </span>
      <v-text-field placeholder="댓글을 입력하세요!"
        v-model="content" required outlined filled clearable dense rounded></v-text-field>
      <v-btn @click="onSubmit"
        elevation="2" small class="ms-2" depressed
      >게시</v-btn>
    </div>
    
    <!-- <button>게시</button> -->
  </form>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'



export default {
  name: 'CommentForm',
  data() {
    return {
      content: ''
    }
  },
  computed: {
    ...mapGetters(['review', 'currentUser', 'getProfileImage',]),
    profileImage() {
      this.setProfileImagePath(this.currentUser.username)
      return this.getProfileImage
    },
  },

  methods: {
    ...mapActions(['createComment', 'setProfileImagePath',]),
    onSubmit() {
      this.createComment({ reviewPk: this.review.id, content: this.content, })
      this.content = ''
    }
  },
}
</script>

<style>
/* .comment-form {
  border: 1px solid black;
  /* margin: 1rem; */
  /* padding: 0.5rem; */
/* } */
</style>