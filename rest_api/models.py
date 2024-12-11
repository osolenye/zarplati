from django.db import models
from django.contrib.auth.models import AbstractUser

class Company(models.Model):
    name = models.CharField(max_length=100)
    employees_count = models.IntegerField()

class Admin(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='admins', default=None)

    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='admin_set',  # Add a unique related_name here
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='admin_set',  # Add a unique related_name here
    )

class Worker(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=20)
    position = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='workers')