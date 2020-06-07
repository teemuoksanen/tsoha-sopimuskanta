from application import db
from application.models import Base

from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    user_role = db.Column(db.String(80), nullable=False)

    contracts = db.relationship("Contract", backref='account', lazy=True)

    def __init__(self, name, username, password, user_role):
        self.name = name
        self.username = username
        self.password = password
        self.user_role = user_role
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        return self.user_role

    @staticmethod
    def users_with_contracts_count():
        stmt = text("SELECT Account.id, Account.username, Account.name, Account.user_role, COUNT(Contract.id) FROM Account"
                    " LEFT JOIN Contract ON Contract.account_id = Account.id"
                    " GROUP BY Account.id")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "username":row[1], "name":row[2], "user_role":row[3], "contracts_count":row[4]})

        return response