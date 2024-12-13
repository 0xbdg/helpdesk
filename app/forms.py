from app import *
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, ValidationError

class LoginForm(FlaskForm):
    username= StringField(validators=[InputRequired(), Length(min=1, max=255)], render_kw={"class":"form-control"})
    password = PasswordField(validators=[InputRequired(), Length(min=1, max=255)])

    submit = SubmitField("Log in")

    def validate(self,username):
        pass