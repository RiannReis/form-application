from form import db

class Register(db.Model):
    __tablename__ = "participants"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(db.String(80), nullable=False))
    email = db.Column(db.String(120), unique=True, nullable=False)
    occupation = db.Column(db.String(80), nullable=False)
    age = db.Column(db.String(2))
    number = db.Column(db.String(11))
