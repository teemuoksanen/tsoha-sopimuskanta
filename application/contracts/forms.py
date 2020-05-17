from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms.fields.html5 import DateField

class ContractForm(FlaskForm):
    name = StringField("Sopimuksen nimi", [validators.Length(min=2, max=144, message="Sopimuksen nimen on oltava %(min)d-%(max)d merkkiä pitkä")])
    date_signed = DateField("Allekirjoitettu (pvm)")
    date_entry = DateField("Tulee voimaan (pvm)")
    date_expiry = DateField("Umpeutuu (pvm)", [validators.Optional(strip_whitespace=True)])
  
    class Meta:
        csrf = False
