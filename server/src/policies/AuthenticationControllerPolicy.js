const Joi = require('joi')

module.exports = {
  register (req, res, next) {
    const schema = Joi.object({
      email: Joi.string().email().messages({
        'string.email': '"{#value}" is not a valid email.'
      }),
      password: Joi.string().min(8).max(32).regex(
        new RegExp('^[a-zA-Z0-9]$') //eslint-disable-line
      ).messages({
        'string.min': '"password" must be at least 8 characters.',
        'string.max': '"password" must be no greater than 32 characters.',
        'string.pattern.base': '"password" with value "{#value}" failed to match the required pattern: a-z, A-Z, 0-9'
      })
    })

    const { error, value } = schema.validate(req.body) //eslint-disable-line

    if (error) {
      res.status(400).send({
        error: error.details
      })
    } else {
      next()
    }
  }
}
