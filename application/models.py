from application import db
import datetime

class Base(db.Model):

    __abstract__ = True
  
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    # Fix type for dates in SQLite
    @staticmethod
    def correct_date_format(original):
        if isinstance(original, str):
            return datetime.datetime.strptime(original, '%Y-%m-%d').date()
        else:
            return original