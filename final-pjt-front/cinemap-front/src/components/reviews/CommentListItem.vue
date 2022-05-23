<template>
  <!-- https://vuetifyjs.com/en/components/lists/#three-line -->
  <v-list-item class="ps-0">
      <div class="">
        <button @click="moveToProfile(comment.user.username)">
          <v-list-item-avatar color="grey" size="30" class="ms-1 me-1">
            <img :src="commentUserProfileImage" alt=""></v-list-item-avatar>
          <span class="font-weight-bold">{{ comment.user.username  }}</span>
        </button></div>
    <!-- <v-list-item-avatar>
      :alt="`${chat.title} avatar`"
      <v-img :src="item.avatar"></v-img>
    </v-list-item-avatar> -->
    <v-list-item-content class="ms-5 py-0"><v-list-item-title v-text="comment.content"></v-list-item-title></v-list-item-content>
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