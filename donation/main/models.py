from django.db import models


# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact1 = models.IntegerField()
    standard = models.IntegerField()
    dateOfBirth = models.DateField()
    joined_Date = models.DateField()
    last_Date = models.DateField()
    interests = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'student'


class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=False)
    contact1 = models.IntegerField(null=False)
    expertise = models.CharField(max_length=400)
    dateOfBirth = models.DateField()
    joined_Date = models.DateField()
    last_Date = models.DateField()

    class Meta:
        managed = False
        db_table = 'teacher'


class Supervisor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=False)
    contact1 = models.IntegerField( null=False)
    goods_or_services = models.CharField(max_length=400)
    dateOfBirth = models.DateField()
    joined_Date = models.DateField()
    last_Date = models.DateField()

    class Meta:
        managed = False
        db_table = 'supervisor'


class Awards(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    winner = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='sid_winner')
    runner_up = models.ForeignKey(Student, on_delete=models.CASCADE,related_name='sid_runner_up')
    winner_senior = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='tid_winner')
    runner_up_senior = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='tid_runner_up')

    class Meta:
        managed = False
        db_table = 'awards'


class Events(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    event_date = models.DateField()
    awards_id = models.CharField(max_length=400)
