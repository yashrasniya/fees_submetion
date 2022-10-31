from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from divisions.models import batch, branch
from rest_framework_simplejwt.tokens import RefreshToken

from django.conf import settings


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, mobile_number, password, **extra_fields):
        if not mobile_number:
            raise ValueError('The given email must be set')

        user = self.model(mobile_number=mobile_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, mobile_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(mobile_number, password, **extra_fields)

    def create_superuser(self, mobile_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if batch.objects.last():
            obj1 = batch.objects.last()
        else:
            obj1 = batch.objects.create(batch_name='test')
        if branch.objects.last():
            obj2 = branch.objects.last()
        else:
            obj2 = branch.objects.create(branch_name='test')

        extra_fields.setdefault('batch', obj1)
        extra_fields.setdefault('branch', obj2)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(mobile_number, password, **extra_fields)


class Student(AbstractUser):
    father_name = models.CharField(max_length=20, null=False)
    batch = models.ForeignKey('divisions.batch', on_delete=models.CASCADE, null=True)
    branch = models.ForeignKey('divisions.branch', on_delete=models.CASCADE, null=True)

    mobile_number = models.IntegerField(null=False, unique=True)
    username = models.CharField(max_length=50, null=False)
    roll_number = models.IntegerField(null=False, primary_key=True)
    USERNAME_FIELD = 'mobile_number'
    objects = UserManager()

    def batch_name(self):
        return self.batch.batch_name

    def branch_name(self):
        return self.branch.branch_name



    def __str__(self):
        return str(self.mobile_number)
