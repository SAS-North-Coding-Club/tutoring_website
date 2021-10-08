<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt="Logo"
          class="shrink mr-2"
          contain
          src="@/assets/logo.png"
          transition="scale-transition"
          width="40"
        />

        <v-toolbar-title
          @click="$router.push('/')"
          style="cursor:pointer"
        >
          Tutoring Website
        </v-toolbar-title>

      </div>

      <v-tabs
        v-model="tab"
        right
        dark
      >
        <v-tabs-slider color="black"></v-tabs-slider>

        <v-tab
          v-for="item in items"
          :key="item.name"
          :to="item.link"
        >
          {{ item.name }}
        </v-tab>
      </v-tabs>
    </v-app-bar>

    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    tab: null,
    items: [
      {
        name: 'Home',
        link: '/'
      },
      {
        name: 'About',
        link: '/about'
      },
      {
        name: 'Register',
        link: '/register'
      }
    ]
  }),
};
</script>
