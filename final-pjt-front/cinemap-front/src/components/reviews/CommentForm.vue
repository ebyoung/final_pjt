<template>
  <form @submit.prevent="onSubmit" class="comment-form">
    <label for="comment">comment: </label>
    <input type="text" id="comment" v-model="content" required>
    <v-btn
      elevation="2"
    >게시</v-btn>
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
    ...mapGetters(['review']),
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
.comment-form {
  border: 1px solid black;
  margin: 1rem;
  padding: 1rem;
}
</style>