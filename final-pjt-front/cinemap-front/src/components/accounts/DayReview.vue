<template>
  <div class='day-review'>
    <figure v-if="getReview" class="snip1395">
      <img :src="getReview.movie_poster" alt="moviePoster" />
      <figcaption>
        <h2>{{ getReview.movie_title }}</h2>
        <pre>{{ '★'.repeat(getReview.vote) + '☆'.repeat(5 - getReview.vote) }}</pre>
      </figcaption>
      <router-link :to="{ name: 'review', params: { reviewPk: getReview.pk } }"></router-link>
    </figure>
    <img v-else class='white' @click="setWatchDay(date)" src="https://mblogthumb-phinf.pstatic.net/20160602_77/lllyourinlll_1464878597694YQsWS_PNG/a233fb2e4ad22000.png?type=w2" alt="">
    <div class="middle">
      <font-awesome-icon icon="fa-solid fa-circle-plus" size="xl" color="grey"/>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'DayReview',
  props: {
    date: String,
    idx: Number,
  },
  computed: {
    ...mapGetters(['profile', ]),
    getReview() {
      const thisDayReview = this.profile.reviews?.filter(review => this.date === review.watch_day)
      if (thisDayReview) {
        return thisDayReview[0]
      } else {
        return false
      }
    },
  },
  methods: {
    ...mapActions(['setWatchDay', ]),
  },
}
</script>

<style scoped>
@import url(https://fonts.googleapis.com/css?family=Raleway);
@import url(https://fonts.googleapis.com/css?family=Julius+Sans+One);
img {
  width: 112.281px;
  height: 167.292px;
  padding: 0;
  cursor: pointer;
}

.white {
  opacity: 1;
  display: block;
  width: 100%;
  height: auto;
  transition: .5s ease;
  backface-visibility: hidden;
}

.middle {
  transition: .5s ease;
  opacity: 0;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  text-align: center;
}

.day-review:hover .white {
  opacity: 0.3;
}

.day-review:hover .middle {
  opacity: 1;
}

.snip1395 {
  font-family: 'Raleway', Arial, sans-serif;
  position: relative;
  overflow: hidden;
  width: 100%;
  color: #ffffff;
  text-align: left;
  background-color: #ffffff;
  line-height: 1em;
  transform: translateZ(0);
}
.snip1395 * {
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  -webkit-transition: all 0.35s ease-out;
  transition: all 0.35s ease-out;
}
.snip1395 img {
  max-width: 100%;
  vertical-align: top;
  -webkit-transition: all 0.8s ease-out;
  transition: all 0.8s ease-out;
}
.snip1395:before {
  background: #000000;
  position: absolute;
  content: '';
  -webkit-transition: all 0.35s ease-out;
  transition: all 0.35s ease-out;
  -webkit-transition-delay: 0.2s;
  transition-delay: 0.2s;
  z-index: 1;
  top: 0;
  bottom: 0;
  right: 0;
  left: 100%;
  box-shadow: 0 0 40px white;
}
.snip1395 figcaption {
  position: absolute;
  top: 0;
  height: 100%;
  left: 0;
  width: 100%;
  z-index: 2;
}
.snip1395 h2,
.snip1395 pre {
  font-size: 16px;
  margin: 0;
  width: 100%;
  opacity: 0;
  padding: 20px;
}
.snip1395 h2 {
  font-family: 'Julius Sans One', Arial, sans-serif;
  word-break: keep-all;
}
.snip1395 pre {
  position: absolute;
  bottom: 0;
  padding-left: 22px;
  font-size: 0.8em;
  letter-spacing: 1px;
  text-align: right;
}
.snip1395 a {
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  position: absolute;
  z-index: 2;
}
.snip1395:hover img,
.snip1395.hover img {
  opacity: 0.2;
}
.snip1395:hover:before,
.snip1395.hover:before {
  left: 0;
  box-shadow: 0 0 0px white;
  -webkit-transition-delay: 0s;
  transition-delay: 0s;
}
.snip1395:hover figcaption h2,
.snip1395.hover figcaption h2,
.snip1395:hover figcaption pre,
.snip1395.hover figcaption pre {
  -webkit-transition-delay: 0.25s;
  transition-delay: 0.25s;
}
.snip1395:hover figcaption h2,
.snip1395.hover figcaption h2 {
  -webkit-transform: translateY(0%);
  transform: translateY(0%);
  opacity: 0.5;
}
.snip1395:hover figcaption pre,
.snip1395.hover figcaption pre {
  opacity: 0.7;
}

</style>