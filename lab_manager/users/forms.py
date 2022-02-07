from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class Registration(FlaskForm):
    username     = StringField('Username', validators=[Length(min=4, max=25), DataRequired()])
    email        = StringField('Email Address', validators=[Length(min=6, max=35), DataRequired(), Email()])
    name         = StringField('Name', validators=[DataRequired(), Length(min=10, max=30)])
    project      = StringField('Project', validators=[DataRequired()])
    password     = PasswordField('Password', validators=[Length(min=6, max=20), DataRequired()])
    password2    = PasswordField('Confirm Password', validators=[EqualTo(password), DataRequired()])
    submit       = SubmitField('Submit')

class Login(FlaskForm):
    email        = StringField('Email Address', validators=[Length(min=6, max=35), DataRequired(), Email()])
    password     = PasswordField('Password', validators=[Length(min=6, max=20), DataRequired()])
    submit       = SubmitField('Login')