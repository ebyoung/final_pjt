<template>
  <div :style='`position:absolute;top:${top}%;left:${left}%;`'>
    <font-awesome-icon @click="openCarousel" icon="fa-solid fa-location-dot"/>
    <v-carousel
      v-if="isCarousel"
      cycle
      height="200"
      hide-delimiter-background
      show-arrows-on-hover
    >
      <v-carousel-item
        v-for="(image, i) in images"
        :key="i"
      >
        <v-sheet
          height="100%"
        >
          <v-row
            class="fill-height"
            align="center"
            justify="center"
          >
          <img class='carousel-image' :src="images[i]">
          </v-row>
        </v-sheet>
      </v-carousel-item>
    </v-carousel>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'MapPoint',
  props: {
    top: Number,
    left: Number,
    targetMovie: Object,
  },
  data () {
    return {
      HOST: 'http://localhost:8000',
      isCarousel: false,
    }
  },
  computed: {
    ...mapGetters(['movies']),
    images() {
      return [
        this.HOST + this.targetMovie.image1,
        this.HOST + this.targetMovie.image2,
        this.HOST + this.targetMovie.image3,
        this.HOST + this.targetMovie.image4,
        this.HOST + this.targetMovie.image5,
      ]
    },
  },
  methods: {
    ...mapActions(['fetchMovies', 'moveToRecom']),
    openCarousel() {
      this.isCarousel = !this.isCarousel
    },
  },
  created() {
    this.fetchMovies()
  }
}
</script>

<style scoped>
.carousel-image {
  width: 100%;
  cursor: pointer;
  object-fit: cover;
}
</style>