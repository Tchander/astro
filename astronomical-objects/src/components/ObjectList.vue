<template>
  <div class="container">
    <header-item class="grid-container"/>
    <object-item
        class="grid-container"
        v-for="(object, i) of objects" :key="object.id"
        v-bind:object="object"
        v-bind:index="i"
    />
  </div>
</template>

<script>
import ObjectItem from '@/components/ObjectItem'
import HeaderItem from '@/components/HeaderItem'

export default {
  props: ['objects'],
  components: {
    ObjectItem,
    HeaderItem
  }
}
</script>

<style>
.grid-container {
  width: 100%;
  display: grid;
  grid-template-columns: 40px 16.6% 160px repeat(4, 16.6%);
  grid-template-rows: 40px;
  text-align: left;
}

.container {
  width: 100%;
  max-width: 1200px;
  margin: 40px auto;
  background: rgba(42, 29, 56, 0.2);
}
</style>
