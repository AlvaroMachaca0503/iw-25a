from flask import Flask
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from config import Config
from models.generation_db import db
from models.course import Course
from models.inscription import Inscription, InscriptionAdmin
from models.student import Student
from models.teacher import Teacher
from models.workload import Workload
import click


app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = '123456'


@app.cli.command("seed")
def seed():
    from seed import seed_data
    seed_data()
    

db.init_app(app)
migrate = Migrate(app, db)

admin = Admin(app, name='Admin Panel')
admin.add_view(ModelView(Course, db.session))
admin.add_view(InscriptionAdmin(Inscription, db.session))
admin.add_view(ModelView(Student, db.session))
admin.add_view(ModelView(Teacher, db.session))
admin.add_view(ModelView(Workload, db.session))


if __name__ == "__main__":
    app.run(debug=True)
