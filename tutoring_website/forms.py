from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from tutoring_website.models import Tutor


class RequestForm(FlaskForm):
    first_name = StringField("First Name",
                             validators=[DataRequired()])
    last_name = StringField("Last Name",
                            validators=[DataRequired()])
    email = StringField("Email",
                        validators=[DataRequired(), Email()])
    submit = SubmitField("Request")


class RegisterForm(FlaskForm):
    first_name = StringField("First Name",
                             validators=[DataRequired(), Length(min=2, max=25)])
    last_name = StringField("Last Name",
                            validators=[DataRequired(), Length(min=2, max=25)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        tutor = Tutor.query.filter_by(username=username.data).first()
        if tutor:
            raise ValidationError(
                'That username is taken. Please choose a difference one.')

    def validate_email(self, email):
        tutor = Tutor.query.filter_by(email=email.data).first()
        if tutor:
            raise ValidationError(
                'That email is taken. Please choose a difference one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')
