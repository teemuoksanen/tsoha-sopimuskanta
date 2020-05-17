from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus")
    password = PasswordField("Salasana")
  
    class Meta:
        csrf = False
  
class UserForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=1, max=144, message="Nimen on oltava %(min)d-%(max)d merkkiä pitkä")])
    username = StringField("Käyttäjätunnus", [validators.Length(min=1, max=144, message="Käyttäjätunnuksen on oltava %(min)d-%(max)d merkkiä pitkä")])
    password = PasswordField("Salasana", [validators.Length(min=8, max=144, message="Salasanan on oltava %(min)d-%(max)d merkkiä pitkä")])
  
    class Meta:
        csrf = False