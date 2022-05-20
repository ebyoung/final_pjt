<template>
  <li class="comment-list-item">
    <!-- {{ comment.user.profile_image }} -->
    <router-link :to="{ name: 'profile', params: { username: comment.user.username } }">
      {{ comment.user.username }}
    </router-link>: 
    <span>{{ comment.content }}</span>
    <span v-if="currentUser.username === comment.user.username">
      <button @click="deleteComment(payload)">Delete</button>
    </span>

  </li>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListItem',
  props: { comment: Object },
  data() {
    return {
      payload: {
        reviewPk: this.comment.review,
        commentPk: this.comment.id,
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  methods: {
    ...mapActions(['deleteComment']),
  },
}
</script>

<style>
.comment-list-item {
  border: 1px solid green;

}
</style>