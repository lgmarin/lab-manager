from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from lab_manager.models import User

class Registration(FlaskForm):

    courses = ['None','Mechanical Engineering', "Electrical Engineering", "Computer Science"]

    email        = StringField('Email Address', validators=[Length(min=6, max=35), DataRequired(), Email()])
    name         = StringField('Name', validators=[DataRequired(), Length(min=10, max=30)])
    grr          = IntegerField('GRR', validators=[DataRequired()])
    project      = SelectField('Project', validators=[DataRequired()], coerce=int)
    course       = SelectField('Course', validators=[DataRequired(), Length(min=8, max=50)], choices=courses)
    password     = PasswordField('Password', validators=[Length(min=6, max=20), DataRequired()])
    password2    = PasswordField('Confirm Password', validators=[EqualTo('password'), DataRequired()])
    submit       = SubmitField('Submit')

    def validate_email(form, email):
        test = User.query.filter_by(email=form.email.data).first()
        if test:
            raise ValidationError('Your email is already in use!')

    def validate_grr(form, grr):
        test = User.query.filter_by(grr=form.grr.data).first()
        if test:
            raise ValidationError('Your GRR is already in use!')

class Login(FlaskForm):
    email        = StringField('Email Address', validators=[Length(min=6, max=35), DataRequired(), Email()])
    password     = PasswordField('Password', validators=[Length(min=6, max=20), DataRequired()])
    submit       = SubmitField('Login')

class ChangePassword(FlaskForm):
    current_password    = PasswordField('Current Password', validators=[Length(min=6, max=20), DataRequired()])
    password            = PasswordField('New Password', validators=[Length(min=6, max=20), DataRequired()])
    password2           = PasswordField('Confirm your New Password', validators=[EqualTo('password'), DataRequired()])
    submit              = SubmitField('Change Password')

    def validate_current_password(form, current_password):
        test = User.query.filter_by(id=current_user.id).first()
        if not test.check_password(form.current_password.data):
            raise ValidationError('You not entered your current value password!')

    def validate_password(form, password):
        test = User.query.filter_by(id=current_user.id).first()
        if test.check_password(form.current_password.data) == form.password.data:
            raise ValidationError('Your new password should be different from your current password!')
