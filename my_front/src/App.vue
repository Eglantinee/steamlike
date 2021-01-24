<template style="height: 100%">
  <Header/>
  <router-view/>
  <Footer />
</template>

<style>
html, body {
  height: 100%;
  min-height: 100%;
}
</style>
<script>
import Header from "@/components/Header";
import Footer from "@/components/Footer";

export default {
  components: {Footer, Header}
}
</script>