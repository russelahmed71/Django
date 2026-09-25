from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    semester = models.IntegerField()
    department = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='students/', blank=True, null=True)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    u_id = models.IntegerField()

    def __str__(self):
        return self.name
