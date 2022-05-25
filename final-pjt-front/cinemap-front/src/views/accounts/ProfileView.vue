<template>
  <div class="container">
    <v-row justify="center">
      <div class="snip1376  me-5">
        <div class="text-center">
            <v-avatar color="white" size="250" class="mb-5">
              <v-img :src="profileImageUrl" alt="profileImage" />
            </v-avatar>
          <div>
            <div v-if="!isCurrentUserProfile">
              <h2>{{ profile.username }}</h2>
              <br>
              <v-btn v-if="isFollow" block rounded color="deep-purple accent-3" 
              @click="follow(profile.username)">
                <font-awesome-icon  icon="fa-solid fa-user-check" 
                size="lg" color="white"/>
                <span class="ms-3 white--text">언팔로우</span>
              </v-btn>
              <v-btn v-else block rounded color="grey" @click="follow(profile.username)">
                <font-awesome-icon icon="fa-solid fa-user-plus"
                size="lg" color="white"/>
                <span class="ms-3 white--text">팔로우</span>
              </v-btn>
            </div>
            <div v-else class="d-flex justify-center">
              <h2>{{ profile.username }}</h2>
              <div class="ms-2">
                <v-dialog v-model="dialog"
                  persistent max-width="550">
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn icon dark color="deep-purple accent-5" v-bind="attrs" v-on="on">
                      <v-icon>mdi-pencil</v-icon>
                      <!-- <span class="ms-2">프로필 수정</span> -->
                    </v-btn>
                  </template>
                  <ProfileForm v-if="dialog" :username="this.profile.username"
                    :introduction="this.profile.introduction"
                    @close-dialog="updateProfileImage"/>
                </v-dialog>
              </div>
            </div>

            <div class="d-flex ms-3 mt-3">
              <span class="me-1 mt-1"><font-awesome-icon icon="fa-bold fa-user-group" color="purple"
              /></span>
              <div>
                <v-dialog
                  v-model="dialog_follower"
                  scrollable
                  max-width="320"
                  >

                  <template v-slot:activator="{ on, attrs }">
                    <v-btn class="px-2"
                      text
                      v-bind="attrs"
                      v-on="on"
                    >
                    <v-card-title class="text-overline font-weight-bold px-1">팔로워</v-card-title>
                    <span class="">{{ profile.follower_count }}</span>
                    
                    </v-btn>
                  </template>
                  <v-card>
                    <v-card-title class="font-weight-bold">팔로워</v-card-title>
                    <v-card-text style="height: 300px;">
                      <div class="mt-2"
                      v-for="follower in this.profile.followers" :key="follower.username">
                        <!-- dialog 창 꺼지게 -->
                        <v-btn text rounded class="p-2" @click="moveProfile(follower.username)" >
                          <v-avatar color="white" size="32" class="me-2">
                          <img
                            :src="HOST + follower.profile_image"
                          ></v-avatar>
                          {{ follower.username }}
                        </v-btn>
                      </div>
                    </v-card-text>
                    <v-divider></v-divider>
                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn
                        color="black"
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
                  max-width="320"
                >
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn class="px-2"
                      text v-bind="attrs"
                      v-on="on"
                    >
                    <v-card-title class="text-overline font-weight-bold px-1">팔로잉</v-card-title>
                    <span>{{ profile.following_count }}</span>
                    </v-btn>
                  </template>
                  <v-card>
                    <v-card-title class="font-weight-bold">팔로잉</v-card-title>
                    <v-card-text style="height: 300px;">
                      <div class="mt-2"
                      v-for="following in this.profile.followings" :key="following.username">
                        
                        <!-- dialog 창 꺼지게 -->
                        <v-btn text rounded class="p-2" @click="moveProfile(following.username)" >
                          <v-avatar color="white" size="32" class="me-2">
                          <img
                            :src="HOST + following.profile_image"
                          ></v-avatar>
                          {{ following.username }}
                        </v-btn>
                      </div>
                    </v-card-text>
                    <v-divider></v-divider>
                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn
                        color="black"
                        text
                        @click="dialog_following = false"
                      >
                        Close
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>
              </div>
            </div>
          </div>
        </div>
        
        <v-card shaped class="mt-4" elevation="10" min-height="300" color="deep-purple lighten-5" width="300">
          <v-card-text class="black--text" >
          <!-- <v-sheet>{{ profile.introduction }}</v-sheet> -->
            {{ profile.introduction }}
          </v-card-text>
        </v-card>  
      </div>

      <MovieCalendar/>
    </v-row>
  </div>
</template>



<script>
import { mapGetters, mapActions } from 'vuex'
import MovieCalendar from '@/components/accounts/MovieCalendar'
import ProfileForm from '@/components/accounts/ProfileForm'
import router from '@/router'


export default {
  name: 'ProfileView',
  components: {
    MovieCalendar, ProfileForm,
  },
  data: () => ({
      dialog: false,
      dialog_follower: false,
      dialog_following: false,
      HOST: 'http://localhost:8000',
    }),
  computed: {
    ...mapGetters(['profile', 'isFollow', 'currentUser', 'profileImageUrl']),
    isCurrentUserProfile() {
      return this.currentUser.username === this.profile.username
    },
  },
  methods: {
    ...mapActions(['fetchProfile', 'fetchCurrentUser', 'follow']),
    updateProfileImage() {
      this.dialog = false
      // this.fetchProfile({ username: this.$route.params.username })
      this.$router.go()
    },
    moveProfile(username) {
      this.dialog_follower = false
      this.dialog_following = false
      this.fetchProfile({ username })
      router.push({ name:'profile', params: { username } })
    },
  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
  },
  // updated() {
  //   const payload = { username: this.$route.params.username }
  //   this.fetchProfile(payload)
  // },
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
  margin-top: 127px;
  width: 300px;
  color: #141414;
  text-align: left;
  line-height: 1.4em;
  font-size: 20px;
}
.snip1376 * {
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
}
.snip1376 img {
  width: 100%;
  height: 200px;
  vertical-align: top;
  object-fit: cover;
}
/* .snip1376 figcaption {
  width: 100%;
  height: 72px;
  background-color: #fcfcfc;
  padding: 15px 25px 65px;
  position: relative;
} */

/* .snip1376 figcaption:before {
  position: absolute;
  content: '';
  z-index: 2;
  bottom: 100%;
  left: 0;
  width: 100%;
  height: 80px;
  background-image: -webkit-linear-gradient(top, transparent 0%, #ffffff 100%);
  background-image: linear-gradient(to bottom, transparent 0%, #38ca25 100%);
} */

.snip1376 h2 {
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
  /* background-color: #e6e6e6; */
  width: 100%;
  text-align: center;
  border-radius: 20px;
}
.snip1376 i {
  padding: 10px 5px;
  display: inline-block;
  font-size: 24px;
  /* color: #141414; */
  opacity: 0.65;
}
.snip1376 i:hover {
  opacity: 1;
  -webkit-transition: all 0.35s ease;
  transition: all 0.35s ease;
}
</style>