<template>
  <nav>
    <v-app-bar color="deep-purple accent-1" dark rounded>
        <v-app-bar-nav-icon><font-awesome-icon icon="fa-solid fa-clapperboard" size="2x" /></v-app-bar-nav-icon>
        <!--  -->
  
        <v-toolbar-title>Cinemap</v-toolbar-title>

        <!-- <v-btn icon>
          <v-icon>mdi-heart</v-icon>
        </v-btn> -->
  
        <v-btn icon class="ms-2">
          <!-- 돋보기 아이콘 <font-awesome-icon icon="fa-solid fa-magnifying-glass" size="3x"/>-->
          <router-link :to="{ name: 'reviews' }"><font-awesome-icon icon="fa-solid fa-magnifying-glass" size="2x" color="white"/></router-link>
        </v-btn>

        <v-spacer></v-spacer>
  
        <v-menu v-if="isLoggedIn"
          left
          bottom
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              icon
              v-bind="attrs"
              v-on="on"
            >
              <v-avatar color="grey" size="47">
                <img :src="profileImage" alt=""></v-avatar>
            </v-btn>
          </template>
          <v-list>
            <v-subheader><v-avatar color="grey" size="40">
                <img :src="profileImage" alt=""></v-avatar>
                <span class="ms-1"> Hi! {{ username }}</span>
            </v-subheader>
            <v-list-item-group v-model="selectedItem" color="primary">
              <v-list-item v-for="(item, i) in items" :key="i">
                <v-list-item-icon>
                  <v-icon v-text="item.icon"></v-icon>
                  <!-- <v-btn icon @click="moveProfile(username)">profile</v-btn> -->
                </v-list-item-icon>
                <v-list-item-content>
                  <v-list-item-title v-if="i === 0">
                    <v-btn icon @click="moveProfile(username)">profile</v-btn>
                  </v-list-item-title>
                  <v-list-item-title v-else-if="i === 1">
                    <v-btn icon @click="logout">Logout</v-btn>
                    <!-- <v-btn>
                      <router-link class="text-decoration-none" :to="{ name: 'logout' }">Logout</router-link>
                    </v-btn> -->

                  </v-list-item-title>
                </v-list-item-content>
                <!-- <v-list-item-title v-if="isLoggedIn"><v-btn icon ><router-link class="text-decoration-none" :to="{ name: 'logout' }">Logout
                  </router-link></v-btn></v-list-item-title> -->
              </v-list-item>
            </v-list-item-group>

          </v-list>
          
        </v-menu>
      </v-app-bar>



        <!-- 돋보기 아이콘
        <router-link :to="{ name: 'reviews' }"><font-awesome-icon icon="fa-solid fa-magnifying-glass" size="3x"/></router-link>
      </li> -->

      <!-- <li v-if="!isLoggedIn">
        <router-link :to="{ name: 'login' }">Login</router-link>
      </li>
      <li v-if="!isLoggedIn">
        <router-link :to="{ name: 'signup' }">Signup</router-link>
      </li> -->

      <!-- <li v-if="isLoggedIn">
        <router-link :to="{ name: 'reviewNew' }">New</router-link>
      </li> -->

      <!-- <li v-if="isLoggedIn">
        <v-btn @click="moveProfile(username)">
          {{ currentUser.username }}'s home
        </v-btn>
      </li>
      <li v-if="isLoggedIn">
        <router-link :to="{ name: 'logout' }">Logout</router-link>
      </li>
    </ul> -->
  </nav>
</template>

<script>
  import router from '@/router'
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'NavBar',

    data: () => ({
      selectedItem: 0,
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
        this.setProfileImagePath(this.currentUser.username)
        return this.getProfileImage
      },
    },
    methods: {
    ...mapActions(['logout', 'fetchProfile', 'setProfileImagePath',]),
    
    moveProfile(username) {
      this.fetchProfile({ username })
      router.push({ name:'profile', params: { username } })
    },
  },
  }
</script>

<style></style>