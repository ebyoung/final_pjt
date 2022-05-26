<template>
  <div class="my-login">
    <v-carousel
      hide-delimiters
      :show-arrows="false"
      class="carousel"
      height="110%"
      cycle
      :interval="7000">
      <v-carousel-item
        src="https://pds.joongang.co.kr/news/component/htmlphoto_mmdata/201701/09/htm_20170109115141307904.jpg"
      ></v-carousel-item>
      <v-carousel-item
        src="https://www.themoviedb.org/t/p/original/tlCBtqrhbPcuXVXoxmQ0AYfUstt.jpg"
      ></v-carousel-item>
      <v-carousel-item
        src="https://www.themoviedb.org/t/p/original/9qic7AS9L0OdRGltWYd3PFx7gd1.jpg"
      ></v-carousel-item>
    </v-carousel>
    <ul class="nav">
      <li @click="showSignup()">Sign up</li>
      <li @click="showLogin()">Login</li>
    </ul>
    <div class="wrapper">
      <div :class="{'rec-prism-login': isLogin, 'rec-prism-signup' : isSignup, 'rec-prism-thankyou' : isThank}">
        <div class="face face-right">
          <div @keyup.enter="showThankYou()" class="content">
            <h2>Log in</h2>
            <div class="field-wrapper">
              <input v-model="credentials_login.username" type="text" id="login_username" placeholder="Username" required />
              <label>username</label>
            </div>
            <div class="field-wrapper">
              <input v-model="credentials_login.password" type="password" id="login_password" placeholder="Password" required />
              <label>password</label>
            </div>
            <div class="field-wrapper">
              <input type="submit" value="로그인" @click="showThankYou()">
            </div>
            <span class="signup" @click="showSignup()">아직 회원이 아니신가요?</span>
          </div>
        </div>
        <div class="face face-front">
          <div @keyup.enter="showThankYou()" class="content">
            <h2>Sign up</h2>
            <div class="field-wrapper">
              <input v-model="credentials_signup.username" type="text" id="signup_username" placeholder="Username" required/>
              <label>username</label>
            </div>
            <div class="field-wrapper">
              <input v-model="credentials_signup.password1" type="password" id="signup_password1" placeholder="Password" required />
              <label>password</label>
            </div>
            <div class="field-wrapper">
              <input v-model="credentials_signup.password2" type="password" id="signup_password2" placeholder="Password Confirmation" required />
              <label>re-enter password</label>
            </div>
            <div class="field-wrapper">
              <input type="submit" value="회원가입" @click="showThankYou()">
            </div>
            <span class="singin" @click="showLogin()">이미 회원이신가요?</span>
          </div>
        </div>
        <div class="face face-bottom">
          <div class="content">
            <div class="thank-you-msg">
              Thank you!
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'LoginView',
  components: {
      
    },
    data() {
      return {
        credentials_login: {
          username: '',
          password: '',
        },
        credentials_signup: {
          username: '',
          password1: '',
          password2: '',
        },
        showing: 'login',
      }
    },
  computed: {
      ...mapGetters(['authError']),
      isLogin() {
        return this.showing === 'login'
      },
      isSignup() {
        return this.showing === 'signup'
      },
      isThank() {
        return this.showing === 'thank'
      },
    },
    methods: {
      ...mapActions(['login', 'signup']),
      showSignup(){
        this.showing = 'signup'
      },
      showLogin(){
        this.showing = 'login'
      },
      showThankYou(){
        if (this.showing === 'login') {
          this.showing = 'thank'
          setTimeout(() => {
            this.login(this.credentials_login)
          }, 1500)
        } else {
          this.showing = 'thank'
          setTimeout(() => {
            this.signup(this.credentials_signup)
          }, 1500)
        }
      },
    },
}
</script>

<style scoped>
.my-login {
  /* background: url('https://pds.joongang.co.kr/news/component/htmlphoto_mmdata/201701/09/htm_20170109115141307904.jpg'); */
  /* background-size: cover; */
  /* width: 100%;
  height: 100%;
  opacity: 90%; */
  /* position: absolute;
  top: 0;
  left: 0;
  content: ""; */
}

.carousel {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

</style>

<style lang="scss" scoped>
// Dimensions
$prism-height: 400px;
$prism-length: 300px;
$prism-depth: $prism-length;
$spacing: 20px;
$br: 3px;

// Colors
$text-light: #fff;
$text-dark: rgb(41, 40, 40);
$blue: #b96def9c;
$smoke: #f9f9fa;
$coral: #ff5751;
$navy-blue: #993ad3;
$purple: #d07fdfe5;
$purple2: #9231a3de;

.wrapper{
  width: $prism-length;
  height: $prism-height;
  margin: 60px auto;
  perspective: 600px;
  text-align: left;
}

.rec-prism-login {
  width: 100%;
  height: 100%;
  position: relative;
  transform-style: preserve-3d;
  transform: translateZ(-100px) rotateY( -90deg);
  transition: transform 0.5s ease-in;
}

.rec-prism-signup {
  width: 100%;
  height: 100%;
  position: relative;
  transform-style: preserve-3d;
  transform: translateZ(-100px);
  transition: transform 0.5s ease-in;
}

.rec-prism-thankyou {
  width: 100%;
  height: 100%;
  position: relative;
  transform-style: preserve-3d;
  transform: translateZ(-100px) rotateX( 90deg);
  transition: transform 0.5s ease-in;
}

.face {
  position: absolute;
  width: $prism-length;
  height: $prism-height;
  padding: $spacing;
  background: rgba(249, 247, 250, 0.781);
  border: 3px solid $purple;
  border-radius: 3px;
  
  .content{
    color: $text-dark;
    h2{
      font-size: 1.2em;
      color: $purple2;
    }
    .field-wrapper{
      margin-top: $spacing*1.5;
      position: relative;

      label{
        position: absolute;
        pointer-events: none;
        font-size: 0.85em;
        top: 40%;
        left: 0;
        transform: translateY(-50%);
        transition: all ease-in 0.25s;
        color: lighten($text-dark, 20%);
      }
      input[type="text"], input[type="password"], input[type="submit"], textarea{
        -webkit-appearance: none;
        appearance: none;
        &:focus{
          outline: none;
        }
      }
      input[type="text"], input[type="password"], textarea{
        width: 100%;
        border: none;
        background: transparent;
        line-height: 2em;
        border-bottom: 1px solid $purple;
        color: $text-dark;

        &::-webkit-input-placeholder{
          opacity: 0;
        }
        &::-moz-placeholder{
          opacity: 0;
        }
        &:-ms-input-placeholder{
          opacity: 0;
        }
        &:-moz-placeholder { 
          opacity: 0;
        }
        &:focus, &:not(:placeholder-shown){
          + label{
            top: -35%;
            color: $purple;
          }
        }
      }
      input[type="submit"]{
        -webkit-appearance: none;
        appearance: none;
        cursor: pointer;
        width: 100%;
        background: $purple;
        line-height: 2em;
        color: $text-light;
        border: 1px solid $purple;
        border-radius: $br;
        padding: $spacing/4;
        
        &:hover{
          opacity: 0.9;
        }
        &:active{
          transform: scale(0.96);
        }
      }
      textarea{
        resize: none;
        line-height: 1em;
        &:focus, &:not(:placeholder-shown){
          + label{
            top: -25%;
          }
        }
      }
    }
  }
  
  .thank-you-msg{
    position: absolute;
    width: 200px;
    height: 130px;
    text-align: center;
    font-size: 2em;
    color: $purple2;
    left: 50%;
    top: 50%;
    -webkit-transform: translate(-50%, -50%);
    
    &:after{
      position: absolute;
      content: '';
      width: 50px;
      height: 25px;
      border: 10px solid $purple2;
      border-right: 0;
      border-top: 0;
      left: 50%;
      top: 50%;
      -webkit-transform: translate(-50%, -50%) rotate(0deg) scale(0);
      transform: translate(-50%, -50%) rotate(0deg) scale(0);
      -webkit-animation: success ease-in 0.15s forwards;
      animation: success ease-in 0.15s forwards;
      animation-delay: 2.5s;
    }
  }
  &-front{ 
    transform: rotateY(0deg) translateZ($prism-length/2);  
  }
  &-top{ 
    height: $prism-depth;
    transform: rotateX(90deg) translateZ($prism-depth/2); 
  }
  &-back{ 
    transform: rotateY(180deg) translateZ($prism-length/2); 
  }
  &-right{ 
    transform: rotateY(90deg) translateZ($prism-length/2); 
  }
  &-left{ 
    transform: rotateY(-90deg) translateZ($prism-length/2); 
  }
  &-bottom{ 
    height: $prism-depth;
    transform: rotateX(-90deg) translateZ($prism-height - ($prism-depth/2));
  }
}

.nav{
  text-align: center;
  margin: 100px 0 20px 0;
  padding: 0;
  
  li{
    display: inline-block;
    list-style-type: none;
    font-size: 1em;
    margin: 0 $spacing/2;
    color:$purple2;
    font-weight: bold;
    position: relative;
    cursor: pointer;
    &:after{
      content: "";
      position: absolute;
      bottom: 0;
      left: 0;
      width: 20px;
      border-bottom: 1px solid $purple;
      transition: all ease-in 0.25s;
    }
    &:hover:after{
      width: 100%;
    }
  }
}

.psw, .signup, .singin{
  display: block;
  margin: $spacing 0;
  font-size: 0.75em;
  text-align: center;
  color: $purple2;
  cursor: pointer;
}

small{
  font-size: 0.7em;
}
@-webkit-keyframes success{
    from {
       -webkit-transform: translate(-50%, -50%) rotate(0) scale(0);
       }
    to {
      -webkit-transform: translate(-50%, -50%) rotate(-45deg) scale(1);
    }
}
</style>