from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Staff(models.Model):

    ROLE_CHOICES = [
        ('manager', 'Manager'),
        ('receptionist', 'Receptionist')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.user.username
