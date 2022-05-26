<template>
  <div class="background d-flex justify-center align-center p-5">
    <div>
      <div class="my-name">C I N E M A P</div>
      <br>
      <div class="content">
        <div>영화로 떠나는 세계 여행을</div>
        <p>
          <!-- <span class="my-movie">cinemap</span> -->
          <span>시작해 볼까요? 🤩</span>
        </p>
      </div>

      <br>
      <router-link :to="nextUrl" class="text-decoration-none">
        <v-btn block rounded color="deep-purple accent-4" class="white--text">START</v-btn>
        </router-link>
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
  height: 40vw;
  
}

.background::after {
  /* background: url('https://pds.joongang.co.kr/news/component/htmlphoto_mmdata/201701/09/htm_20170109115141307904.jpg'); */
  background: url('https://www.themoviedb.org/t/p/original/nyuzfjAbuSel6dVKY4zFo95ugUf.jpg');
  background-size: cover;
  width: 100%;
  height: 100%;
  opacity: 100%;
  position: absolute;
  top: 0;
  left: 0;
  content: "";
  z-index: -1;
}

.my-name {
  font-family: 'Monoton', cursive;
  font-size: 60px;
  /* color:#60176fa7; */
  color: rgba(232, 179, 246, 0.936);
}

/* .my-movie {
  font-family: 'Monoton', cursive;
  font-size: 20px;
  color:#60176fa7;
} */

.content {
  background: transparent ;
  color: rgba(223, 152, 243, 0.936);
  font-family: 'Hahmlet', serif;
  font-size: 20px;
  height: 100%;
  width: 100%;
  margin: auto;
  text-align: center;
  font-weight: bolder;
  /* border-radius: 10px; */
}
</style>