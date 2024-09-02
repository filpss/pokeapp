<script setup>
  const props = defineProps({
    backgroundColor: {
      type: String,
      default: '#ffffff',
    },
    textColor: {
      type: String,
      default: '#18181A',
    }
  });
</script>

<template>
  <button :style="{ backgroundColor: props.backgroundColor, color: props.textColor }" class="CustomButtonComponent">
    <slot></slot>
  </button>
</template>

<style scoped>
  .CustomButtonComponent {
    height: 43px;
    padding: 12px 32px 12px 32px;
    border-radius: 8px;
    border: none;
    cursor: pointer;
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-size: 16px;
    line-height: 19.36px;
    width: 100%;
    letter-spacing: .4px;
  }
</style>