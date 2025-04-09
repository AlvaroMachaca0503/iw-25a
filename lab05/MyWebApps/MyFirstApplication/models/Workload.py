from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

from .Course import Course
from .Teacher import Teacher

class Workload(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    GROUPS = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
    ]
    group = models.CharField(null=False, max_length=1, choices=GROUPS, default='A')

    LABORATORIES = [
        ('lab01', 'Laboratorio 01'),
        ('lab02', 'Laboratorio 02'),
        ('lab03', 'Laboratorio 03'),
        ('lab04', 'Laboratorio 04'),
        ('lab05', 'Laboratorio 05'),
        ('lab06', 'Laboratorio 06'),
        ('lab07', 'Laboratorio 07'),
        ('lab08', 'Laboratorio 08'),
    ]
    laboratory = models.CharField(null=False, max_length=6, choices=LABORATORIES, default='lab01')

    capacity = models.PositiveIntegerField(null=False, default=20)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    status = models.BooleanField(default=True, null=False)
    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)

    class Meta:
        ordering = ['course', 'group', 'laboratory', 'capacity', 'teacher']
        constraints = [
            models.UniqueConstraint(fields=['course', 'group'], name='unique_workload')
        ]

    def __str__(self):
        return "%s %s %s %s %s" % (self.course, self.group, self.laboratory, self.capacity, self.teacher)




