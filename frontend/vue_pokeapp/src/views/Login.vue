<script setup lang="ts">
  import InputComponent from "@/components/InputComponent.vue";
  import CustomButtonComponent from "@/components/CustomButtonComponent.vue";
  import axios from 'axios';
  import {ref} from 'vue';
  import {useRouter} from 'vue-router';

  const username = ref('');
  const password = ref('');
  const errorMessage = ref('');
  const router = useRouter();

  const login = async () => {
    errorMessage.value = '';

    if (!username.value || !password.value) {
      errorMessage.value = 'Usuário e senha não podem ser vazios';
      return;
    }

    try {
      const response = await axios.post('/login', new URLSearchParams({
        username: username.value,
        password: password.value
      }), {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        }
      });

      const { access_token, token_type } = response.data;
      localStorage.setItem('token', access_token);
      await router.push('/');

    } catch (error) {
      if(error.response) {
        errorMessage.value = error.response.data.detail;
      } else {
        errorMessage.value = 'Erro na tentativa de login';
      }
    }
  }
</script>

<template>
  <section class="card">
    <form @submit.prevent="login">
      <div>
        <h1>Login</h1>
      </div>
      <div>
        <label for="inputLogin">Usuário</label>
        <InputComponent id="inputLogin" v-model="username"/>
      </div>
      <div>
        <label for="inputPassword">Senha</label>
        <InputComponent type="password" id="inputPassword" v-model="password"/>
      </div>
      <div>
        <CustomButtonComponent>ENTRAR</CustomButtonComponent>
      </div>
      <div>
      <router-link to="/register">
        <CustomButtonComponent backgroundColor="transparent" textColor="#9C9C9C">REGISTRAR</CustomButtonComponent>
      </router-link>
      </div>
      <div v-if="errorMessage">
        <p>{{ errorMessage }}</p>
      </div>
    </form>
  </section>
</template>

<style scoped>
  p {
    color: red;
    text-align: center;
  }
</style>