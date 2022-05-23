<template>
  <form @submit.prevent="onSubmit" class="comment-form">
    <div class="d-flex">
      <span class="d-flex me-2">
        <!-- currentUser profile로! -->
        {{ currentUser.username }}:
      </span>
      <v-text-field placeholder="댓글을 입력하세요!" v-model="content" required outlined filled clearable dense></v-text-field>
      <v-btn @click="onSubmit"
        elevation="2" small class="ms-2" 
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
    ...mapGetters(['review', 'currentUser']),
  },
  methods: {
    ...mapActions(['createComment']),
    onSubmit() {
      this.createComment({ reviewPk: this.review.id, content: this.content, })
      this.content = ''
    }
  }
}
</script>

<style>
/* .comment-form {
  border: 1px solid black;
  /* margin: 1rem; */
  /* padding: 0.5rem; */
/* } */
</style>