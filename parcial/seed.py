from app import app
from models.generation_db import db
from models.course import Course
from models.student import Student
from models.teacher import Teacher
from models.workload import Workload


def seed_data():
    with app.app_context():
        db.create_all()

        if Course.query.first():
            print("Ya hay datos cargados. Omitir la inserción.")
            return

        student = Student(
            cui="202312345",
            names="Juan",
            father_surname="Pérez",
            mother_surname="García",
            email="juan@example.com",
            phone="999999999",
            status="activo"
        )

        course = Course(
            curriculum="2023",
            year=1,
            semester=1,
            code="INF101",
            name="Introducción a la Informática",
            acronym="INF1",
            credits=4,
            theory_hours=3,
            practice_hours=1,
            laboratory_hours=0,
            laboratory=False,
            status="activo"
        )

        prerequisite = Course(
            curriculum="2023",
            year=1,
            semester=1,
            code="MAT100",
            name="Matemática Básica",
            acronym="MAT1",
            credits=4,
            theory_hours=3,
            practice_hours=1,
            laboratory_hours=0,
            laboratory=False,
            status="activo"
        )

        teacher = Teacher(
            names="Carlos",
            father_surname="Ramírez",
            mother_surname="Lopez",
            email="carlos@example.com",
            phone="123456789",
            status="activo"
        )

        workload = Workload(
            course=course,
            group="A",
            laboratory=False,
            capacity=30,
            teacher=teacher,
            status="activo"
        )

        course.prerequisites.append(prerequisite)

        db.session.add_all([student, course, prerequisite, teacher, workload])
        db.session.commit()

        print("Datos de ejemplo insertados correctamente.")
