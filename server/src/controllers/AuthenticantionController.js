const { User } = require('../models')
const jwt = require('jsonwebtoken')
const config = require('../config/config')

function jwtSignUser (user) { 
  const ONE_WEEK = 604800
  return jwt.sign(user, config.authentication.jwtSecret, {
    expiresIn: ONE_WEEK
  })
}

module.exports = {
  async register (req, res) {
    try {
      const user = await User.create(req.body)
      const userJson = user.toJSON()
      res.send({
        user: userJson,
        token: jwtSignUser(userJson)
      })
    } catch (err) {
      /** Catch any error
       *  Example: Email already exist
      */
      res.status(400).send({
        error: 'This email account is already in use.'
      })
    }
  },
  async login (req, res) {
    try {
      const { email, password } = req.body
      const user = await User.findOne({
        where: {
          email: email
        }
      })
      if (!user) {
        return res.status(403).send({
          error: 'Invalid login information.'
        })
      }

      const validPassword = user.comparePassword(password)
      if (!validPassword) {
        return res.status(403).send({
          error: 'Invalid login information.'
        })
      }

      res.send({
        user: user.toJSON()
      })
    } catch (err) {
      res.status(500).send({
        error: 'An error occurred during login.'
      })
    }
  }
}
