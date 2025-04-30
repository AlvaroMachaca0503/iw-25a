from models.generation_db import db


class Teacher(db.Model):
    __tablename__ = 'teachers'

    id = db.Column(db.Integer, primary_key=True)
    names = db.Column(db.String(255))
    father_surname = db.Column(db.String(255))
    mother_surname = db.Column(db.String(255))
    email = db.Column(db.String(255))
    phone = db.Column(db.String(20))
    show_phone = db.Column(db.Boolean, default=False)
    status = db.Column(db.String(20))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = self.names.upper()
        self.father_surname = self.father_surname.upper()
        self.mother_surname = self.mother_surname.upper()

    def __str__(self):
        return f"{self.names} {self.father_surname} {self.mother_surname}"