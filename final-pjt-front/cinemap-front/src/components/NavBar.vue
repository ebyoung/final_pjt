<template>
  <nav class="my-navbar">
    <v-app-bar color="transparent" rounded>
        <v-app-bar-nav-icon><font-awesome-icon icon="fa-solid fa-clapperboard" color="purple" size="2x" /></v-app-bar-nav-icon>
        <!--  -->
  
        <v-toolbar-title>
          <span class="text-lg-button purple--text font-weight-bold">Cinemap</span>
          </v-toolbar-title>

        <!-- <v-btn icon>
          <v-icon>mdi-heart</v-icon>
        </v-btn> -->
  
        <v-btn icon class="ms-2">
          <!-- 돋보기 아이콘 <font-awesome-icon icon="fa-solid fa-magnifying-glass" size="3x"/>-->
          <router-link :to="{ name: 'reviews' }"><font-awesome-icon icon="fa-solid fa-magnifying-glass" size="2x" color="purple"/></router-link>
        </v-btn>

        <v-spacer></v-spacer>

        <v-btn text rounded @click="goBack" color="purple" class="me-3">BACK</v-btn>
        
        <v-menu v-if="isLoggedIn" offset-y >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              icon
              v-bind="attrs"
              v-on="on"
            >
              <v-avatar color="grey" size="47" class="me-4">
                <img :src="profileImage" alt=""></v-avatar>
            </v-btn>
          </template>
          <v-list width="150px" height="160px" color="purple lighten-5">
            <v-subheader class="">
              <!-- <v-avatar color="grey" size="40">
                <img :src="profileImage" alt="">
              </v-avatar> -->
              <v-list-item-title class="text-center"> Hi😊
                <span class="font-weight-bold purple--text"> {{ username }}</span>
              
              </v-list-item-title>
            </v-subheader>
            <v-list-item-group  color="purple">
              <v-list-item v-for="(item, i) in items" :key="i" dense >
                <v-list-item-content>
                  <v-list-item-title v-if="i === 0" class="text-center">
                    <button @click="moveProfile(username)" class="text-button font-weight-bold">
                      <!-- <v-icon class="me-2">mdi-account</v-icon> -->
                      profile
                      </button>
                  </v-list-item-title>
                  <v-list-item-title v-else-if="i === 1" class="text-center">
                    <button @click="logout" class="text-button font-weight-bold">Logout</button>

                  </v-list-item-title>
                </v-list-item-content>

              </v-list-item>
            </v-list-item-group>

          </v-list>
          
        </v-menu>
      </v-app-bar>
  </nav>
</template>

<script>
  import router from '@/router'
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'NavBar',

    data: () => ({
      
      items: [
        { text: 'profile', icon: 'mdi-account'},
        { text: 'logout', icon: 'mdi-account' },
      ],
    }),

    computed: {
      ...mapGetters(['isLoggedIn', 'currentUser', 'getProfileImage',]),
      username() {
        return this.currentUser.username ? this.currentUser.username : 'guest'
      },
      profileImage() {
        return this.getProfileImage
      },
    },
    methods: {
    ...mapActions(['logout', 'fetchProfile', ]),
    
    moveProfile(username) {
      this.fetchProfile({ username })
      router.push({ name:'profile', params: { username } })
    },
    goBack(){
      this.$router.go(-1)
    },
  },
  }
</script>

<style>
nav {
  z-index: 1;
}

/* .my-navbar {
  position: sticky;
  top: 4px;
} */
</style>