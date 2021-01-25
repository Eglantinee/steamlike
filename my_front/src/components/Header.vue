<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-12 column">
        <div class="main-banner">
          <h1 class="my-logo">Steamlike</h1>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-12 column">
        <div class="navbar">
          <ul>
            <li class="first-item"><a href="#">Link</a></li>
            <li><a href="#">Link</a></li>
            <li><a href="#">Link</a></li>
            <li><a href="#" class="right">Link</a></li>
          </ul>
          <form class="search-form" action="">
            <input type="text" placeholder="Search..." name="search">
            <button type="submit"><i class="fa fa-search"></i></button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Header"
}
</script>

<style scoped>


.main-banner {
  background-image: url("../assets/images/baner.jpg");
  background-size: 100% 100%;
  height: 300px;
  color: white;
  font-style: italic;
}

.main-banner h1 {
  padding: 50px;
}

.navbar ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
  overflow: hidden;
  background-color: white;
}

.navbar li {
  float: left;
}

.navbar li.first-item {
  padding-left: 200px;
}

.navbar a {
  display: block;
  color: black;
  padding-top: 16px;
  padding-left: 50px;
  text-decoration: none;
}

form.search-form {
  padding-top: 16px;
  padding-right: 100px;
  text-decoration: none;
}

form.search-form input[type=text] {
  float: left;
  width: 200px;
  height: 1.5rem;
  background: #919aa0;
  border-radius: 15px;
  color: black;
  box-shadow: none;
  border: none;
  padding-left: 10px;
}

form.search-form button {
  float: left;
  width: 1.5rem;
  height: 1.5rem;
  background-image: url("../assets/images/search1.png");
  background-size: 100% 100%;
  box-shadow: none;
  border: none;
  margin-left: 10px;
}
</style>