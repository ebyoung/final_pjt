<template>
  <div class="container">
    <v-row justify="center">
      <figure class="snip1376">
        <img :src="profile.profile_image" alt="profileImage" />
        <figcaption>
          <h2>{{ profile.username }}</h2>
          <pre>{{ profile.introduction }}</pre>
          <div class="icons">
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
          </div>
        </figcaption>
      </figure>




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
  updated() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
  },
}
</script>

<style>
@import url(https://fonts.googleapis.com/css?family=Oswald);
@import url(https://code.ionicframework.com/ionicons/2.0.1/css/ionicons.min.css);
@import url(https://fonts.googleapis.com/css?family=Quattrocento);
.snip1376 {
  font-family: 'Quattrocento', Arial, sans-serif;
  position: relative;
  overflow: hidden;
  margin: 10px;
  min-width: 230px;
  max-width: 315px;
  width: 100%;
  color: #141414;
  text-align: left;
  line-height: 1.4em;
  font-size: 16px;
}
.snip1376 * {
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
}
.snip1376 img {
  max-width: 100%;
  vertical-align: top;
}
.snip1376 figcaption {
  width: 100%;
  background-color: #ffffff;
  padding: 15px 25px 65px;
  position: relative;
}
.snip1376 figcaption:before {
  position: absolute;
  content: '';
  z-index: 2;
  bottom: 100%;
  left: 0;
  width: 100%;
  height: 80px;
  background-image: -webkit-linear-gradient(top, transparent 0%, #ffffff 100%);
  background-image: linear-gradient(to bottom, transparent 0%, #ffffff 100%);
}
.snip1376 h2,
.snip1376 pre {
  margin: 0 0 10px;
}
.snip1376 h2 {
  font-weight: 300;
  font-size: 1.5em;
  line-height: 1.2em;
  font-family: 'Oswald', Arial, sans-serif;
  text-transform: uppercase;
}
.snip1376 pre {
  font-size: 0.9em;
  letter-spacing: 1px;
  opacity: 0.9;
}
.snip1376 .icons {
  position: absolute;
  bottom: 0;
  left: 0;
  background-color: #e6e6e6;
  width: 100%;
  text-align: center;
}
.snip1376 i {
  padding: 10px 5px;
  display: inline-block;
  font-size: 24px;
  color: #141414;
  opacity: 0.65;
}
.snip1376 i:hover {
  opacity: 1;
  -webkit-transition: all 0.35s ease;
  transition: all 0.35s ease;
}
</style>