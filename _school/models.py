from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.fields.related import OneToOneField

from _teacher.models import Teacher
from _stuff.models import Stuff

#babor, babor8872
#12345karim, 12345rahim, 12345javed, 12345mon, 12345kiran, 12345amit
# Create your models here.
class AdminUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='admins')

class Term(models.Model):
    name = models.CharField(max_length=50)
    year = models.CharField(max_length=10)
    total_students = models.PositiveIntegerField()
    total_exams = models.PositiveIntegerField()
    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=50)
    total_students = models.PositiveIntegerField()
    total_sections = models.PositiveIntegerField()
    def __str__(self):
        return str(self.id) +'-'+self.name


class Section(models.Model):
    name = models.CharField(max_length=10)
    _class = models.ForeignKey(Class, on_delete=models.CASCADE)
    total_students = models.PositiveIntegerField()
    def __str__(self):
        return self.name

classes = Class.objects.all()
CLASS_CHOICES = ([(str(cls), str(cls)) for cls in classes])
class Subject(models.Model):
    name = models.CharField(max_length=100)
    _class = models.CharField(max_length=20, choices=CLASS_CHOICES, default='None')
    subject_code = models.CharField(max_length=50)
    total_chapter = models.PositiveIntegerField()
    def __str__(self):
        return self.name


GROUP_CHOICES = (
    ('None', 'None'),
    ('Science', 'Science'),
    ('Commerce', 'Commerce'),
    ('Arts', 'Arts'),
)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='students')
    age = models.CharField(max_length=50)
    student_id = models.CharField(max_length=50)
    _class = models.ForeignKey(Class, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    _group = models.CharField(max_length=20, choices=GROUP_CHOICES, default='None')
    phone = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=50, null=True, blank=True)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    def __str__(self):
        return self.user.username


class StudentAttendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    _date = models.DateField()
    is_present = models.BooleanField()
    def __str__(self):
        return self.student.user.username


GRADE_CHOICES = (
    ('A+', 'A+'),
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ('F', 'F'),
)

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    written_mark = models.PositiveIntegerField()
    objective_mark = models.PositiveIntegerField()
    practical_mark = models.PositiveIntegerField()
    total_mark = models.PositiveIntegerField()
    grade = models.CharField(max_length=10, choices=GRADE_CHOICES, default='F')
    is_passed = models.BooleanField()
    publication_date = models.DateTimeField()
    def __str__(self):
        return self.student.user.username+'-'+self.subject.name+'-'+self.grade


class Exam(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    _class = models.ForeignKey(Class, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    is_completed = models.BooleanField()
    duration = models.FloatField()
    _date = models.DateTimeField()
    def __str__(self):
        return self.subject.name+'-'+self._class.name


MONTH_CHOICES = (
    ('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'),
    ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'),
    ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December'),
)

class Salary(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True,)
    stuff = models.ForeignKey(Stuff, on_delete=models.CASCADE, null=True, blank=True)
    month = models.CharField(max_length=20, choices=MONTH_CHOICES, default='January')
    salary_amount = models.PositiveIntegerField()
    paying_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.teacher.user.username


class LogisticsExpenditure(models.Model):
    name = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    receipt_no = models.CharField(max_length=50, null=True, blank=True)
    model_no = models.CharField(max_length=50, null=True, blank=True)
    company = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()
    def __str__(self):
        return self.name+'-'+str(self.amount)