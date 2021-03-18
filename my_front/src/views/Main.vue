<template>
  <div class="container-fluid editContainer">
    <div class="row row-mov">
      <div class="col-2 sidebar">
        <template v-for="genre in genres">
          <div>
            <label>
              <input type="checkbox" :id=genre.genre_name :value=genre.genre_name v-model="filter">
            </label>
            <label :for=genre.genre_name style="padding-left: 10px">{{ genre.genre_name }}</label>
          </div>
        </template>
        <input type="button" value="Submit-button" v-on:click="filterBook">
        <div>
          <p>{{ filter }}</p>
        </div>
      </div>
      <div class="col-10 list-view">
        <div class="row">
          <template v-for="book in books">
            <div class="col-auto"
                 style="margin-top: 10px; margin-left: 10px; background-color: white; width: 250px; height: 280px">
              <div class="book_image">
                <img v-bind:src="book.images" alt="template" width="200" height="200">
              </div>
              <div class="book_title">
                <router-link :to="{name:'single', params: { id: book.book_id, book:book }}">{{ book.title }}
                </router-link>
              </div>
              <div class="book_author">
                <template v-for="author in book.authors">
                  <pre>{{ author.first_name}} {{ author.last_name }}</pre>
                </template>
              </div>
            </div>
          </template>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import qs from "qs"
import router from "@/router";

export default {
  name: "Main",
  data() {
    return {
      filter: [],
      books: null,
      genres: null
    }
  },
  created() {
    axios.get('http://localhost:8000/book/').then(response => {
          this.books = response.data;
          console.log(this.books)
          // console.log(response.data[0].images)
        }
    )
    axios.get('http://localhost:8000/genre/').then(response => {
          this.genres = response.data
        }
    )
  },
  methods: {
    filterBook: function () {
      axios.get('http://localhost:8000/book/', {
        params: {filter: this.filter}, paramsSerializer: params => {
          return qs.stringify(params, {arrayFormat: "comma"})
        }
      }).then(response => {
        this.books = response.data;
      })
    },
    singlePage: function (id) {
      return router.push({name: 'Single', params: {id}})
    }
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

.editContainer {
  min-height: 350px;
  padding-top: 5px;
}

.book_title {
  padding-top: 10px;
  font-size: 16px;
  text-align: center;
  color: black;
}

.book_image {
  padding-top: 10px;
  text-align: center;
}
.book_author {
  padding-top: 10px;
  text-align: center;
  color: navy;
  font-size: 14px;
}
</style>