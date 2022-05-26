import Vue from 'vue'
import VueRouter from 'vue-router'

import HomeView from '@/views/HomeView.vue'
import BoardView from '@/views/BoardView.vue'
import ProfileView from '@/views/ProfileView.vue'
import ReviewCreateView from '@/views/ReviewCreateView.vue'
import ReviewDeleteView from '@/views/ReviewDeleteView.vue'
import ReviewDetailView from '@/views/ReviewDetailView.vue'
import ReviewUpdateView from '@/views/ReviewUpdateView.vue'
import UserUpdateView from '@/views/UserUpdateView.vue'

import LoginView from '@/views/LoginView.vue'
import LogoutView from '@/views/LogoutView.vue'
import signupView from '@/views/SignupView.vue'


import NotFoundView from '@/views/NotFoundView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/board',
    name: 'board',
    component: BoardView
  },
  {
    path: '/reviewcreate',
    name: 'reviewcreate',
    component: ReviewCreateView
  },
  {
    path: '/reviewdelete/:pk',
    name: 'reviewdelete',
    component: ReviewDeleteView,
    props: true
  },
  {
    path: '/reviewdetail/:pk',
    name: 'reviewdetail',
    component: ReviewDetailView,
    props: true
  },
  {
    path: '/reviewupdate/',
    name: 'reviewupdate',
    component: ReviewUpdateView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  {
    path: '/signup',
    name: 'signup',
    component: signupView
  },
  {
    path: '/profile/:username',
    name: 'profile',
    component: ProfileView,
    props: true
  },
  {
    path: '/profile/update/:username',
    name: 'userupdate',
    component: UserUpdateView,
    props: true
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFoundView
  },
  {
    path: '*',
    redirect: '/404'
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
