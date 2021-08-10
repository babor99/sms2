from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='teachers')
    age = models.CharField(max_length=50)
    teacher_id = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    teacher_salary = models.PositiveIntegerField()
    is_active = models.BooleanField()
    is_married = models.BooleanField()
    phone = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=100)
    def __str__(self):
        return self.user.username


class TeacherAttendance(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    _date = models.DateField()
    is_present = models.BooleanField()
    def __str__(self):
        return self.teacher.user.username