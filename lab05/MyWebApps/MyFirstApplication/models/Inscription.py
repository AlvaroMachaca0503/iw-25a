from django.db import models
from django.db.models.constraints import UniqueConstraint
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from django.utils.translation import gettext_lazy as _
import uuid

from .Workload import Workload
from .Student import Student

def validate_even(value):
    if value == 1:
        raise ValidationError(
            _('%(value)s is 1'),
            params={'value': value},
        )

class Inscription(models.Model):
    workload = models.ForeignKey(Workload, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, validators=[validate_even])
    status = models.BooleanField(default=True, null=False)
    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)

    class Meta:
        ordering = ['workload', 'student', 'created']
        constraints = [
            models.UniqueConstraint(fields=['workload', 'student'], name='unique_inscription')
        ]

    def clean(self):
        if self.workload.id == 3 and self.student.id == 2:
            raise ValidationError("No se puede inscribir workload=3 student=2")
        super(Inscription, self).clean()

    def save(self, *args, **kwargs):
        self.clean()
        return super(Inscription, self).save(*args, **kwargs)

    def __str__(self):
        return "%s %s" % (self.workload, self.student)



