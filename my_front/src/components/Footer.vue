<template>
  <div class="header">
    <div class="footer-image">
      <h1 class="my-logo">Footer</h1>
    </div>
  </div>
</template>

<script>
export default {
  name: "Footer"
}
</script>

<style scoped>
.footer-image {
  background-image: url("../assets/images/baner.jpg");
  height: 300px;
  color: white;
  font-style: italic;
}

.my-logo {
  padding-left: 50%;
  padding-top: 150px;
}
</style>