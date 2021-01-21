<template>
  <Top />
  <router-view/>
  <Bottom />
</template>

<style>
  @import "./assets/css/bootstrap.css";
  @import "./assets/css/font-awesome.css";
  @import "./assets/css/style.css";
</style>

<script>
import Top from './components/Top'
import Bottom from "@/components/Bottom";
export default {
  components: {Bottom, Top }
}
</script>
