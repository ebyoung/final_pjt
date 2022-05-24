<template>
  <div id="example">
    <carousel-3d :width="200" :height="400">
      <slide v-for="(slide, i) in slides" :index="i" :key="i">
        <img src="https://image.tmdb.org/t/p/w500//x6KSvale7iuxLhsrEfhYNoICyfK.jpg">
      </slide>
    </carousel-3d>
  </div>
  <!-- 세로버전: 별로ㅠ -->
  <!-- <v-expansion-panels popout focusable class="panel">
    <v-expansion-panel @click="changeTrailer(movie.video_key)">
      <v-expansion-panel-header>{{ movie.title }}</v-expansion-panel-header>
      <v-expansion-panel-content>
        <v-row>
          <v-col cols='4' class='pr-0 pb-0'>
            <v-img width="100%" :src="makePosterUrl(movie.poster_path)" alt=""></v-img>
          </v-col>
          <v-col cols='8'>
            <p>{{ movie.overview }}</p>
          </v-col>
        </v-row>
      </v-expansion-panel-content>
    </v-expansion-panel>
    <v-expansion-panel
      v-for="(i) in 5"
      :key="i"
      @click="changeTrailer(movie.recommendations[i].video_key)"
    >
      <v-expansion-panel-header>{{ movie.recommendations[i].title }}</v-expansion-panel-header>
      <v-expansion-panel-content>
        <v-row>
          <v-col cols='4' class='pr-0 pb-0'>
            <v-img width="100%" :src="makePosterUrl(movie.recommendations[i].poster_path)" alt=""></v-img>
          </v-col>
          <v-col cols='8'>
            <p>{{ movie.recommendations[i].overview }}</p>
          </v-col>
        </v-row>
      </v-expansion-panel-content>
    </v-expansion-panel>
  </v-expansion-panels> -->
</template>

<script>
import { Carousel3d, Slide } from 'vue-carousel-3d'

export default {
  name: 'RecomList',
  components: {
    'carousel-3d': Carousel3d,
    'slide': Slide,
  },
  props: {
    movie: Object,
  },
  data:() => ({
    tmdb: 'https://image.tmdb.org/t/p/w500/',
    slides: 7,
  }),
  computed: {
    recommendations() {
      return this.movie.recommendations
    },
  },
  methods: {
    makePosterUrl(poster_path) {
      return this.tmdb + poster_path
    },
    changeTrailer(videoKey) {
      this.$emit('changeTrailer', videoKey) 
    },
  },
}
</script>

<style scoped>
/* #app > div > div > div.col.col-4 > div > div.v-expansion-panel.v-expansion-panel--active.v-item--active > div > div {
  padding-left: 0;
  padding-bottom: 0;
}
p {
  text-overflow:ellipsis;
  font-size: 1rem;
} */
/* .panel {
  opacity: 0.3;
}

.panel:hover .panel,
.panel.hover .panel {
  opacity: 100%;
} */

#example {
  z-index: 1;
}

img {
  width: 100%;
}


</style>