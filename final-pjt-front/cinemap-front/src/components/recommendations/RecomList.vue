<template>
  <div id="example">
    <carousel-3d
    :width="200"
    :height="300"
    :space="300"
    :display="slides+1" 
    :perspective="60"
    >
      <slide v-for="(slide, i) in slides" :index="i" :key="i">
        <img v-if="i===0" @click="changeTrailer(movie)" :src="movie.poster_path">
        <img v-else @click="changeTrailer(movie.recommendations[i])" :src="movie.recommendations[i].poster_path">
      </slide>
    </carousel-3d>
  </div>
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
  }),
  computed: {
    slides() {
        return 7
      },
    },
  methods: {
    changeTrailer(currentMovie) {
      this.$emit('changeTrailer', currentMovie) 
    },
  },
}
</script>

<style scoped>
img {
  height: 100%;
  cursor: pointer;
}


</style>