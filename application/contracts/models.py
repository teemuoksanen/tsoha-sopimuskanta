from application import db

class Contract(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    date_signed = db.Column(db.DateTime)
    date_entry = db.Column(db.DateTime)
    date_expiry = db.Column(db.DateTime)
    value = db.Column(db.Numeric)
    notes = db.Column(db.String(250))

    def __init__(self, name):
        self.name = name

