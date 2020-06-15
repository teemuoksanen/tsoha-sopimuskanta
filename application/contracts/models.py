from application import db
from application.models import Base
from flask_login import current_user
import datetime

from sqlalchemy.sql import text
from datetime import date

contractparties = db.Table('contractparty',
    db.Column('contract_id', db.Integer, db.ForeignKey('contract.id'), primary_key=True),
    db.Column('party_id', db.Integer, db.ForeignKey('party.id'), primary_key=True)
)

class Contract(Base):

    name = db.Column(db.String(144), nullable=False)
    date_signed = db.Column(db.Date)
    date_entry = db.Column(db.Date)
    date_expiry = db.Column(db.Date)

    parties = db.relationship('Party', secondary=contractparties, lazy='subquery',
        backref=db.backref('contracts', lazy='subquery'))

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

    @staticmethod
    def search(search, onlyOwn, onlyValid):
        stmt = "SELECT id, name, date_signed, date_entry, date_expiry FROM Contract"

        if search != "":
            stmt = stmt + " WHERE upper(name) LIKE :search"
        
        if onlyOwn == True:
            if "WHERE" in stmt:
                stmt = stmt + " AND "
            else:
                stmt = stmt + " WHERE "
            stmt = stmt + "account_id = :account_id"
        
        if onlyValid == True:
            if "WHERE" in stmt:
                stmt = stmt + " AND "
            else:
                stmt = stmt + " WHERE "
            stmt = stmt + "date_entry <= :today AND (date_expiry IS NULL OR date_expiry >= :today)"

        stmt = text(stmt).params(search = "%" + search.upper() + "%", account_id = current_user.id, today = date.today())
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "date_signed":Base.correct_date_format(row[2]), "date_entry":Base.correct_date_format(row[3]), "date_expiry":Base.correct_date_format(row[4])})

        return response
