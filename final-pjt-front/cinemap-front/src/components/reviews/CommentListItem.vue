<template>
  <div class="px-0 mb-3 d-flex" dense>
    <v-btn text rounded @click="moveToProfile(comment.user.username)" class="py-3" small color="blacknp"
      outlined>
      <v-list-item-avatar color="grey" size="27" class="ms-0 me-1">
        <img :src="commentUserProfileImage" alt=""></v-list-item-avatar>
      <span class="font-weight-bold">{{ comment.user.username  }}</span>
    </v-btn>
    <v-list-item-content class="mx-5 py-0 black--text">
      {{ comment.content }}
    </v-list-item-content>
    <span v-if="currentUser.username === comment.user.username" class="ms-5">
      <v-btn icon color="grey" @click="deleteComment(payload)">
        <font-awesome-icon small icon="fa-regular fa-trash-can"/>
      </v-btn>
    </span>

    <br>
  </div>

  
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import router from '@/router'
import drf from '@/api/drf'

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
    ...mapGetters(['currentUser',]),
    commentUserProfileImage() {
      return drf.accounts.profileImage(this.comment.user?.profile_image)
    },
  },

  methods: {
    ...mapActions(['deleteComment']),
    moveToProfile(username) {
      router.push({ name:'profile', params: { username } })
    },
  },
}
</script>

<style>

</style>