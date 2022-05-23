<template>
  <nav>
    <ul>
      <li>
        <!-- 돋보기 아이콘 -->
        <router-link :to="{ name: 'reviews' }">둘러보기</router-link>
      </li>

      <li v-if="!isLoggedIn">
        <router-link :to="{ name: 'login' }">Login</router-link>
      </li>
      <li v-if="!isLoggedIn">
        <router-link :to="{ name: 'signup' }">Signup</router-link>
      </li>

      <!-- <li v-if="isLoggedIn">
        <router-link :to="{ name: 'reviewNew' }">New</router-link>
      </li> -->
      <li v-if="isLoggedIn">
        <v-btn @click="moveProfile(username)">
          {{ currentUser.username }}'s home
        </v-btn>
      </li>
      <li v-if="isLoggedIn">
        <router-link :to="{ name: 'logout' }">Logout</router-link>
      </li>
    </ul>
  </nav>
</template>

<script>
  import router from '@/router'
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'NavBar',
    computed: {
      ...mapGetters(['isLoggedIn', 'currentUser']),
      username() {
        return this.currentUser.username ? this.currentUser.username : 'guest'
      },
    },
    methods: {
    ...mapActions(['fetchProfile',]),
    
    moveProfile(username) {
      this.fetchProfile({ username })
      router.push({ name:'profile', params: { username } })
    },
  },
  }
</script>

<style></style>