from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class PartyForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=2, max=144, message="Nimen on oltava %(min)d-%(max)d merkkiä pitkä")])
    businessid = StringField("Y-tunnus", [validators.Length(min=9, max=9, message="Y-tunnuksen on oltava tasan 9 merkkiä pitkä")])
    address_street = StringField("Lähiosoite", [validators.Length(min=2, max=144, message="Lähiosoitteen on oltava %(min)d-%(max)d merkkiä pitkä")])
    address_postalcode = StringField("Postinumero", [validators.Length(min=5, max=5, message="Postinumeron on oltava tasan 5 merkkiä pitkä")])
    address_city = StringField("Kaupunki", [validators.Length(min=2, max=50, message="Kaupungin on oltava %(min)d-%(max)d merkkiä pitkä")])
    bankrupt = BooleanField("Konkurssissa")
 
    class Meta:
        csrf = False
