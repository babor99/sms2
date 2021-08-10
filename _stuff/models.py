from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Stuff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='stuffs')
    age = models.CharField(max_length=50)
    stuff_id = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    stuff_salary = models.PositiveIntegerField()
    is_active = models.BooleanField()
    is_married = models.BooleanField()
    phone = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=100)
    def __str__(self):
        return self.user.username


class StuffAttendance(models.Model):
    stuff = models.ForeignKey(Stuff, on_delete=models.CASCADE)
    _date = models.DateField()
    is_present = models.BooleanField()
    def __str__(self):
        return self.stuff.user.username