<template>
  <div>
    <div v-for="text in header" class="grid-item-header">{{ text }}</div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      header: ['№', 'Name', 'Type', 'Mass(kg)', 'Radius(km)', 'Density(g/cm^3)', 'Temperature(K)']
    }
  }
}
</script>

<style>
.grid-item-header{
  display: flex;
  align-items: center;
  justify-content: center;
  border-left: 1px solid #fff;
  border-bottom: 1px solid #fff;
  border-top: 1px solid #fff;
  font-size: 18px;
  font-weight: 700;
  color: #fff;
}
.grid-item-header:last-child{
  border-right: 1px solid #fff;
}
</style>
