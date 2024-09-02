<script setup>
  import InputComponent from "@/components/InputComponent.vue";
  import CustomButtonComponent from "@/components/CustomButtonComponent.vue";
  import axios from 'axios';
  import {ref, computed} from 'vue';
import {useRouter} from 'vue-router';

  const username = ref('');
  const password = ref('');
  const confirmPassword = ref('');
  const errorMessage = ref('');
  const successMessage = ref('');
  const router = useRouter();

  const isFormComplete = computed(()=>{
    return username.value && password.value && confirmPassword.value
  })

  const register = async () => {
    errorMessage.value = '';
    if(password.value !== confirmPassword.value) {
      return errorMessage.value = 'As senhas não são iguais';
    }

    if(password.value.length < 6) {
      return errorMessage.value = 'A senha deve ter pelo menos 6 caracteres'
    }

    try {
        await axios.post('/register', {
        username: username.value,
        password: password.value
      });
      successMessage.value = 'Usuário registrado com sucesso!';
      alert(successMessage.value);
      await router.push('/login');
    } catch (error) {
      if(error.response && error.response.status === 400) {
        errorMessage.value = error.response.data.detail;
      } else {
        errorMessage.value = 'Erro ao registrar usuário';
      }
    }
  }
</script>

<template>
    <section class="card">
    <form @submit.prevent="register">
      <div>
        <h1>Registrar</h1>
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
        <label for="input_confirm_password">Confirme a senha</label>
        <InputComponent type="password" id="input_confirm_password" v-model="confirmPassword"/>
      </div>
      <div>
        <CustomButtonComponent
            :disabled="!isFormComplete"
            :style="{
              opacity: isFormComplete ? 1 : 0.5,
              cursor: isFormComplete ? 'pointer' : 'default'
            }"
            type="submit">REGISTRAR</CustomButtonComponent>
      </div>
      <div v-if="errorMessage">
        <p>{{errorMessage}}</p>
      </div>
    </form>
  </section>
</template>

<style scoped>
  p {
    color: #ff0000;
    text-align: center;
  }
</style>