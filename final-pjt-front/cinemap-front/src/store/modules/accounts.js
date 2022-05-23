import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'


export default {
  // namespaced: true,

  // state는 직접 접근하지 않겠다!
  state: {
    token: localStorage.getItem('token') || '' ,
    currentUser: {},
    profile: {},
    authError: null,
    profileImagePath: '',
  },
  // 모든 state는 getters 를 통해서 접근하겠다.
  getters: {
    isLoggedIn: state => !!state.token,
    currentUser: state => state.currentUser,
    profile: state => state.profile,
    isFollow: state => state.profile.followers?.some((user) => user.username === state.currentUser.username),
    authError: state => state.authError,
    authHeader: state => ({ Authorization: `Token ${state.token}`}),
    profileImageUrl: state => state.profile.profile_image,
    getProfileImage: state => state.profileImagePath
  },

  mutations: {
    SET_TOKEN: (state, token) => state.token = token,
    SET_CURRENT_USER: (state, user) => state.currentUser = user,
    SET_PROFILE: (state, profile) => state.profile = profile,
    SET_PROFILEIMAGEPATH: (state, profile_image_path) => state.profileImagePath = profile_image_path, 
    SET_AUTH_ERROR: (state, error) => state.authError = error,
    SET_FOLLOW: (state, data) => {
      state.profile.followers = data.followers
      state.profile.follower_count = data.follower_count
      state.profile.following_count = data.following_count
    },

    
  },

  actions: {
    saveToken({ commit }, token) {
      /* 
      state.token 추가 
      localStorage에 token 추가
      */
      commit('SET_TOKEN', token)
      localStorage.setItem('token', token)
    },

    removeToken({ commit }) {
      /* 
      state.token 삭제
      localStorage에 token 추가
      */
      commit('SET_TOKEN', '')
      localStorage.setItem('token', '')
    },

    login({ commit, dispatch }, credentials) {
      /* 
      POST: 사용자 입력정보를 login URL로 보내기
        성공하면
          응답 토큰 저장
          현재 사용자 정보 받기
          메인 페이지(ArticleListView)로 이동
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.accounts.login(),
        method: 'post',
        data: credentials
      })
        .then(res => {
          const token = res.data.key
          dispatch('saveToken', token)
          dispatch('fetchCurrentUser')
          router.push({ name: 'map' })
        })
        .catch(err => {
          console.error(err.response.data)
          commit('SET_AUTH_ERROR', err.response.data)
        })
    },

    signup({ commit, dispatch }, credentials) {
      /* 
      POST: 사용자 입력정보를 signup URL로 보내기
        성공하면
          응답 토큰 저장
          현재 사용자 정보 받기
          메인 페이지(ArticleListView)로 이동
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.accounts.signup(),
        method: 'post',
        data: credentials
      })
        .then(res => {
          const token = res.data.key
          dispatch('saveToken', token)
          dispatch('fetchCurrentUser')
          router.push({ name: 'map' })
        })
        .catch(err => {
          // console.error(err.response.data)
          commit('SET_AUTH_ERROR', err.response.data)
        })
    },

    logout({ getters, dispatch }) {
      /* 
      POST: token을 logout URL로 보내기
        성공하면
          토큰 삭제
          사용자 알람
          LoginView로 이동
        실패하면
          에러 메시지 표시
      */
      if (confirm('정말로 로그아웃 하시겠습니까?')) {
        axios({
          url: drf.accounts.logout(),
          method: 'post',
          headers: getters.authHeader,
        })
          .then(() => {
            dispatch('removeToken')
            alert('성공적으로 로그아웃 되었습니다!')
            router.push({ name: 'login' })
          })
          .error(err => {
            console.error(err.response)
          })
      }
    },

    follow({ commit, getters }, username) {
      axios({
        url: drf.accounts.follow(username),
        method: 'POST',
        headers: getters.authHeader,
      })
      .then((response) => {
        commit('SET_FOLLOW', response.data)
      })
    },

    fetchCurrentUser({ commit, getters, dispatch }) {
      /*
      GET: 사용자가 로그인 했다면(토큰이 있다면)
        currentUserInfo URL로 요청보내기
          성공하면
            state.cuurentUser에 저장
          실패하면(토큰이 잘못되었다면)
            기존 토큰 삭제
            LoginView로 이동
      */
      if (getters.isLoggedIn) {
        axios({
          url: drf.accounts.currentUserInfo(),
          method: 'get',
          headers: getters.authHeader,
        })
          .then(res => commit('SET_CURRENT_USER', res.data))
          .catch(err => {
            if (err.response.status === 401) {
              dispatch('removeToken')
              router.push({ name: 'login' })
            }
          })
      }
    },

    fetchProfile({ commit, getters }, { username } ) {
      /*
      GET: profile URL로 요청보내기
        성공하면
          state.profile에 저장
      */
      axios({
        url: drf.accounts.profile(username),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          res.data.profile_image = drf.accounts.profileImage(res.data.profile_image)
          commit('SET_PROFILE', res.data)
        })
    },

    updateProfile({ commit, getters }, profileData) {
      axios({
        url: drf.accounts.profile(profileData.username) + '/',
        method: 'post',
        data: profileData,
        headers: {
          ...getters.authHeader,
          'Content-Type': 'multipart/form-data',
        }
      })
        .then(res => {
          res.data.profile_image = drf.accounts.profileImage(res.data.profile_image)
          commit('SET_PROFILE', res.data)
        })
    },


    setProfileImagePath({commit, getters}, username) {
      axios({
        url: drf.accounts.getProfileImagePath(username),
        method: 'get',
        headers: getters.authHeader,
      })
      .then(res => {
        res.data.profile_image = drf.accounts.profileImage(res.data?.profile_image)
        commit('SET_PROFILEIMAGEPATH', res.data.profile_image)
      })
    },
  }
}