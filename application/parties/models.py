from application import db
from application.models import Base

class Party(Base):

    name = db.Column(db.String(144), nullable=False)
    business_id = db.Column(db.String(9))
    address_street = db.Column(db.String(144))
    address_postalcode = db.Column(db.String(5))
    address_city = db.Column(db.String(50))
    bankrupt = db.Column(db.Boolean, nullable=False)

    def __init__(self, name):
        self.name = name
        self.bankrupt = False