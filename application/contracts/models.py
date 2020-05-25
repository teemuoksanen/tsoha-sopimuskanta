from application import db
from application.models import Base

class Contract(Base):

    name = db.Column(db.String(144), nullable=False)
    date_signed = db.Column(db.Date)
    date_entry = db.Column(db.Date)
    date_expiry = db.Column(db.Date)
    value = db.Column(db.Numeric)
    notes = db.Column(db.String(250))

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name):
        self.name = name