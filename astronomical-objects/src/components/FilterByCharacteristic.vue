<template>
  <div class="ao-select-wrapper">
    <select class="select" v-model="filterByCharacteristic" @click="$emit('filter-by-characteristics', filterByCharacteristic)">
      <option value="" disabled selected hidden>Characteristics</option>
      <option v-for="op of options" :value="op.value">{{ op.text }}</option>
    </select>
  </div>
</template>

<script>
export default {
  data() {
    return {
      filterByCharacteristic: '',
      options: [
        {value: 'radius', text: 'Radius'},
        {value: 'mass', text: 'Mass'},
        {value: 'density', text: 'Density'},
        {value: 'temperature', text: 'Temperature'}
      ]
    }
  }
}
</script>

