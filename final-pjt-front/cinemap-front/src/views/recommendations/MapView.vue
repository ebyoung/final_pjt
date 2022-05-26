<template>
  <div class="distribution-map">
    <div class="my-welcome-message text-center">
      지도에서 <font-awesome-icon  icon="fa-solid fa-location-dot" size="xl" color="#5E35B1"/>
      을 클릭하면 세계 여행 출발합니다. </div>
    <img src="@/assets/worldmapcolorborder.png" alt="" />

    <MapPoint :top='34' :left='23' :targetMovie='mapMovies[0]'/>
    <MapPoint :top='42' :left='72' :targetMovie='mapMovies[1]'/>
    <MapPoint :top='38' :left='82' :targetMovie='mapMovies[2]'/>
    <MapPoint :top='40' :left='11' :targetMovie='mapMovies[3]'/>
    <!-- 어바웃 -->
    <MapPoint :top='29' :left='43' :targetMovie='mapMovies[4]'/>
    <!-- 먹고기도하고 -->
    <MapPoint :top='60' :left='77' :targetMovie='mapMovies[5]'/>
    <!-- 월터 -->
    <MapPoint :top='24' :left='40' :targetMovie='mapMovies[6]'/>
    <!-- 비포선셋 -->
    <MapPoint :top='32' :left='45' :targetMovie='mapMovies[7]'/>
    <!-- 호빗 -->
    <MapPoint :top='78' :left='90' :targetMovie='mapMovies[8]'/>

    <div v-bind:class="{ active: isActive }" class="toast" >
        <div class="toast-content">
          <div class="message">
            <div class="d-flex justify-space-between">
              
              <div v-if="isFirst"  class="mt-0">
                <div class="text-button font-weight-bold">리뷰를 작성하시면</div> 
                <div class="text-button font-weight-bold">영화를 추천 드려요😊</div> 
              </div>
              <div v-else class="mt-0">
                <div class="text-button font-weight-bold" >{{ currentUser.username}}<span class="text-button me-0">님께만</span></div> 
                <div class="text-button">추천 드려요😊</div> 
              </div>
              <v-btn icon color="deep-purple" class="my-exit ms-3">
                <font-awesome-icon @click="closeToast" 
                  size="xl" icon="fa-solid fa-circle-xmark"/>
              </v-btn>
            </div>
              <div class="portfolio-item portfolio-effect__item portfolio-item--eff1">
                <img class="portfolio-item__image" :src="isFirst? selected.poster_path : selected.posterPath" alt="Portfolio Item" width="826" height="551">
                <div class="portfolio-item__info">
                  <h3 class="portfolio-item__header">{{ selected.title }}</h3>
                  <div class="portfolio-item__links">
                    <div class="portfolio-item__link-block">
                      <p class="portfolio-item__link" @click="moveToRecom(selected.movieId)">보러 가기</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        <div v-bind:class="{ active: isActive }" class="progress"></div>
    </div>
    <div class="text-overline  text-center black--text text--lighten-4 font-weight-bold">잠깐!! 어떤 영화를 봐야 할지 고민되시나요? 
    <v-btn icon  @click="getRecommend"><font-awesome-icon icon="fa-solid fa-rocket" 
      color="purple" size="xl"/></v-btn>
      을 클릭해주세요!
    </div>
    


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
        isFirst: false,
        timer1: '',
        timer2: '',
      }
    },
    components: {
      MapPoint,
    },
    computed: {
      ...mapGetters(['mapMovies', 'userRecommendations', 'movies', 'currentUser']),
    },
    methods: {
      ...mapActions(['getMapMovies', 'getUserRecommendations', 'moveToRecom', 'fetchMovies']),
      selectRecommendMovie() {
        if (this.userRecommendations.length > 0) {
          return _.sample(this.userRecommendations)
        }
        else {
          this.isFirst = true
          return _.sample(this.movies)
        }
      },
      getRecommend() {
        this.selected = this.selectRecommendMovie()
        this.isActive = true
        this.timer1 = setTimeout(() => {
          this.isActive = false
        }, 10000)
        this.timer2 = setTimeout(() => {
          this.isActive = false
        }, 10000);
      },
      closeToast() {
        this.isActive = false
        clearTimeout(this.timer1)
        clearTimeout(this.timer2)
      },
    },
    created() {
      this.getMapMovies()
      this.fetchMovies()
      this.getUserRecommendations()
      setTimeout(() => {
          this.getRecommend()
        }, 900)
    },
  }
</script>

<style scoped>


  .my-exit {
    background-color: transparent;
  }

  .my-welcome-message {
    font-size: 25px;
    /* font-family: 'Noto Sans KR', sans-serif; */
    font-family: 'Hahmlet', serif;
    font-weight: bolder;
    color: rgba(158, 23, 231, 0.827);
    /* font-family: 'Nanum Gothic Coding', monospace; */
    margin-bottom: 40px;
    margin-top: 20px;
  }

  h1 {
    left: 45%;
    position: absolute;
    /* font-family: 'Noto Sans KR', sans-serif; */
  }

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

  .toast{
      position: absolute;
      top: 57%;
      right: 81px;
      border-radius: 10px;
      background: rgba(248, 243, 248, 0.585);
      padding: 10px 5px 20px 5px;
      border-left: 4px solid #9f51f9;
      border-top: 4px solid #ac40f4;
      border-right: 4px solid #590690be;
      overflow: hidden;
      transform: translateX(calc(300%));
      transition: all 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.35);
  }

  .toast.active{
      transform: translateX(130%);
  }

  .toast .toast-content{
      display: flex;
      align-items: center;
  }

  .toast-content .message{
      display: flex;
      flex-direction: column;
      margin: 0 21px;
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

  .message .text.text-first{
      font-size: 12px;
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
      background-color: #42016db6;
  }

  .progress.active:before{
      animation: progress 10s linear forwards;
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
      /* background-color: #4070f4; */
      color: #fff;
      border-radius: 6px;
      cursor: pointer;
      transition: 0.3s;
  }

  button:hover{
      background-color: #c9a9f4a7;
  }

  .toast.active ~ button{
      pointer-events: none;
  }

  .portfolio-item__image {
    width: 150px;
    height: 250px;
    border-radius: 10px;
    object-fit: cover;
    cursor: pointer;
  }
</style>

<style lang="scss" scoped>
//VARIABLES
$accent-theme-color: #7A306C;
$accent-theme-color2: #8D909B;
$dark-theme-color: #101010;
$light-theme-color: #fff;

$portfolio-item-width: 150px;
$portfolio-item-height: 250px ;

$portfolio-item-info-offset: 5px;

$portfolio-link-dimensions: 100%;
$portfolio-link-offset: 10px;

//MIXINS

//transitions mixin
@mixin transition-mix($property: all, $duration: 0.2s, $timing: linear, $delay: 0s) {
  transition-property: $property;
  transition-duration: $duration;
  transition-timing-function: $timing;
  transition-delay: $delay;
}

//position absolute mixin
@mixin position-absolute ($top: null, $left: null, $right: null, $bottom: null) {
  position: absolute;
  top: $top;
  left: $left;
  right: $right;
  bottom: $bottom;
}

//mixin for image positioning
// @mixin img-position($max-width: 200%, $max-height: 200%) {
//   position: relative;
//   overflow: hidden;

//   img {
//     @include position-absolute($top: 50%, $left: 50%);

//     width: auto;
//     height: auto;
//     min-width: 100%;
//     min-height: 100%;
//     max-width: $max-width;
//     max-height: $max-height;
//     transform: translate(-50%, -50%);
//   }
// }

/* effects styles !!!YOU NEED THEM */

/* don't forget to add your own colors and parameters */

.portfolio-effect {
  display: flex;
  justify-content: space-between;
}

.portfolio-item {
  // @include img-position();
  
  width: $portfolio-item-width;
  height: $portfolio-item-height;
}

.portfolio-item__info {
  @include position-absolute($top: $portfolio-item-info-offset, $left: $portfolio-item-info-offset);
  
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: calc(100% - 2 * #{$portfolio-item-info-offset});
  height: calc(100% - 2 * #{$portfolio-item-info-offset});
  
  background-color: rgba(255,255,255, .7);
}

.portfolio-item__header {
  position: relative;
  
  margin: 0 0 20px 0;
  padding: 15px 0;
  
  font: {
    size: 15px;
  }
  text-transform: uppercase;
  letter-spacing: 2px;
  
  &:after {
    @include position-absolute($bottom: 0, $left: 0);
    
    display: block;
    height: 2px;
    width: 100%;
    
    content: '';
    
    background-color: $accent-theme-color2;
  }
}

.portfolio-item__links {
  display: flex;
}

.portfolio-item__link-block {
   position: relative;
  
   width: $portfolio-link-dimensions;
   height: $portfolio-link-dimensions;
   margin-right: $portfolio-link-offset;
  
  &:last-child {
    margin-right: 0;
  }
}

.portfolio-item__link {
  @include transition-mix;
  
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
  font-weight: bolder;
  
  color: $dark-theme-color;
  text-decoration: none;
  cursor: pointer;
}

/* EFFECT #1 STYLES */
.portfolio-item--eff1 {
  
  .portfolio-item__info {
    transform: scale(1.1);
    opacity: 0;
  }
  
  .portfolio-item__header {
    top: -10px;
    opacity: 0;
    
    &:after {
      transform: scaleX(0);
    }
  }
  
  .portfolio-item__link-block {
    top: 20px;
    
    opacity: 0;
  }
}

.portfolio-item--eff1:hover {
 
  .portfolio-item__info {
    @include transition-mix($duration: .4s);
    
    transform: scale(1);
    opacity: 1;
  }
  
  .portfolio-item__header {
    @include transition-mix($delay: .45s);
    
    top: 0;
    opacity: 1;
    
    &:after {
      @include transition-mix($duration: .3s, $timing: cubic-bezier(0.63, 0.01, 0, 1.39), $delay: .65s);
      
      transform: scaleX(1);
    }
  }
  
  .portfolio-item__link-block {
    top: 0;
    opacity: 1;
    
    &:first-child {
      @include transition-mix($delay: .85s);
    }
    
    &:nth-child(2) {
      @include transition-mix($delay: .95s);
    }
  }
}
</style>