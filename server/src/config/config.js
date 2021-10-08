module.exports = {
  port: process.env.PORT || 8081,
  db: {
    database: process.env.DB_NAME || 'tutoring_website_test',
    user: process.env.DB_USER || 'root',
    password: process.env.DB_PASS || 'pass',
    options: {
      dialect: process.env.DIALECT || 'mysql',
      host: process.env.HOST || 'localhost'
    }
  }
}
