<template>
  <div class="pagination">
    <button
      :disabled="currentPage === 1"
      @click="changePage(currentPage - 1)">
      &lt;
    </button>

    <button
      v-for="page in visiblePages"
      :key="page"
      @click="changePage(page)"
      :class="{ active: page === currentPage }"
      :disabled="page === '...'">
      {{ page }}
    </button>

    <button
      :disabled="currentPage === totalPages"
      @click="changePage(currentPage + 1)">
      &gt;
    </button>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";

const props = defineProps({
  totalItems: {
    type: Number,
    required: true,
  },
  itemsPerPage: {
    type: Number,
    default: 6,
  },
  currentPage: {
    type: Number,
    default: 1,
  },
  maxPagesToShow: {
    type: Number,
    default: 10,
  },
  maxLimit: {
    type: Number,
    default: 171
  }
});

const emit = defineEmits(['update:currentPage']);

const totalPages = computed(() => {
  return Math.min(Math.ceil(props.totalItems / props.itemsPerPage), props.maxLimit);
});

const visiblePages = computed(() => {
  const pages = [];
  const total = totalPages.value;
  const current = props.currentPage;

  pages.push(1);

  if (current > 3) {
    pages.push('...');
  }

  const startPage = Math.max(2, current - 2);
  const endPage = Math.min(total - 1, current + 2);

  for (let i = startPage; i <= endPage; i++) {
    pages.push(i);
  }

  if (current < total - 2) {
    pages.push('...');
  }

  if (total > 1) {
    pages.push(total);
  }

  return pages;
});

const changePage = (page) => {
  if (page !== '...' && page <= totalPages.value) {
    emit('update:currentPage', page);
  }
};
</script>

<style scoped>
.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: row;
}
button {
  height: 32px;
  width: 32px;
  margin: 0 5px;
  font-size: 14px;
  font-family: 'SF Pro Text', sans-serif;
  border-radius: 4px;
  border: 1px solid #DFE3E8;
}

button.active {
  font-weight: bold;
  color: #4200FF;
  border: 1px solid #4200FF;
}
button[disabled] {
  background: #919EAB;
  border: none;
  cursor: not-allowed;
  opacity: 0.6;
}
</style>
