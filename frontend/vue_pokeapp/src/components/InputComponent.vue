<script setup>
const props = defineProps({
  modelValue: String
});
</script>

<template>
  <input @input="$emit('update:modelValue', $event.target.value)">
</template>

<style scoped>
  input {
    background: #f5f5f5;
    border-radius: 8px;
    border: 1px solid #2C2C2D;
    padding: 12px;
    height: 43px;
    display: block;
    width: 608px;
    font-size: 16px;
  }

  input:focus {
    outline: none;
  }
</style>
