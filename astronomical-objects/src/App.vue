<template>
  <div id="app">
    <h1>Astronomical Database</h1>

    <router-view />
  </div>
</template>

<script>

export default {
  name: 'App',
}
</script>

<style>
body {
  margin: 0;
}

body::before {
  content: '';
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url("assets/images/background/space-background-for-astronomical-database-dark.png");
  background-repeat: no-repeat;
  background-size: cover;
  z-index: -1;
}

h1, h2, h3, h4, h5, h6 {
  margin: 0;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #fff;
  margin-top: 60px;
}
.ao-select-wrapper {
  position: relative;
  display: inline;
}
.ao-select-wrapper:before {
  content: '';
  display: inline-block;
  position: absolute;
  right: 30px;
  top: 5px;
  width: 0;
  height: 0;
  border-left: 5px solid transparent;
  border-right: 5px solid transparent;

  border-top: 5px solid red;
}
</style>
