from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    CURRICULUMS = [
        (0, 'Sin Plan'),
        (2017, 'Plan 2017'),
        (2023, 'Plan 2023'),
    ]
    curriculum = models.IntegerField(null=False, choices=CURRICULUMS, default=2017)

    YEARS = [
        (0, 'Sin año'),
        (1, '1er año'),
        (2, '2do año'),
        (3, '3er año'),
        (4, '4to año'),
        (5, '5to año'),
        (6, '6to año'),
        (7, '7mo año'),
    ]
    year = models.IntegerField(null=False, choices=YEARS, default=0)

    SEMESTERS = [
        (0, 'Sin semestre'),
        (1, 'I semestre'),
        (2, 'II semestre'),
        (3, 'III semestre'),
        (4, 'IV semestre'),
        (5, 'V semestre'),
        (6, 'VI semestre'),
        (7, 'VII semestre'),
        (8, 'VIII semestre'),
        (9, 'IX semestre'),
        (10, 'X semestre'),
    ]
    semester = models.IntegerField(null=False, choices=SEMESTERS, default=0)

    code = models.CharField(unique=True, null=True, blank=True, max_length=25)
    name = models.CharField(null=False, blank=False, max_length=255)
    acronym = models.CharField(null=True, blank=True, max_length=25)
    credits = models.DecimalField(null=True, blank=True, max_digits=4, decimal_places=2)
    theory_hours = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)
    practice_hours = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)
    laboratory_hours = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)
    laboratory = models.BooleanField(default=True, null=False)
    status = models.BooleanField(default=True, null=False)
    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)
    prerequisites = models.ManyToManyField('self', blank=True, symmetrical=False)

    class Meta:
        ordering = ['curriculum', 'year', 'semester', 'code', 'name']

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        if self.acronym is not None:
            self.acronym = self.acronym.upper()
        return super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return "%s %s %s %s %s" % (self.curriculum, self.year, self.semester, self.code, self.name)



