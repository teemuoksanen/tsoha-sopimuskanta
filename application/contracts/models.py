from application import db
from application.models import Base

contractparties = db.Table('ContractParty',
    db.Column('contract_id', db.Integer, db.ForeignKey('contract.id'), primary_key=True),
    db.Column('party_id', db.Integer, db.ForeignKey('party.id'), primary_key=True)
)

class Contract(Base):

    name = db.Column(db.String(144), nullable=False)
    date_signed = db.Column(db.Date)
    date_entry = db.Column(db.Date)
    date_expiry = db.Column(db.Date)
    value = db.Column(db.Float)
    notes = db.Column(db.String(250))

    parties = db.relationship('Party', secondary=contractparties, lazy='subquery',
        backref=db.backref('contracts', lazy='dynamic'))

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name):
        self.name = name