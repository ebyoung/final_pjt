<template>
  
  <!-- <div id="app">
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </nav>
    <router-view/>
  </div> -->

  
  <v-app id="app">
    <nav-bar></nav-bar>
    <hr />
    <router-view></router-view>
  </v-app>

</template>


<script>
  import NavBar from '@/components/NavBar.vue'

  import { mapActions } from 'vuex'

  export default {
    name: 'App',
    components: { NavBar },
    methods: {
      ...mapActions(['fetchCurrentUser'])
    },
    created() {
      this.fetchCurrentUser()
    }
  }
</script>

<style>
#app {
  background: linear-gradient(#f6dbd85c, 70%, rgba(215, 133, 248, 0.613));
  height: 100%;
  /* background: linear-gradient(70deg, #b093e573, rgb(252, 134, 252)); */
  /* background: linear-gradient(70deg, blue, pink); */
  /* padding: 15px 25px 65px; */
}


</style>