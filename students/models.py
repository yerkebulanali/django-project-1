from django.db import models
from courses.models import Course

class Student(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    dob = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True, null=True)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=255)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.lastname
