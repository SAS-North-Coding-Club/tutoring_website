<template>
  <v-form>
    <v-container>
      <h1>This is an register page</h1>
      <v-row>
        <v-col
          cols="12"
          md="4"
        >
          <v-text-field type="username" name="username" v-model="username" placeholder="username" 
            :error-messages="errors.username"
          />
        </v-col>

        <v-col
          cols="12"
          md="4"
        >
          <v-text-field type="email" name="email" v-model="email" placeholder="email" 
            :error-messages="errors.email"
          />
        </v-col>

        <v-col
        cols="12"
        md="4"
        >
          <v-text-field type="password" name="password" v-model="password" placeholder="password" 
            :error-messages="errors.password"
          />
        </v-col>

        <v-col
        cols="12"
        md="4"
        >
          <v-text-field type="confirm_password" name="confirm_password" v-model="confirm_password" placeholder="confirm_password" 
            :error-messages="errors.confirm_password"
          />
          <div class="error" v-html="errors.confirm_password" />
        </v-col>
      <v-btn color="success" v-on:click.prevent="register">Register</v-btn>
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
      username: '',
      email: '',
      password: '',
      confirm_password: '',
      errors: {}
    }
  },

  methods: {
    async register () {
      try {
        await AuthenticationService.register({
          username: this.username,
          email: this.email,
          password: this.password,
          confirm_password: this.confirm_password
        })
        this.errors = null
      } catch (error) {
        const errors = error.response.data.errors
        for(let i = 0; i < errors.length; i++) {
          this.errors[errors[i].label] = errors[i].message
        }
      }
    }
  }
}
</script>

<style scoped>
.error {
  background-color: red;
}
</style>
