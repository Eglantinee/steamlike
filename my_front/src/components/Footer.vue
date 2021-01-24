<template>
  <div class="container-fluid">
    <div class="footer-grid_section_w3layouts">
      <div class="footer-image">
        <h1 class="w3layouts-footer">Footer</h1>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Footer"
}
</script>

<style scoped>
.container-fluid {
  padding: 50px 0 0 0;
  /*position: absolute;*/
  /*bottom: 0;*/
}
.footer-image {
  background-image: url("../assets/images/baner.jpg");
  height: 300px;
  color: white;
  font-style: italic;
  background-size: 100% 100%;
}

.footer-image h1 {
  padding-left: 50%;
  padding-top: 150px;
}
</style>