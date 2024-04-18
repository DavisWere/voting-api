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
    USER_TYPES = [
        ('voter', 'Voter'),
        ('candidate', 'Candidate'),
    ]
    first_name = models.CharField(max_length=255, null = True, blank=True)
    last_name = models.CharField(max_length=255, null = True, blank=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255, null = False, blank=False)  
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    email = models.EmailField()
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default= 'voter', null= False, blank=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Position(models.Model):
    TITLE_CHOICES = [
        ('president', 'President'),
        ('vice_president', 'Vice President'),
        ('secretary', 'Secretary'),
        ('treasurer', 'Treasurer'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank= True)
    title = models.CharField(max_length=255, choices=TITLE_CHOICES, default= 'president')
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Election(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Vote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)

    def __str__(self):
        return f"Vote {self.voter.username} for {self.position.title} in {self.election.title}"
    



