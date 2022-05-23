<template>
  <!-- https://vuetifyjs.com/en/components/lists/#three-line -->
  <v-list-item class="ps-0">
    <!-- <v-list-item-avatar>
      <v-img :src="item.avatar"></v-img>
    </v-list-item-avatar> -->
    <router-link class="text-decoration-none" :to="{ name: 'profile', params: { username: comment.user.username } }">
      <!-- {{ comment.user.profile_image }} --> 
      {{ comment.user.username }} :
    </router-link>
    <v-list-item-content class="ms-1 py-0"><v-list-item-title v-text="comment.content"></v-list-item-title></v-list-item-content>
    <span v-if="currentUser.username === comment.user.username" class="ms-3">
      <button @click="deleteComment(payload)" elevation="2">
        <font-awesome-icon icon="fa-regular fa-trash-can"/>
      </button>
    </span>
    <br>
  </v-list-item>
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

</style>