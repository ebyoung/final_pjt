<template>
  <div>
    <br>
    <div class="d-flex justify-center">
      <v-chip x-large color="purple lighten-4" class="my-edit text-h4 font-weight-bold mt-5 my-5 px-5 text-center purple--text">😃 Edit Review </v-chip>
    </div>
    <review-form v-if="isReview" :review="review" action="update">
    </review-form>
  </div>

</template>

<script>
import ReviewForm from '@/components/reviews/ReviewForm.vue'
import { mapGetters, mapActions } from 'vuex'
  export default {
    name: 'ReviewEditView',
    components: { ReviewForm },
    computed: {
      ...mapGetters(['review', 'isReview',])
    },
    methods: {
      ...mapActions(['fetchReview'])
    },
    created() {
      this.fetchReview(this.$route.params.reviewPk)
    },
  }
</script>

<style>
/* .my-edit {
  margin-left: 100px;
} */

</style>
