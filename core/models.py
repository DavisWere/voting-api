from django.db import models
import django
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
import os
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import RegexValidator
from django.utils import timezone

# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=40, null= True, blank=True)
    last_name = models.CharField(max_length=40, null= True, blank=True)
    email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return self.username