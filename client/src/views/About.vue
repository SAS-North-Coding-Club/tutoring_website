<template>
  <div class="about">
    <h1>This is an about page</h1>
    <home/>
  </div>
</template>

<script>
import Home from '@/views/Home'
export default {
  name: "About",

  components: {
    Home,
  }
}
</script>