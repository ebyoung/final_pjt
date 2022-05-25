<template>
  <iframe :src="videoKey + '&start=10'" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"></iframe>
</template>

<script>
export default {
  name: 'MovieTrailer',
  props: {
    videoKey: String,
  },
  computed: {
  }
}
</script>

<style scoped>
iframe {
  /* position: absolute; */
  /* margin-top: -150px; */
  width: 100%;
  aspect-ratio: 16/9;
}
</style>