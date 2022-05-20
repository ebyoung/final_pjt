<template>
  <div class="background d-flex justify-content-center align-items-center p-5">
    <div class="content p-5">
      <h1>Intro</h1>
      <p>안녕하세요</p>
      <p>ㅎㅎ</p>
      <p>ㅎㅎㅎㅎ</p>
      <router-link :to="nextUrl" class="text-decoration-none">START</router-link>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'IntroView',
  computed: {
      ...mapGetters(['isLoggedIn']),
      nextUrl: function() {
        return this.isLoggedIn ? 'map' : 'login'
        },
    },
}
</script>

<style scoped>
.background {
  height: 62.5vw;
}

.background::after {
  background: url('https://pds.joongang.co.kr/news/component/htmlphoto_mmdata/201701/09/htm_20170109115141307904.jpg');
  background-size: cover;
  width: 100%;
  height: 100%;
  opacity: 60%;
  position: absolute;
  top: 0;
  left: 0;
  content: "";
  z-index: -1;
}

.content {
  background: white;
  color: black;
  height: 40%;
}
</style>