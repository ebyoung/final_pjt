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

  /* background: url('https://pds.joongang.co.kr/news/component/htmlphoto_mmdata/201701/09/htm_20170109115141307904.jpg'); */

  background: linear-gradient(rgb(226, 210, 236), 50%, rgb(187, 148, 213));
  /* background: url('https://www.themoviedb.org/t/p/original/nlPCdZlHtRNcF6C9hzUH4ebmV1w.jpg');
  background-size: cover; */
  /* background: linear-gradient(#2c3b895e, 70%, #8c465971); */

  
  /* background: linear-gradient(70deg, #b093e573, rgb(252, 134, 252)); */
  /* background: linear-gradient(70deg, blue, pink); */
  /* padding: 15px 25px 65px; */
}


</style>