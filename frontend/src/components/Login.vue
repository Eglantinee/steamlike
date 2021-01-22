<template>
  <!--This is part where we store html code for page. It is static at all-->
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
// --This is part of   JS   logic. -->
export default {
  name: "Login",
  data() {
    return {
      msg: 'Hello!',
    };
  },
}
</script>

<style scoped>
/*here we store our styles*/
</style>


<!--Then we gonna add this page into /router/index.js
  In main APP.vue it is connected into <router view/> -->
