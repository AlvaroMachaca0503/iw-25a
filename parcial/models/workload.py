from sqlalchemy.orm import relationship
from models.generation_db import db


class Workload(db.Model):
    __tablename__ = 'workloads'

    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.String(36), db.ForeignKey('courses.id'))
    group = db.Column(db.String(10))
    laboratory = db.Column(db.Boolean, default=False)
    capacity = db.Column(db.Integer)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))
    status = db.Column(db.String(20))

    course = db.relationship('Course', backref='workloads')
    teacher = db.relationship('Teacher', backref='workloads')

    def __str__(self):
        return f"{self.course} {self.group} {self.laboratory} {self.capacity} {self.teacher}"
