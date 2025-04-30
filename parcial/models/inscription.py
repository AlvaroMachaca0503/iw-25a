from sqlalchemy.orm import relationship
from models.generation_db import db
from flask import abort
from flask_admin.contrib.sqla import ModelView
from wtforms.fields import SelectField
from models.student import Student
from models.workload import Workload
from wtforms_sqlalchemy.fields import QuerySelectField


class Inscription(db.Model):
    __tablename__ = 'inscriptions'

    id = db.Column(db.Integer, primary_key=True)
    workload_id = db.Column(db.Integer, db.ForeignKey('workloads.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    status = db.Column(db.String(20))

    workload = db.relationship('Workload', backref='inscriptions')
    student = db.relationship('Student', backref='inscriptions')

    def save(self):
        self.validate_inscription()
        db.session.add(self)
        db.session.commit()

    def validate_inscription(self):
        if self.student_id == 1:
            abort(400, description='El valor 1 no está permitido para student_id.')
        if self.workload_id == 3 and self.student_id == 2:
            abort(400, description='No se puede inscribir workload=3 student=2.')
            

class InscriptionAdmin(ModelView):
    column_list = ('id', 'student', 'workload', 'status')
    form_extra_fields = {
        'student': QuerySelectField(
            label='Student',
            query_factory=lambda: Student.query.all(),
            allow_blank=False
        ),
        'workload': QuerySelectField(
            label='Workload',
            query_factory=lambda: Workload.query.all(),
            allow_blank=False
        )
    }

