from application import db
from application.models import Base

from sqlalchemy.sql import text

class Reminder(Base):

    note = db.Column(db.String(250), nullable=False)
    date_remind = db.Column(db.Date, nullable=False)
    done = db.Column(db.Boolean, nullable=False)

    contract_id = db.Column(db.Integer, db.ForeignKey('contract.id'),
                           nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, note):
        self.note = note
        self.done = False

    @staticmethod
    def all_reminders():
        stmt = text("SELECT Reminder.id, Reminder.note, Reminder.date_remind, Reminder.done, Contract.id, Contract.name, Account.id, Account.username, Account.name FROM Reminder"
                    " JOIN Account ON Reminder.account_id = Account.id"
                    " JOIN Contract ON Reminder.contract_id = Contract.id")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "note":row[1], "date_remind":row[2], "done":row[3], "contract_id":row[4], "contract_name":row[5], "account_id":row[6], "account_username":row[7], "account_name":row[8]})

        return response