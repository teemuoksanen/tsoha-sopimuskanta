from application import db
from application.models import Base

from sqlalchemy.sql import text
from datetime import date

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

    @staticmethod
    def parties_with_most_contracts():
        stmt = text("SELECT Party.id, Party.name, COUNT(Contract.id) AS contracts_count FROM Party"
                    " JOIN ContractParty ON ContractParty.party_id = Party.id"
                    " JOIN Contract ON ContractParty.contract_id = Contract.id"
                    " GROUP BY Party.id"
                    " HAVING contracts_count > 0"
                    " ORDER BY contracts_count DESC LIMIT 5")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "contracts_count":row[2]})
        return response

    @staticmethod
    def parties_with_most_valid_contracts():
        stmt = text("SELECT Party.id, Party.name, COUNT(Contract.id) AS contracts_count FROM Party"
                    " JOIN ContractParty ON ContractParty.party_id = Party.id"
                    " JOIN Contract ON ContractParty.contract_id = Contract.id"
                    " WHERE Contract.date_entry <= :today AND (Contract.date_expiry IS NULL OR Contract.date_expiry >= :today)"
                    " GROUP BY Party.id"
                    " ORDER BY contracts_count DESC LIMIT 5").params(today = date.today())
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "contracts_count":row[2]})
        return response

    @staticmethod
    def parties_with_no_contracts():
        stmt = text("SELECT Party.id, Party.name FROM Party"
                    " LEFT JOIN ContractParty ON ContractParty.party_id = Party.id"
                    " LEFT JOIN Contract ON ContractParty.contract_id = Contract.id"
                    " GROUP BY Party.id"
                    " HAVING COUNT(Contract.id) = 0")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})
        return response