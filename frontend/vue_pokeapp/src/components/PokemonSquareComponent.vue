<script setup>
  import { ref, onMounted } from "vue";
  import { FastAverageColor } from "fast-average-color";
  const props = defineProps({
    pokemonName: String,
    pokemonImage: String,
    pokemonColor: String
  });

  const defaultColor = ref('#ffffff');
  const fac = new FastAverageColor();

  onMounted(() => {
    fac.getColorAsync(props.pokemonImage).then(color => {
      defaultColor.value = color.hex;
    }).catch(error => {
      console.log('Erro ao calcular cor ideal: ', error);
    });
  });
</script>

<template>
  <div class="square" :style="{ backgroundColor: defaultColor }">
    <h1>{{ props.pokemonName }}</h1>
    <img :src="props.pokemonImage" alt="Foto do pokemon">
  </div>
</template>

<style scoped>
  .square {
    background: #236db0;
    width: 230px;
    height: 230px;
    border-radius: 15px;
    display: flex;
    justify-content: center;
    box-shadow: 0 4px 4px rgba(0, 0, 0, 0.25);
    align-items: center;
    filter: brightness(90%) saturate(80%);
  }

  h1 {
    font-size: 24px;
    position: relative;
    top: 15px;
  }

  .square img {
    width: 171px;
    height: 171px;
  }
</style>