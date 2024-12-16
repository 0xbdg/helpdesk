from app import *
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, ValidationError

class LoginForm(FlaskForm):
    username= StringField(validators=[InputRequired(), Length(min=1, max=255)], render_kw={"class":"form-control", "placeholder":"Enter username"})
    password = PasswordField(validators=[InputRequired(), Length(min=1, max=255)], render_kw={"class":"form-control", "placeholder":"Enter password"})

    submit = SubmitField("Log in", render_kw={"class":"btn btn-lg btn-primary"})