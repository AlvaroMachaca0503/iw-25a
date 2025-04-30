from models.generation_db import db
from sqlalchemy.orm import relationship
import uuid

course_prerequisites = db.Table(
    'course_prerequisites',
    db.Column('course_id', db.String(36), db.ForeignKey('courses.id')),
    db.Column('prerequisite_id', db.String(36), db.ForeignKey('courses.id'))
)


class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    curriculum = db.Column(db.String(255))
    year = db.Column(db.Integer)
    semester = db.Column(db.Integer)
    code = db.Column(db.String(20))
    name = db.Column(db.String(255))
    acronym = db.Column(db.String(20))
    credits = db.Column(db.Integer)
    theory_hours = db.Column(db.Integer)
    practice_hours = db.Column(db.Integer)
    laboratory_hours = db.Column(db.Integer)
    laboratory = db.Column(db.Boolean, default=False)
    status = db.Column(db.String(20))

    prerequisites = db.relationship(
        'Course',
        secondary='course_prerequisites',
        primaryjoin='Course.id==course_prerequisites.c.course_id',
        secondaryjoin='Course.id==course_prerequisites.c.prerequisite_id',
        backref='required_by'
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = self.name.upper()
        self.acronym = self.acronym.upper()
