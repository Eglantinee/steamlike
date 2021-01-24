<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-sm-auto sidebar">
        <ul>
          <li><a>First</a></li>
          <li><a>First</a></li>
          <li><a>First</a></li>
          <li><a>First</a></li>
        </ul>
      </div>
      <div class="col list-view">
        <div class="single-book">
          <img src="">
          <p>Title</p>
          <p>price</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Main"
}
</script>

<style scoped>
.container-fluid {
  padding: 0;
}

.sidebar {
  height: 100%;
  width: 200px;
  position: inherit;
  z-index: 1;
  top: 0;
  left: 0;
  background-color: whitesmoke;
  overflow-x: hidden;
  padding-top: 20px;
  padding-bottom: 20px;
}

.sidebar ul {
  list-style-type: none;
  margin: 0;
  overflow: hidden;
  padding-left: 50px;
}

.sidebar li {
  padding-top: 20px;
}

.list-view {
  padding-top: 1px;
  padding-left: 50px;
  background-color: floralwhite;
}
</style>