<template>
  <v-form ref="form">
    <v-container>
      <h1>This is an register page</h1>
      <v-row>
        <v-col
          cols="12"
          md="4"
        >
          <v-text-field type="username" name="username" v-model="username" placeholder="username" 
            :rules="rules.username"
          />
        </v-col>

        <v-col
          cols="12"
          md="4"
        >
          <v-text-field type="email" name="email" v-model="email" placeholder="email" 
            :rules="rules.email"
          />
        </v-col>

        <v-col
        cols="12"
        md="4"
        >
          <v-text-field type="password" name="password" v-model="password" placeholder="password" 
            :rules="rules.password"
          />
        </v-col>

        <v-col
        cols="12"
        md="4"
        >
          <v-text-field type="confirm_password" name="confirm_password" v-model="confirm_password" placeholder="confirm_password" 
            :rules="rules.confirm_password"
          />
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
      errors: {
        username: '',
        email: '',
        password: '',
        confirm_password: ''
      },
      rules: {
        username: [() => this.errors.username === '' || this.errors.username],
        email: [() => this.errors.email === '' || this.errors.email],
        password: [() => this.errors.password === '' || this.errors.password],
        confirm_password: [() => this.errors.confirm_password === '' || this.errors.confirm_password]
      }
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

      this.$refs.form.validate()
    }
  }
}
</script>

<style scoped>
.error {
  background-color: red;
}
</style>
