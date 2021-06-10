<template>
  <div class="container-fluid editContainer">
    <div class="row">
      <div class="col-3">
        <img v-bind:src="book.images" alt="template" class="image">
<!--        <p> This is content {{ book }} </p>-->
      </div>
      <div class="col-9">
        <p style="margin-top: 10px">{{book.title}}</p>
        <p>{{book.author[0].first_name}} {{book.author[0].last_name}}</p>
        <p>Year: {{book.year}}</p>
        <div class="col-8" style="padding: 0">
          <p>Annotation:</p>
          <p>{{book.annotation}}</p>
        </div>
      </div>
    </div>
  </div>
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
      book: null,
    }
  },
  created() {
    axios.get('http://localhost:8000/books/' + this.id + "/").then(response => {
          this.book = response.data
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
.image {
  width: 200px;
  height: 200px;
  margin: 20px
}
</style>