from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

class Teacher(models.Model):
    names = models.CharField(null=False, blank=False, max_length=155)
    father_surname = models.CharField(null=False, blank=False, max_length=155)
    mother_surname = models.CharField(null=False, blank=False, max_length=155)
    email = models.EmailField(unique=True, null=True, blank=True, max_length=255)
    phone = models.CharField(null=True, blank=True, max_length=255)
    show_phone = models.BooleanField(default=False, null=False)
    status = models.BooleanField(default=True, null=False)
    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)

    class Meta:
        ordering = ['names', 'father_surname', 'mother_surname']

    def save(self, *args, **kwargs):
        self.names = self.names.upper()
        self.father_surname = self.father_surname.upper()
        self.mother_surname = self.mother_surname.upper()
        return super(Teacher, self).save(*args, **kwargs)

    def __str__(self):
        return "%s %s %s" % (self.names, self.father_surname, self.mother_surname)




