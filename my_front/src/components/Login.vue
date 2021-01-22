<template>
  <!--This is part where we store html code for page. It is static at all-->
  <div class="container">
    <button type="button" class="btn btn-primary">{{ msg }}</button>
  </div>
</template>

<script>
import axios from 'axios'
// --This is part of   JS   logic. -->
export default {
  name: "Login",
  data() {
    return {
      msg: 'Hello!',
    };
  },

  methods: {
    getMessage() {
      const path = 'http://localhost:8000/login';
      axios.get(path)
          .then((res) => {
            this.msg = res.data;
          })
          .catch((error) => {
            // eslint-выключение следующей строки
            console.error(error);
          });
    },
  },
  created() {
    this.getMessage();
  },
}
</script>

<style scoped>
/*here we store our styles*/
</style>


<!--Then we gonna add this page into /router/index.js
  In main APP.vue it is connected into <router view/> -->
