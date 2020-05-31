from application import db
from application.models import Base

from sqlalchemy.sql import text

contractparties = db.Table('contractparty',
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

    @staticmethod
    def parties_not_linked_to_contract(contract_id):
        stmt = text("SELECT Party.id, Party.name FROM Party"
                    " LEFT JOIN ContractParty ON (Party.id = ContractParty.party_id)"
                    " WHERE Party.id NOT IN"
                    " (SELECT party_id FROM ContractParty WHERE contract_id = :contract_id)"
                    " GROUP BY Party.id"
                    ).params(contract_id=contract_id)
        res = db.engine.execute(stmt)

        response = [(party.id, party.name) for party in res]

        return response