from form import db

class Register(db.Model):
    __tablename__ = "participants"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    occupation = db.Column(db.String(80), nullable=False)
    age = db.Column(db.String(2))
    number = db.Column(db.String(11), unique=True)

    def __init__(self, name, email, occupation, age, number):
            self.name = name
            self.email = email
            self.occupation = occupation
            self.age = age
            self.number = number
    
    def __repr__(self) -> str:
          return self._repr(id = self.id, name = self.name,
                            email = self.email, occupation = self.occupation,
                            age = self.age, number = self.number)
