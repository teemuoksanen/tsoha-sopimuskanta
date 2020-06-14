from application import db
from application.models import Base
import datetime

from sqlalchemy.sql import text
from datetime import date

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
    def all_undone_reminders():
        stmt = text("SELECT Reminder.id, Reminder.note, Reminder.date_remind, Reminder.done, Contract.id, Contract.name, Account.id, Account.username, Account.name FROM Reminder"
                    " JOIN Account ON Reminder.account_id = Account.id"
                    " JOIN Contract ON Reminder.contract_id = Contract.id"
                    " WHERE Reminder.done = FALSE")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            # Fix type for dates in SQLite
            if isinstance(row[2], str):
                date_remind = datetime.datetime.strptime(row[2], '%Y-%m-%d').date()
            else:
                date_remind = row[2]
            response.append({"id":row[0], "note":row[1], "date_remind":date_remind, "done":row[3], "contract_id":row[4], "contract_name":row[5], "account_id":row[6], "account_username":row[7], "account_name":row[8]})

        return response

    @staticmethod
    def all_done_reminders():
        stmt = text("SELECT Reminder.id, Reminder.note, Reminder.date_remind, Reminder.done, Contract.id, Contract.name, Account.id, Account.username, Account.name FROM Reminder"
                    " JOIN Account ON Reminder.account_id = Account.id"
                    " JOIN Contract ON Reminder.contract_id = Contract.id"
                    " WHERE Reminder.done = TRUE")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            # Fix type for dates in SQLite
            if isinstance(row[2], str):
                date_remind = datetime.datetime.strptime(row[2], '%Y-%m-%d').date()
            else:
                date_remind = row[2]
            response.append({"id":row[0], "note":row[1], "date_remind":date_remind, "done":row[3], "contract_id":row[4], "contract_name":row[5], "account_id":row[6], "account_username":row[7], "account_name":row[8]})

        return response

    @staticmethod
    def active_reminders_for_user(account_id):
        stmt = text("SELECT Reminder.id, Reminder.note, Reminder.date_remind, Reminder.done, Contract.id, Contract.name, Account.id FROM Reminder"
                    " JOIN Account ON Reminder.account_id = Account.id"
                    " JOIN Contract ON Reminder.contract_id = Contract.id"
                    " WHERE (Account.id = :account_id AND Reminder.done = FALSE AND Reminder.date_remind <= :date)").params(account_id=account_id, date = date.today())
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            # Fix type for dates in SQLite
            if isinstance(row[2], str):
                date_remind = datetime.datetime.strptime(row[2], '%Y-%m-%d').date()
            else:
                date_remind = row[2]
            response.append({"id":row[0], "note":row[1], "date_remind":date_remind, "done":row[3], "contract_id":row[4], "contract_name":row[5], "account_id":row[6]})

        return response

    @staticmethod
    def undone_reminders_for_user(account_id):
        stmt = text("SELECT Reminder.id, Reminder.note, Reminder.date_remind, Reminder.done, Contract.id, Contract.name FROM Reminder"
                    " JOIN Contract ON Reminder.contract_id = Contract.id"
                    " WHERE Reminder.account_id = :account_id AND Reminder.done = FALSE").params(account_id=account_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            # Fix type for dates in SQLite
            if isinstance(row[2], str):
                date_remind = datetime.datetime.strptime(row[2], '%Y-%m-%d').date()
            else:
                date_remind = row[2]
            response.append({"id":row[0], "note":row[1], "date_remind":date_remind, "done":row[3], "contract_id":row[4], "contract_name":row[5]})

        return response

    @staticmethod
    def done_reminders_for_user(account_id):
        stmt = text("SELECT Reminder.id, Reminder.note, Reminder.date_remind, Reminder.done, Contract.id, Contract.name FROM Reminder"
                    " JOIN Contract ON Reminder.contract_id = Contract.id"
                    " WHERE Reminder.account_id = :account_id AND Reminder.done = TRUE").params(account_id=account_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            # Fix type for dates in SQLite
            if isinstance(row[2], str):
                date_remind = datetime.datetime.strptime(row[2], '%Y-%m-%d').date()
            else:
                date_remind = row[2]
            response.append({"id":row[0], "note":row[1], "date_remind":date_remind, "done":row[3], "contract_id":row[4], "contract_name":row[5]})

        return response