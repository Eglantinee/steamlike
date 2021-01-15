<template>
  <Top />
  <router-view/>
</template>

<style>
  @import "./assets/css/bootstrap.css";
  @import "./assets/css/font-awesome.css";
  @import "./assets/css/style.css";
</style>

<script>
import Top from './components/Top'
export default {
  components: { Top }
}
</script>
