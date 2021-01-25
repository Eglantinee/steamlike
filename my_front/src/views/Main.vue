<template>
  <div class="container-fluid editContainer">
    <div class="row row-mov">
      <div class="col-2 sidebar">
        <ul>
          <li><a>First</a></li>
          <li><a>First</a></li>
          <li><a>First</a></li>
          <li><a>First</a></li>
        </ul>
      </div>
      <div class="col-10 list-view">
        <div class="row">
          <template v-for="book in books">
            <div class="col-3">
              <p>{{ book.title }}</p>
              <img v-bind:src="book.images" alt="template" width="200" height="200">
              <p> {{ book.price }}</p>
            </div>
          </template>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Main",
  data() {
    return {
      books: null
    }
  },
  created() {
    console.log('AAAAAAAAAAAA')
    axios.get('http://localhost:8000/book/').then(response => {
          this.books = response.data;
          console.log(response.data[0].images)
        }
    )
  }
}

</script>

<style scoped>


.sidebar {
  height: 100%;
  width: 200px;
  position: inherit;
  z-index: 1;
  top: 0;
  left: 20px;
  background-color: whitesmoke;
  overflow-x: hidden;
  padding-top: 20px;
  padding-bottom: 20px;
  padding-left: 20px;
  border: 4px double black;
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
.row-mov {
  padding: inherit;
}
.editContainer{
  min-height: 350px;
  padding-top: 5px;
}
</style>