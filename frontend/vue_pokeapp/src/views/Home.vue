<script setup>
import PokemonSquareComponent from "@/components/PokemonSquareComponent.vue";
import PaginatorComponent from "@/components/PaginatorComponent.vue";
import axios from 'axios';
import { ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const searchQuery = ref('');
const pokemonList = ref([]);
const currentPage = ref(1);
const itemsPerPage = ref(6);
const totalItems = ref(0);
const totalPages = ref(0);
const isLoading = ref(false);

const router = useRouter();

onMounted(async () => {
  fetchPokemons();
});

const fetchPokemons = async () => {
  isLoading.value = true;
  try {
    const offset = (currentPage.value - 1) * itemsPerPage.value;
    const response = await axios.get('http://localhost:8000/api/', {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`
      },
      params: {
        limit: itemsPerPage.value,
        offset,
        query: searchQuery.value
      }
    });

    pokemonList.value = response.data.results;
    totalItems.value = response.data.count;
    totalPages.value = Math.ceil(response.data.count / itemsPerPage.value);

    if (currentPage.value > totalPages.value) {
      currentPage.value = totalPages.value;
    }
  } catch (error) {
    if (error.response && error.response.status === 401) {
      localStorage.removeItem('token');
      router.push('/login');
    } else if (error.response && error.response.status === 404) {
      console.log('Pokémon não encontrado.');
      pokemonList.value = [];
      totalItems.value = 0;
      totalPages.value = 1;
    }
    console.log('Erro ao buscar os pokemons', error);
  } finally {
    isLoading.value = false;
  }
};

const filteredPokemonList = computed(() => {
  return pokemonList.value.filter(pokemon =>
    pokemon.name.toLowerCase().includes(searchQuery.value.toLowerCase())
  );
});

function capitalize(string) {
  return string.charAt(0).toUpperCase() + string.slice(1);
}

const handlePageChange = (page) => {
    currentPage.value = page;
    fetchPokemons();
};
</script>

<template>
  <section class="main">
    <div class="header">
      <h1>Olá! <br><span>Seja bem vindo a central de Pokemons!</span></h1>
      <input v-model="searchQuery" placeholder="Encontre seu pokemon" type="text">
        <div v-if="isLoading" class="loadingMessage">
          Buscando Pokemons...
        </div>
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
      <PaginatorComponent
        :totalItems="totalItems"
        :itemsPerPage="itemsPerPage"
        :currentPage.sync="currentPage"
        :totalPages="totalPages"
        @update:currentPage="handlePageChange"
      />
    </div>
  </section>
</template>


<style scoped>
  .header, .loadingMessage {
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
    min-height: 620px;
  }

  .loadingMessage {
    font-family: 'Heebo', sans-serif;
    font-weight: 600;
    font-size: 24px;
  }
</style>