<template>
  <nav class="my-navbar">
    <v-app-bar color="transparent" rounded>
        
        <v-toolbar-title >
          <v-btn @click="moveToMap" text rounded x-large>
            <span class="my-logo purple--text">Cinemap</span>
          </v-btn>
          
        </v-toolbar-title>

  
        <v-btn icon>
          <!-- 돋보기 아이콘 <font-awesome-icon icon="fa-solid fa-magnifying-glass" size="3x"/>-->
          <router-link :to="{ name: 'reviews' }"><font-awesome-icon icon="fa-solid fa-magnifying-glass" size="2x" color="purple"/></router-link>
        </v-btn>

        <v-spacer></v-spacer>

        <v-btn v-if="isAdmin" text rounded class="me-1" > 
          <a href="http://127.0.0.1:8000/admin/" class="text-decoration-none grey--text">ADMIN</a>
        </v-btn>
        <v-btn text rounded @click="goBack" color="purple" class="me-3">BACK</v-btn>
        
        <v-menu v-if="isLoggedIn" offset-y  >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              icon class="me-2"
              v-bind="attrs"
              v-on="on"
            >
              <v-avatar color="grey" size="50" class="me-3">
                <img :src="profileImage" alt=""></v-avatar>
            </v-btn>
          </template>
          <v-list width="150px" height="160px" color="purple lighten-5">
            <v-subheader class="">
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
      isAdmin() {
        return this.currentUser.username === "admin"
      }
    },
    methods: {
    ...mapActions(['logout', 'fetchProfile', ]),
    
    moveProfile(username) {
      this.fetchProfile({ username })
      router.push({ name:'profile', params: { username } })
    },
    moveToMap() {
      router.push({ name: 'map'})
    },

    goBack() {
      this.$router.go(-1)
    },
  },
  }
</script>

<style>
nav {
  z-index: 1;
}

.my-logo {
  font-family: 'Monoton', cursive;
  font-size: 30px;
}

/* .my-navbar {
  position: sticky;
  top: 4px;
} */
</style>