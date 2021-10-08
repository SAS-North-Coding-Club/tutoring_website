const fs = require('fs')
const Sequelize = require('sequelize')
const config = require('../config/config')
const db = {}

/*
Creating sequalize object with config settings
*/
const sequelize = new Sequelize(
  config.db.database,
  config.db.user,
  config.db.password,
  config.db.options
)

/*
  Reading through each file within the models dir
  (excluding index.js), import it through sequalize,
  and input it into the database
*/
fs.readdirSync(__dirname)
  .filter((file) => file !== 'index.js')
  .forEach((file) => {
    const model = require(`./${file}`)(sequelize, Sequelize.DataTypes)
    db[model.name] = model
  })

db.sequelize = sequelize
db.Sequelize = Sequelize

module.exports = db
