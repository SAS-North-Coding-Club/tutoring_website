const Joi = require('joi')

module.exports = {
  register (req, res, next) {
    const schema = Joi.object({
      username: Joi.string().min(6).max(32).required().messages({
        'any.required': '{#label} is required.',
        'string.empty': '{#label} is required.',
        'string.min': '{#label} must be at least {#limit} characters.',
        'string.max': '{#label} must be no greater than {#limit} characters.'
      }),
      email: Joi.string().email().required().messages({
        'any.required': '{#label} is required.',
        'string.empty': '{#label} is required.',
        'string.email': '{#value} is not a valid email.'
      }),
      password: Joi.string().min(6).max(32).required().regex(
        new RegExp('^[a-zA-Z0-9]{6,32}$') //eslint-disable-line
      ).messages({
        'any.required': '{#label} is required.',
        'string.empty': '{#label} is required.',
        'string.min': '{#label} must be at least {#limit} characters.',
        'string.max': '{#label} must be no greater than {#limit} characters.',
        'string.pattern.base': '{#label} with value "{#value}" failed to match the required pattern: a-z, A-Z, 0-9.'
      }),
      confirm_password: Joi.string().valid(Joi.ref('password')).required().messages({
        'any.required': '{#label} is required.',
        'string.empty': '{#label} is required.',
        'any.only': '{#label} does not match "password"'
      })
    }).options({ abortEarly: false })

    const { error } = schema.validate(req.body) //eslint-disable-line

    if (error) {
      res.status(400).send({ errors: (error.details || []).map(er => { return { label: er.path[0], message: er.message } }) })
    } else {
      next()
    }
  }
}
