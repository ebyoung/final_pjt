const HOST = 'http://localhost:8000/'

const ACCOUNTS = 'accounts/'
const REVIEWS = 'reviews/'
const COMMENTS = 'comments/'

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    follow: (username) => HOST + ACCOUNTS + 'follow/' + username + '/',
    // Token 으로 현재 user 판단
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    // username으로 프로필 제공
    profile: username => HOST + ACCOUNTS + 'profile/' + username,
  },
  
  reviews: {
    // /reviews/
    reviews: () => HOST + REVIEWS,
    // /reviews/1/
    review: reviewPk => HOST + REVIEWS + `${reviewPk}/`,
    likeReview: reviewPk => HOST + REVIEWS + `${reviewPk}/` + 'like/',
    comments: reviewPk => HOST + REVIEWS + `${reviewPk}/` + COMMENTS,
    comment: (reviewPk, commentPk) =>
      HOST + REVIEWS + `${reviewPk}/` + COMMENTS + `${commentPk}/`,
  },
}
