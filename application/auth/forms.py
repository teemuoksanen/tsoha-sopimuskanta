from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, HiddenField, SelectField, validators, ValidationError
from application.auth.models import User
  
class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus")
    password = PasswordField("Salasana")
    nextpage = HiddenField()
  
    class Meta:
        csrf = False
  
class UserForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=1, max=144, message="Nimen on oltava %(min)d-%(max)d merkkiä pitkä.")], description="Anna käyttäjän oikea nimi.", render_kw={"placeholder": "Etunimi Sukunimi"})
    username = StringField("Käyttäjätunnus", [validators.Length(min=1, max=144, message="Käyttäjätunnuksen on oltava %(min)d-%(max)d merkkiä pitkä.")], description="Anna käyttäjälle käyttäjätunnus.", render_kw={"placeholder": "tunnus"})
    password = PasswordField("Salasana", [validators.Length(min=8, max=144, message="Salasanan on oltava %(min)d-%(max)d merkkiä pitkä."), validators.EqualTo("confirmPassword", message="Salasanojen on täsmättävä keskenään.")], description="Anna käyttäjälle 8-144 merkkiä pitkä salasana.")
    confirmPassword = PasswordField("Salasana uudelleen", description="Anna käyttäjän salasana uudelleen.")
    user_role = SelectField("Käyttäjätyyppi", choices=[('NORMAL', 'Käyttäjä'), ('ADMIN', 'Ylläpitäjä')], description="Valitse käyttäjän käyttäjätyyppi.")

    def validate_username(form, username):
        username_exists = User.query.filter_by(username=form.username.data).first()
        if username_exists:
            raise ValidationError("Käyttäjätunnus '" + form.username.data + "' on jo käytössä, valitse toinen käyttäjätunnus.")
  
    class Meta:
        csrf = False
  
class UserEditForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=1, max=144, message="Nimen on oltava %(min)d-%(max)d merkkiä pitkä.")], description="Anna käyttäjän oikea nimi.")
    username = StringField("Käyttäjätunnus", [validators.Length(min=1, max=144, message="Käyttäjätunnuksen on oltava %(min)d-%(max)d merkkiä pitkä.")], description="Anna käyttäjälle käyttäjätunnus.")
    user_role = SelectField("Käyttäjätyyppi", choices=[('NORMAL', 'Käyttäjä'), ('ADMIN', 'Ylläpitäjä')], description="Valitse käyttäjän käyttäjätyyppi.")
    current_username = HiddenField()

    def validate_username(form, username):
        username_exists = User.query.filter_by(username=form.username.data).first()
        if (form.username.data != form.current_username.data) and username_exists:
            raise ValidationError("Käyttäjätunnus '" + form.username.data + "' on jo käytössä, valitse toinen käyttäjätunnus.")
  
    class Meta:
        csrf = False
  
class UserOwnSettingsForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=1, max=144, message="Nimen on oltava %(min)d-%(max)d merkkiä pitkä.")], description="Anna käyttäjän oikea nimi.")
    username = StringField("Käyttäjätunnus", [validators.Length(min=1, max=144, message="Käyttäjätunnuksen on oltava %(min)d-%(max)d merkkiä pitkä.")], description="Anna käyttäjälle käyttäjätunnus.")
    current_username = HiddenField()

    def validate_username(form, username):
        username_exists = User.query.filter_by(username=form.username.data).first()
        if (form.username.data != form.current_username.data) and username_exists:
            raise ValidationError("Käyttäjätunnus '" + form.username.data + "' on jo käytössä, valitse toinen käyttäjätunnus.")
  
    class Meta:
        csrf = False
  
class PasswordEditForm(FlaskForm):
    password = PasswordField("Salasana", [validators.Length(min=8, max=144, message="Salasanan on oltava %(min)d-%(max)d merkkiä pitkä."), validators.EqualTo("confirmPassword", message="Salasanojen on täsmättävä keskenään.")], description="Anna käyttäjälle 8-144 merkkiä pitkä salasana.")
    confirmPassword = PasswordField("Salasana uudelleen", description="Anna käyttäjän salasana uudelleen.")
  
    class Meta:
        csrf = False