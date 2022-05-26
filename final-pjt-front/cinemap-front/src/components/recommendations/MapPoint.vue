<template>
  <div :style='`position:absolute;top:${top}%;left:${left}%;`'>
    <font-awesome-icon @click="openCarousel" icon="fa-solid fa-location-dot"/>
    <v-carousel
      v-if="isCarousel"
      cycle
      height="290px"
      hide-delimiter-background
      show-arrows-on-hover
      class="carousel-item"
    >
    <div class="header">
      <p>{{ targetMovie.title }}</p>
      <font-awesome-icon class="icon" size="xl" icon="fa-solid fa-circle-xmark" @click="openCarousel" />
    </div>
      <v-carousel-item
        v-for="(image, i) in images"
        :key="i"
      >
        <v-sheet
          height="110%"
        >
          <v-row
            class="fill-height"
            align="center"
            justify="center"
          >
          <img class='carousel-image' @click="moveToRecom(targetMovie.movie_id)" :src="images[i]">
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
.header p {
  position: absolute;
  left: 3%;
  top: 3%;
  font-weight: bolder;
  font-size: 20px;
  color: grey;
  z-index: 1;
}

.header .icon {
  position: absolute;
  right: 3%;
  top: 4%;
  color: grey;
  z-index: 1;
  cursor: pointer;
}

.carousel-image {
  height: 100%;
  cursor: pointer;
  object-fit: cover;
}

.carousel-item {
  border-radius: 20px;
}

#app > div > div > div:nth-child(2) {
  width: 500px;
}
</style>