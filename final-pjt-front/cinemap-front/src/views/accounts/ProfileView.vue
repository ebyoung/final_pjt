<template>
  <div class="container">
    <v-row justify="center">
      <v-card
      class="mx-auto"
      >
        <v-img
        class="white--text align-end"
        height="200px"
        :src="profile.profile_image"
        alt="프로필사진"
        >
        </v-img>
        <v-card-title>{{ profile.username }}</v-card-title>
          <v-dialog
            v-model="dialog_follower"
            scrollable
            max-width="30%"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                text
                v-bind="attrs"
                v-on="on"
              >팔로워: {{ profile.follower_count }}
              </v-btn>
            </template>
            <v-card>
              <v-card-title>팔로워 목록</v-card-title>
              <v-card-text style="height: 300px;">
                <div v-for="follower in this.profile.followers" :key="follower.username">
                  <v-avatar
                    color="primary"
                  >
                  <img
                    :src="follower.profile_image"
                  ></v-avatar>
                  <sapn class="mx-2">{{ follower.username }}</sapn>
                </div>
              </v-card-text>
              <v-divider></v-divider>
              <v-card-actions>
                <v-btn
                  color="blue darken-1"
                  text
                  @click="dialog_follower = false"
                >
                  Close
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
          <v-dialog
            v-model="dialog_following"
            scrollable
            max-width="30%"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                text
                v-bind="attrs"
                v-on="on"
              >팔로잉: {{ profile.following_count }}
              </v-btn>
            </template>
            <v-card>
              <v-card-title>팔로잉 목록</v-card-title>
              <v-card-text style="height: 300px;">
                <div v-for="following in this.profile.followings" :key="following.username">
                  <v-avatar
                    color="primary"
                  >
                  <img
                    :src="following.profile_image"
                  ></v-avatar>
                  <sapn class="mx-2">{{ following.username }}</sapn>
                </div>
              </v-card-text>
              <v-divider></v-divider>
              <v-card-actions>
                <v-btn
                  color="blue darken-1"
                  text
                  @click="dialog_following = false"
                >
                  Close
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        <v-card-text class="text--primary">
          <pre>{{ profile.introduction }}</pre>
        </v-card-text>
        <v-btn
          v-if="!isCurrentUserProfile"
          @click="follow(profile.username)"
          color="primary"
          text
          >{{ isFollow ? '언팔로우' : '팔로우' }}</v-btn>
        <v-dialog
          v-else
          v-model="dialog"
          persistent
          max-width="50%"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              color="primary"
              text
              v-bind="attrs"
              v-on="on"
            >프로필 수정
            </v-btn>
          </template>
          <ProfileForm
            v-if="dialog"
            :username="this.profile.username"
            :introduction="this.profile.introduction"
            @close-dialog="dialog=false"/>
        </v-dialog>
      </v-card>
      <MovieCalendar/>
    </v-row>
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
      dialog_follower: false,
      dialog_following: false,
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