<template>
  <div v-bind="$attrs">
    <div class="grid-item">{{ index + 1 }}</div>
    <router-link :to="{ name: 'objectInfo', params: { id: object.id, objectData: object } }"
                 class="grid-item object-link">{{ object.name }}</router-link>
    <div v-for="key in keys" class="grid-item">{{ object[key] }}</div>
  </div>
</template>

<script>
export default {
  props: {
    object: {
      type: Object,
      required: true,
      default: () => ({})
    },
    index: Number
  },
  data() {
    return {
      keys: ['objectType', 'massKg', 'radiusKm', 'densityGCm3', 'temperatureK']
    }
  }
}
</script>

<style>
.object-link {
  text-decoration: none;
}
.object-link:hover {
  text-decoration: underline;
}
.grid-item{
  display: flex;
  align-items: center;
  justify-content: center;
  border-left: 1px solid #fff;
  border-bottom: 1px solid #fff;
  color: #fff;
}
.grid-item:last-child {
  border-right: 1px solid #fff;
}
</style>
