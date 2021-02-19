<template>
<!--  <div class="container-fluid editContainer">-->
<!--    <div class="row row-mov">-->
  <div><p> This is content {{id}} </p></div>

<!--      <div class="col-2 sidebar">-->
<!--        <template v-for="genre in genres">-->
<!--          <div>-->
<!--            &lt;!&ndash;suppress HtmlFormInputWithoutLabel &ndash;&gt;-->
<!--            <input type="checkbox" :id=genre.genre_name :value=genre.genre_name v-model="filter">-->
<!--            <label :for=genre.genre_name style="padding-left: 10px">{{ genre.genre_name }}</label>-->
<!--          </div>-->
<!--        </template>-->
<!--        <input type="button" value="Submit-button" v-on:click="filterBook">-->
<!--        <div>-->
<!--          <p>{{ filter }}</p>-->
<!--        </div>-->
<!--      </div>-->
<!--      <div class="col-10 list-view">-->
<!--        <div class="row">-->
<!--&lt;!&ndash;          <template v-for="book in books">&ndash;&gt;-->
<!--            <div class="col-3">-->
<!--              <p>A new text {{ id }}</p>-->
<!--&lt;!&ndash;              <img v-bind:src="book.images" alt="template" width="200" height="200">&ndash;&gt;-->
<!--&lt;!&ndash;              <p> {{ book.price }}</p>&ndash;&gt;-->
<!--            </div>-->
<!--&lt;!&ndash;          </template>&ndash;&gt;-->
<!--        </div>-->
<!--      </div>-->
<!--    </div>-->
<!--  </div>-->
</template>

<script>
import axios from "axios";
import qs from "qs"

export default {
  name: "single",
  props: {
    id: Number
  },
  data() {
    return {
      filter: [],
      book: null,
      genres: null
    }
    },
    created() {
      console.log(this.id)
      // }
      axios.get('http://localhost:8000/book/' + this.id + "/").then(response => {
            this.book = response.data;
            console.log(response.data)
          }
      )
    }

}
//     axios.get('http://localhost:8000/genre/').then(response => {
//           this.genres = response.data
//         }
//     )
//   },
//   methods: {
//     filterBook: function () {
//       axios.get('http://localhost:8000/book/', {
//         params: {filter: this.filter}, paramsSerializer: params => {
//           return qs.stringify(params, {arrayFormat: "comma"})
//         }
//       }).then(response => {
//         this.books = response.data;
//       })
//     },
//     log(checkboxEvent) {
//       console.log(checkboxEvent)
//     }
//   }
// }

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
</style>