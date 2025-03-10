import sys
from django.utils.timezone import now
try:
    from django.db import models
except Exception:
    print("There was an error loading django modules. Do you have django installed?")
    sys.exit()

from django.contrib.auth.models import User

# Create your models here.
class Athlete(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True) 
    sport = models.CharField(max_length=100, blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='athletes/', null=True, blank=True)
    #CONTACT AND SOCIAL MEDIA

    def __str__(self):
        return f"{self.first_name} {self.last_name}'s Profile"

class Recruiter(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True) 
    organization = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    sport = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='recruiters/', null=True, blank=True)
    #CONTACT METHODS

    def __str__(self):
        return f"{self.first_name} {self.last_name}'s Profile"