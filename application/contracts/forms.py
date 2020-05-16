from flask_wtf import FlaskForm
from wtforms import StringField, validators

class ContractForm(FlaskForm):
    name = StringField("Sopimuksen nimi", [validators.Length(min=2, max=144, message="Kentän on oltava %(min)d-%(max)d merkkiä pitkä")])
  
    class Meta:
        csrf = False
