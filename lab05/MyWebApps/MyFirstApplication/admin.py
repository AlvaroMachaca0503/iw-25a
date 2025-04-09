from django.contrib import admin

from .models.Course import Course
from .models.Teacher import Teacher
from .models.Workload import Workload
from .models.Student import Student
from .models.Inscription import Inscription

# Registrar los modelos en el panel de administración
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Workload)
admin.site.register(Student)
admin.site.register(Inscription)



