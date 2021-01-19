<template>
  <div id="app">
    <PersonList />
  </div>
</template>

<script>
import Plays from "./components/Plays";

export default {
  name: "App",
  components: {
    PersonList,
  },
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}