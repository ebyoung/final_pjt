<template>
  <v-list rounded color="purple lighten-5">
    
    <comment-form></comment-form>
    <v-list-item-group rounded class="d-flex">
      <!-- https://vuetifyjs.com/en/components/lists/#three-line -->
      <div>
        <comment-list-item 
          v-for="comment in comments" 
          :comment="comment" 
          :key="comment.id">
        </comment-list-item>        
      </div>
    </v-list-item-group>

  </v-list>
</template>

<script>
import CommentListItem from '@/components/reviews/CommentListItem.vue'
import CommentForm from '@/components/reviews/CommentForm.vue'
// import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'CommentList',
  components: { CommentForm, CommentListItem },
  props: { comments: Array },
}
</script>

<style>
/* .comment-list {
  background-color: #b093e573;
} */
</style>