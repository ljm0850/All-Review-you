const MoviePoster = 'https://image.tmdb.org/t/p/original/'
const YoutubeAPI = 'https://www.googleapis.com/youtube/v3/search'
const YoutubeSRC = 'https://youtube.com/embed/'
const YtbKey = process.env.VUE_APP_YOUTUBE_API_KEY

const HOST = 'http://localhost:8000/api/v1/'
const ACCOUNTS = 'accounts/'
const REVIEWS = 'reviews/'
const MOVIES = 'movies/'

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    profile: () => HOST + ACCOUNTS + 'profile/',
    ranking: () => HOST + ACCOUNTS + 'ranking/',
    follow: () => HOST + ACCOUNTS + 'follow/',
    changepassword: () => HOST + ACCOUNTS + 'password/change/',
  },
  movies: {
    setmovie: () => HOST + MOVIES + 'setmovie/',
    getmovie: () => HOST + MOVIES + 'getmovie/',
    best: () => HOST + MOVIES + 'best/',
    poster: () => MoviePoster
  },
  reviews: {
    reviewindex: () =>  HOST + REVIEWS + 'index/',
    reviewcreate: () => HOST + REVIEWS + 'create/',
    reviewdetail: () => HOST + REVIEWS + 'detail/',
    reviewlike: () => HOST + REVIEWS + 'like/',
    reviewcomment: () => HOST + REVIEWS + 'comment/',
    commentdetail: () => HOST + REVIEWS + 'comment/detail/',
  },
  youtube: {
    youtubeurl: () => YoutubeAPI,
    apikey: () => YtbKey,
    videoId: () => YoutubeSRC,
  }
}
