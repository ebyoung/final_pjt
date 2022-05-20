<template>
  <div class='d-flex justify-content-center'>
    <div class="main">  	
		<input type="checkbox" id="chk" aria-hidden="true">

			<div class="login">
				<form @submit.prevent="login(credentials_login)">
					<label for="chk" aria-hidden="true">로그인</label>
          <input v-model="credentials_login.username" type="text" id="username" placeholder="Username" required />
          <input v-model="credentials_login.password" type="password" id="password" placeholder="Password" required />
					<button>로그인</button>
				</form>
			</div>

			<div class="signup" @submit.prevent="signup(credentials_signup)">
				<form>
					<label for="chk" aria-hidden="true">회원 가입</label>
          <input v-model="credentials_signup.username" type="text" id="username" placeholder="Username" required/>
					<input v-model="credentials_signup.password1" type="password" id="password1" placeholder="Password" required />
					<input v-model="credentials_signup.password2" type="password" id="password2" placeholder="Password Confirmation" required />
					<button>회원 가입</button>
				</form>
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
        }
      }
    },
  computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['login', 'signup'])
    },
}
</script>

<style scoped>
  .main{
    width: 350px;
    height: 500px;
    background: #9e6ef6;
    overflow: hidden;
    border-radius: 10px;
    box-shadow: 5px 20px 50px #000;
  }
  #chk{
    display: none;
  }
  .login{
    position: relative;
    width:100%;
    height: 100%;
  }
  label{
    color: #fff;
    font-size: 2.3em;
    justify-content: center;
    display: flex;
    margin: 60px;
    font-weight: bold;
    cursor: pointer;
    transition: .5s ease-in-out;
  }
  input{
    width: 60%;
    height: 20px;
    background: #e0dede;
    justify-content: center;
    display: flex;
    margin: 20px auto;
    padding: 10px;
    border: none;
    outline: none;
    border-radius: 5px;
  }
  button{
    width: 60%;
    height: 40px;
    margin: 10px auto;
    justify-content: center;
    display: block;
    color: #fff;
    background: #573b8a;
    font-size: 1em;
    font-weight: bold;
    margin-top: 20px;
    outline: none;
    border: none;
    border-radius: 5px;
    transition: .2s ease-in;
    cursor: pointer;
  }
  button:hover{
    background: #6d44b8;
  }
  .signup{
    height: 460px;
    background: #eee;
    border-radius: 60% / 10%;
    transform: translateY(-180px);
    transition: .8s ease-in-out;
  }
  .signup label{
    color: #573b8a;
    transform: scale(.6);
  }

  #chk:checked ~ .signup{
    transform: translateY(-500px);
  }
  #chk:checked ~ .signup label{
    transform: scale(1);	
  }
  #chk:checked ~ .login label{
    transform: scale(.6);
  }
</style>