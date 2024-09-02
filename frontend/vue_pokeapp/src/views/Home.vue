<script setup>
  import PokemonSquareComponent from "@/components/PokemonSquareComponent.vue";
  import axios from 'axios';
  import { ref, computed, onMounted } from 'vue'
  import {useRouter} from 'vue-router';


  const searchQuery = ref('');
  const pokemonList = ref([]);
  const router = useRouter();

  onMounted(async () => {
    try {
      const response = await axios.get('/', {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('token')}`
        }
      });
      console.log(response.data.results)
      pokemonList.value = response.data.results;
    } catch (error) {
      if(error.response && error.response.status === 401) {
        localStorage.removeItem('token');
        router.push('/login');
      }
      console.log('Erro ao buscar os pokemons', error);
    }
  });

  const filteredPokemonList = computed(() => {
    return pokemonList.value.filter(pokemon =>
      pokemon.name.toLowerCase().includes(searchQuery.value.toLowerCase())
    );
  });

  function capitalize(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}
</script>

<template>
  <section class="main">
    <div class="header">
      <h1>Olá! <br><span>Seja bem vindo a central de Pokemons!</span></h1>
      <input v-model="searchQuery" placeholder="Encontre seu pokemon" type="text">
    </div>

    <div class="pokemonGallery">
      <PokemonSquareComponent
        v-for="pokemon in filteredPokemonList"
        :key="pokemon.name"
        :pokemonName="capitalize(pokemon.name)"
        :pokemonImage="pokemon.image"
        :pokemonColor="pokemon.color"
      />
    </div>

    <div class="paginator">

    </div>
  </section>
</template>

<style scoped>
  .header {
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
  }

  h1 {
    line-height: 52.88px;
  }

  span {
    font-weight: 400;
  }
  .search {
    position: relative;
    width: 100%;
  }
  input {
    width: 773px;
    padding: 10px 40px 10px 20px;
    border-radius: 20px;
    border: 1px solid #ccc;
    font-size: 24px;
    color: #00000080;
    background: url("@/assets/Search.png") no-repeat right 20px center / 30px 30px #ffffff;
  }

  input:focus {
    outline: none;
  }

  .pokemonGallery {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 60px;
    padding: 50px 0;
  }
</style>