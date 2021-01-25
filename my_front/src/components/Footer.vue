<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-12 column">
      <div class="footer-image">
        <h1>Footer</h1>
      </div>
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