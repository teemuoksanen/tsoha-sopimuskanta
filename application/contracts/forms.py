from flask_wtf import FlaskForm
from wtforms import StringField, DateField, validators

class ContractForm(FlaskForm):
    name = StringField("Sopimuksen nimi", [validators.Length(min=2, max=144, message="Sopimuksen nimen on oltava %(min)d-%(max)d merkkiä pitkä")])
    date_signed = DateField("Allekirjoitettu (yyyy-mm-dd)")
    date_entry = DateField("Tulee voimaan (yyyy-mm-dd)")
    date_expiry = DateField("Umpeutuu (yyyy-mm-dd)")
  
    class Meta:
        csrf = False
