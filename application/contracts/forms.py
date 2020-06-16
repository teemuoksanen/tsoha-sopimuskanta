from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, validators
from wtforms.fields.html5 import DateField

class ContractForm(FlaskForm):
    name = StringField("Sopimuksen nimi", [validators.Length(min=2, max=144, message="Sopimuksen nimen on oltava %(min)d-%(max)d merkkiä pitkä")], description="Anna sopimuksen otsikko tai muu kuvaava nimi.")
    date_signed = DateField("Allekirjoitettu (pvm)", [validators.DataRequired(message="Allekirjoituspäivä on pakollinen.")], description="Valitse päivä nuolesta aukeavasta kalenterista.")
    date_entry = DateField("Tulee voimaan (pvm)", [validators.DataRequired(message="Voimaantulopäivä on pakollinen.")], description="Valitse päivä nuolesta aukeavasta kalenterista.")
    date_expiry = DateField("Umpeutuu (pvm)", [validators.Optional(strip_whitespace=True)], description="Valitse päivä nuolesta aukeavasta kalenterista.")
    account_id = SelectField("Käyttäjä", description="Valitse käyttäjä valikosta.", coerce=int)
  
    class Meta:
        csrf = False

class ContractPartyForm(FlaskForm):
    parties = SelectField("Osapuoli", [validators.required(message="Valitse lisättävä osapuoli")], description="Valitse osapuoli valikosta. Jos osapuolta ei ole valikossa, luo se ensin painamalla 'Luo uusi osapuoli'.", coerce=int)
  
    class Meta:
        csrf = False

class ContractSearch(FlaskForm):
    search = StringField("Hakusana:", [validators.Length(max=144, message="Hakusana voi olla enintään %(max)d merkkiä pitkä.")], description="Haku kohdistuu sopimuksen nimeen. Voit jättää hakusanan tyhjäksi, jos haluat listata kaikki sopimukset.")	
    onlyOwn = BooleanField("Näytä vain omat sopimukset")
    onlyValid = BooleanField("Näytä vain voimassa olevat sopimukset")

    class Meta:
        csrf = False
