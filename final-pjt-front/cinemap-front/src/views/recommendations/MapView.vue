<template>
  <div class="distribution-map">
    <img src="@/assets/worldmapcolor.png" alt="" />

    <MapPoint :top='37' :left='11' :targetMovie='mapMovies[0]'/>
    <MapPoint :top='25' :left='43' :targetMovie='mapMovies[0]'/>

    <div v-bind:class="{ active: isActive }" class="toast" >
        <div class="toast-content">
          <div class="message">
            <div class="d-flex justify-space-between">
              <span class="text text-1">좋아하실 만한 영화가 있어요.</span>
              <font-awesome-icon icon="fa-solid fa-xmark close" @click="closeToast"/>
            </div>
            <span class="text text-2">{{ selected.title }}</span>
          </div>
        </div>
        <div v-bind:class="{ active: isActive }" class="progress"></div>
    </div>
    <button class="purple" @click="getRecommend">맞춤 추천 받기</button>
  </div>
</template>

<script>
  import MapPoint from '@/components/recommendations/MapPoint.vue'
  import { mapActions, mapGetters } from 'vuex'
  import _ from 'lodash'

  export default {
    name: 'MapView',
    data() {
      return {
        selected: {},
        isActive: false,
        timer1: '',
        timer2: '',
      }
    },
    components: {
      MapPoint,
    },
    computed: {
      ...mapGetters(['mapMovies', 'userRecommendations']),
    },
    methods: {
      ...mapActions(['getMapMovies', 'getUserRecommendations']),
      selectRecommendMovie() {
        if (this.userRecommendations.length > 0) {
          return _.sample(this.userRecommendations)
        }
         else {
          return { title: '리뷰를 작성하시면 알려드릴게요.' }
        }
      },
      getRecommend() {
        this.selected = this.selectRecommendMovie()
        this.isActive = true
        this.timer1 = setTimeout(() => {
          this.isActive = false
        }, 5000)
        this.timer2 = setTimeout(() => {
          this.isActive = false
        }, 5300);
      },
      closeToast() {
        this.isActive = false
        clearTimeout(this.timer1)
        clearTimeout(this.timer2)
      },
    },
    created() {
      this.getMapMovies()
      this.getUserRecommendations()
      setTimeout(() => {
          this.getRecommend()
        }, 200)
    },
  }
</script>

<style scoped>
  div, img {
    position: relative;
    box-sizing: border-box;
  }
  .distribution-map {
    position: relative;
    width: 70%;
    padding: 20px;
    box-sizing: border-box;
    margin: 0 auto;
  }
  .distribution-map > img {
    width: 100%;
    position: relative;
    margin: 0;
    padding: 0;
  }

  @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
  *{
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: 'Poppins', sans-serif;
  }

  body{
      height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      background-color: #f2f2f2;
      overflow: hidden;
  }

  .toast{
      position: absolute;
      top: 80%;
      right: 30px;
      border-radius: 10px;
      background: #fff;
      padding: 20px 35px 20px 25px;
      border-left: 4px solid #4070f4;
      border-top: 4px solid #4070f4;
      border-right: 4px solid #4070f4;
      overflow: hidden;
      transform: translateX(calc(200%));
      transition: all 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.35);
  }

  .toast.active{
      transform: translateX(60%);
  }

  .toast .toast-content{
      display: flex;
      align-items: center;
  }

  .toast-content .message{
      display: flex;
      flex-direction: column;
      margin: 0 20px;
  }

  .message .text{
      font-size: 20px;
      font-weight: 400;;
      color: #666666;
  }

  .message .text.text-1{
      font-weight: 600;
      color: #333;
  }

  .toast .close{
      position: absolute;
      top: 10px;
      right: 15px;
      padding: 5px;
      cursor: pointer;
      opacity: 0.7;
  }

  .toast .close:hover{
      opacity: 1;
  }

  .toast .progress{
      position: absolute;
      bottom: 0;
      left: 0;
      height: 4px;
      width: 100%;
      background: #ddd;
  }

  .toast .progress:before{
      content: '';
      position: absolute;
      bottom: 0;
      right: 0;
      height: 100%;
      width: 100%;
      background-color: #4070f4;
  }

  .progress.active:before{
      animation: progress 5s linear forwards;
  }

  @keyframes progress {
      100%{
          right: 100%;
      }
  }

  button{
      padding: 12px 20px;
      font-size: 20px;
      outline: none;
      border: none;
      background-color: #4070f4;
      color: #fff;
      border-radius: 6px;
      cursor: pointer;
      transition: 0.3s;
  }

  button:hover{
      background-color: #0e4bf1;
  }

  .toast.active ~ button{
      pointer-events: none;
  }
</style>