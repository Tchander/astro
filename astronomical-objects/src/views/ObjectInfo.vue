<template>
  <div>
    <router-link to="/">Home</router-link>
    <router-link to="/all-objects">All Objects</router-link>
    <hr>
    <h3>{{ objectData.name }}</h3>
    <div class="info-list">
      <div class="info-item" v-for="key of keys">{{ key }}: {{ objectData[key] }}</div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      keys: []
    }
  },
  props: {
    objectData: {
      type: Object,
      required: true,
      default: () => ({})
    }
  },
  created() {
    this.keys = Object.keys(this.objectData)
  }
}
</script>

<style>
.info-list {
  display: flex;
  flex-wrap: wrap;
  width: 100%;
  max-width: 1000px;
  align-items: center;
  justify-content: space-between;
  margin: 20px auto;
}
</style>
