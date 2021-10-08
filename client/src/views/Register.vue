<template>
  <v-form>
    <v-container>
      <h1>This is an register page</h1>
      <v-row>
        <v-col
          cols="12"
          md="4"
        >
          <v-text-field type="email" name="email" v-model="email" placeholder="email" />
        </v-col>

        <v-col
        cols="12"
        md="4"
        >
          <v-text-field type="password" name="password" v-model="password" placeholder="password" />
        </v-col>
      <div class="error" v-html="error" />
      <v-btn color="success" @click="register">Register</v-btn>
      </v-row>
    </v-container>
  </v-form>
</template>

<script>
import AuthenticationService from '@/services/AuthenticationService'
export default {
  name: "Register",

  data () {
    return {
      email: '',
      password: '',
      error: null
    }
  },

  methods: {
    async register () {
      try {
        await AuthenticationService.register({
          email: this.email,
          password: this.password
        })
        this.error = null
      } catch (error) {
        this.error = error.response.data.error
      }
    }
  }
}
</script>

<style scoped>
.error {
  color: red;
}
</style>
