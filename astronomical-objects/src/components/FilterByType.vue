<template>
  <div class="ao-select-wrapper">
    <select class="select" v-model="filterByType" @click="$emit('filter-by-type', filterByType)">
      <option v-for="op of options" :value="op.value">{{ op.text }}</option>
    </select>
  </div>
</template>

<script>
export default {
  data() {
    return {
      filterByType: 'all',
      options: [
        { value: 'all', text: 'All Objects' },
        { value: 'stars', text: 'Stars' },
        { value: 'planets', text: 'Planets' },
        { value: 'dwarf-planets', text: 'Dwarf Planets' },
        { value: 'satellites', text: 'Satellites' },
        { value: 'asteroids', text: 'Asteroids' }
      ]
    }
  }
}
</script>

