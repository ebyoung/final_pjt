import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

import _ from 'lodash'
// import accounts from './accounts'

export default {
  // namespaced: true,
  state: {
    reviews: [],
    review: {},
  },

  getters: {
    // reviews를 인기(좋아요 or 댓글 수) 순대로 정렬해서 저장해야함. 
    reviews: state => state.reviews,
    review: state => state.review,
    isAuthor: (state, getters) => {
      return state.review.user?.username === getters.currentUser.username
    },
    isReview: state => !_.isEmpty(state.review),
  },

  mutations: {
    SET_REVIEWS: (state, reviews) => state.reviews = reviews,
    SET_REVIEW: (state, review) => state.review = review,
    SET_REVIEW_COMMENTS: (state, comments) => (state.review.comments = comments),
  },

  actions: {
    fetchReviews({ commit, getters }) {
      /* 게시글 목록 받아오기
      GET: reviews URL (token)
        성공하면
          응답으로 받은 게시글들을 state.articles에 저장
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.reviews.reviews(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_REVIEWS', res.data))
        .catch(err => console.error(err.response))
    },

    fetchReview({ commit, getters }, reviewPk) {
      /* 단일 게시글 받아오기
      GET: review URL (token)
        성공하면
          응답으로 받은 게시글들을 state.reviews에 저장
        실패하면
          단순 에러일 때는
            에러 메시지 표시
          404 에러일 때는
            NotFound404 로 이동
      */
      axios({
        url: drf.reviews.review(reviewPk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_REVIEW', res.data))
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
    },

    createReview({ commit, getters }, review) {
      /* 게시글 생성
      POST: reviews URL (게시글 입력정보, token)
        성공하면
          응답으로 받은 게시글을 state.review에 저장
          ReviewDetailView 로 이동
        실패하면
          에러 메시지 표시
      */
      
      axios({
        url: drf.reviews.reviews(),
        method: 'post',
        data: review,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_REVIEW', res.data)
          router.push({
            name: 'review',
            params: { reviewPk: getters.review.pk }
          })
        })
        .catch(err => console.error(err.response))
    },

    updateReview({ commit, getters }, { reviewPk, movie_title, content, movie_poster, vote }) {
      /* 게시글 수정
      PUT: review URL (게시글 입력정보, token)
        성공하면
          응답으로 받은 게시글을 state.article에 저장
          ArticleDetailView 로 이동
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.reviews.review(reviewPk),
        method: 'put',
        data: { movie_title, content, movie_poster, vote },
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_REVIEW', res.data)
          router.push({
            name: 'review',
            params: { reviewPk: getters.review.pk }
          })
        })
        .catch(err => console.error(err.response))
    },

    deleteReview({ commit, getters }, reviewPk) {
      /* 게시글 삭제
      사용자가 확인을 받고
        DELETE: review URL (token)
          성공하면
            state.review 비우기
            AritcleListView로 이동
          실패하면
            에러 메시지 표시
      */
      
      if (confirm('정말 삭제하시겠습니까?')) {
        axios({
          url: drf.reviews.review(reviewPk),
          method: 'delete',
          headers: getters.authHeader,
        })
          .then(() => {
            commit('SET_REVIEW', {})
            router.push({ name: 'reviews' })
          })
          .catch(err => console.error(err.response))
      }
    },

    likeReview({ commit, getters }, reviewPk) {
      /* 좋아요
      POST: likereview URL(token)
        성공하면
          state.review 갱신
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.reviews.likeReview(reviewPk),
        method: 'post',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_REVIEW', res.data))
        .catch(err => console.error(err.response))
    },

		createComment({ commit, getters }, { reviewPk, content }) {
      /* 댓글 생성
      POST: comments URL(댓글 입력 정보, token)
        성공하면
          응답으로 state.review의 comments 갱신
        실패하면
          에러 메시지 표시
      */
      const comment = { content }

      axios({
        url: drf.reviews.comments(reviewPk),
        method: 'post',
        data: comment,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_REVIEW_COMMENTS', res.data)
        })
        .catch(err => console.error(err.response))
    },

    // updateComment({ commit, getters }, { reviewPk, commentPk, content }) {
    //   /* 댓글 수정
    //   PUT: comment URL(댓글 입력 정보, token)
    //     성공하면
    //       응답으로 state.review의 comments 갱신
    //     실패하면
    //       에러 메시지 표시
    //   */
    //   const comment = { content }

    //   axios({
    //     url: drf.reviews.comment(reviewPk, commentPk),
    //     method: 'put',
    //     data: comment,
    //     headers: getters.authHeader,
    //   })
    //     .then(res => {
    //       commit('SET_review_COMMENTS', res.data)
    //     })
    //     .catch(err => console.error(err.response))
    // },

    // deleteComment({ commit, getters }, { reviewPk, commentPk }) {
    //   /* 댓글 삭제
    //   사용자가 확인을 받고
    //     DELETE: comment URL (token)
    //       성공하면
    //         응답으로 state.review의 comments 갱신
    //       실패하면
    //         에러 메시지 표시
    //   */
    //     if (confirm('정말 삭제하시겠습니까?')) {
    //       axios({
    //         url: drf.reviews.comment(reviewPk, commentPk),
    //         method: 'delete',
    //         data: {},
    //         headers: getters.authHeader,
    //       })
    //         .then(res => {
    //           commit('SET_review_COMMENTS', res.data)
    //         })
    //         .catch(err => console.error(err.response))
    //     }
    //   },
  },
}
