from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, validators
from wtforms.fields.html5 import DateField

class ContractForm(FlaskForm):
    name = StringField("Sopimuksen nimi", [validators.Length(min=2, max=144, message="Sopimuksen nimen on oltava %(min)d-%(max)d merkkiä pitkä")], description="Anna sopimuksen otsikko tai muu kuvaava nimi.")
    date_signed = DateField("Allekirjoitettu (pvm)", description="Valitse päivä nuolesta aukeavasta kalenterista.")
    date_entry = DateField("Tulee voimaan (pvm)", description="Valitse päivä nuolesta aukeavasta kalenterista.")
    date_expiry = DateField("Umpeutuu (pvm)", [validators.Optional(strip_whitespace=True)], description="Valitse päivä nuolesta aukeavasta kalenterista.")
  
    class Meta:
        csrf = False

class ContractPartyForm(FlaskForm):
    parties = SelectField("Osapuoli", [validators.required(message="Valitse lisättävä osapuoli")], description="Valitse osapuoli valikosta. Jos osapuolta ei ole valikossa, luo se ensin painamalla 'Luo uusi osapuoli'.", coerce=int)
  
    class Meta:
        csrf = False