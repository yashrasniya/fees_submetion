from django.db import models
from datetime import datetime


# Create your models here.
class batch(models.Model):
    batch_list = [(f"{a}-{a + 4}", f"{a}-{a + 4}") for a in range(2014, 1 + int(str(datetime.now()).split("-")[0]))]

    batch_name = models.CharField(max_length=200, choices=batch_list, null=True, blank=True)


class branch(models.Model):
    branch_list = [
        ('Computer Science Engineering', 'Computer Science Engineering'),
        ('Mechanical Engineering', 'Mechanical Engineering'),
        ('Electronics & Communication', 'Electronics & Communication'),
        ('Electronics Engineering', 'Electronics Engineering'),
        ('Civil Engineering', 'Civil Engineering')
    ]
    branch_name = models.CharField(max_length=200, choices=branch_list, null=True, blank=True)

class semester(models.Model):
    semester_list = [(f'{i} semester',f'{i} semester') for i in range(1,9)]
    branch=models.ForeignKey(branch,on_delete=models.CASCADE)
    batch=models.ForeignKey(batch,on_delete=models.CASCADE)
    semester_name = models.CharField(max_length=200, choices=semester_list, null=True, blank=True)

    TuitionFee = models.IntegerField(null=False)
    ExamFee = models.IntegerField(null=False)
    EnrollmentFee = models.IntegerField(null=False)
    RegistrationFee = models.IntegerField(null=False)
    SecurityDeposited = models.IntegerField(null=False)
    SportFee = models.IntegerField(null=False)
    DevelopmentFee = models.IntegerField(null=False)
    WelfareFee = models.IntegerField(null=False)
