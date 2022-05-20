<template>
  <div class="container row">
    <div class="info col-3">
      <img :src="profile.profile_image" alt="프로필사진">
      <h1>{{ profile.username }}</h1>
      <p>팔로워 수: {{ profile.follower_count }}</p>
      <p>팔로잉 수: {{ profile.following_count }}</p>
      <v-btn
        @click="follow(profile.username)"
        v-if="!isCurrentUserProfile"
        color="primary"
        >{{ isFollow ? '언팔로우' : '팔로우' }}</v-btn>
      <v-btn
        @click="dialog = true"
        v-else
        color="primary"
      >프로필 수정
      </v-btn>
      <ProfileForm
        v-if="dialog"
        @close-dialog="dialog=false"/>
      <pre>{{ profile.introductoin }}</pre>
    </div>
    <div class="calendar col-9">
      <MovieCalendar/>
    </div>

  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import MovieCalendar from '@/components/accounts/MovieCalendar'
import ProfileForm from '@/components/accounts/ProfileForm'


export default {
  name: 'ProfileView',
  components: {
    MovieCalendar, ProfileForm,
  },
  data: () => ({
      dialog: false,
    }),
  computed: {
    ...mapGetters(['profile', 'isFollow', 'currentUser']),
    isCurrentUserProfile() {
      return this.currentUser.username === this.profile.username
    },
  },
  methods: {
    ...mapActions(['fetchProfile', 'fetchCurrentUser', 'follow'])
  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
  },
}
</script>

<style>

</style>