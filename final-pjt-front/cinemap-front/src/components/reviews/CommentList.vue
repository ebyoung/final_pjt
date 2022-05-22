<template>
  <div class="comment-list">
    
    <comment-form></comment-form>
    <ul>
      <comment-list-item 
        v-for="comment in comments" 
        :comment="comment" 
        :key="comment.id">
      </comment-list-item>        
    </ul>

  </div>
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
  border: 1px solid blue;
} */
</style>