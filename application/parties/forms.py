from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class PartyForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=2, max=144, message="Nimen on oltava %(min)d-%(max)d merkkiä pitkä.")], description="Anna osapuolen nimi.", render_kw={"placeholder": "Esimerkki Oy"})
    business_id = StringField("Y-tunnus", [validators.Regexp("^\d{7}-\d$", message="Y-tunnuksen on oltava muotoa 1234567-8 (eli seitsemän numeroa, viiva ja yksi numero).")], description="Anna osapuolen yritystunnus oikeassa muodossa, esimerkiksi '1234567-8'.", render_kw={"placeholder": "1234567-8"})
    address_street = StringField("Lähiosoite", [validators.Length(min=2, max=144, message="Lähiosoitteen on oltava %(min)d-%(max)d merkkiä pitkä.")], description="Anna osapuolen lähiosoite.", render_kw={"placeholder": "Esimerkkikatu 1 A"})
    address_postalcode = StringField("Postinumero", [validators.Regexp("^\d{5}$", message="Postinumeron on oltava tasan 5 numeroa pitkä.")], description="Anna osapuolen postinumero muodossa '12345'. Postinumero on tasan 5 numeroa pitkä.", render_kw={"placeholder": "12345"})
    address_city = StringField("Kaupunki", [validators.Length(min=2, max=50, message="Kaupungin on oltava %(min)d-%(max)d merkkiä pitkä.")], description="Anna osapuolen kaupunki tai kunta.", render_kw={"placeholder": "Helsinki"})
 
    class Meta:
        csrf = False

class PartySearch(FlaskForm):
    search = StringField("Hakusana:", [validators.Length(max=144, message="Hakusana voi olla enintään %(max)d merkkiä pitkä.")], description="Haku kohdistuu osapuolen nimeen.")

    class Meta:
        csrf = False