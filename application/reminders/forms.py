from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, validators
from wtforms.fields.html5 import DateField

class ReminderForm(FlaskForm):
    note = StringField("Muistutus", [validators.Length(min=2, max=250, message="Muistutuksen on oltava %(min)d-%(max)d merkkiä pitkä")], description="Anna muistutuksen sisältö.")
    date_remind = DateField("Muistutuspäivä", [validators.DataRequired(message="Muistutuspäivä on pakollinen.")], description="Valitse päivä nuolesta aukeavasta kalenterista.")
    contract_id = SelectField("Sopimus", [validators.required(message="Valitse sopimus, johon muistutus liittyy.")], description="Valitse sopimus valikosta.", coerce=int)
    account_id = SelectField("Käyttäjä", description="Valitse käyttäjä valikosta.", coerce=int)
  
    class Meta:
        csrf = False