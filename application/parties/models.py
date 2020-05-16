from application import db

class Party(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    business_id = db.Column(db.String(9))
    address_street = db.Column(db.String(144))
    address_postalcode = db.Column(db.String(5))
    address_city = db.Column(db.String(50))
    bankrupt = db.Column(db.Boolean, nullable=False)

    def __init__(self, name):
        self.name = name
        self.bankrupt = False