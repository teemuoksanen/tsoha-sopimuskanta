from application import db

class Contract(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

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