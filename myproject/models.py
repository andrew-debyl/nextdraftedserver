import sys
from django.utils.timezone import now
try:
    from django.db import models
except Exception:
    print("There was an error loading django modules. Do you have django installed?")
    sys.exit()

from django.contrib.auth.models import User
import json

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
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)

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
    email = models.EmailField(blank=True, null=True) 
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}'s Profile"
    

class SportPortfolio(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, related_name='sport_portfolios')
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    sport = models.CharField(max_length=100, blank=True, null=True)
    team = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    portfolio_image = models.ImageField(upload_to='portfolio_images/', null=True, blank=True)
    email = models.EmailField(blank=True, null=True) 
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.athlete.first_name} {self.athlete.last_name} ({self.sport})"
    

class SportPortfolioItem(models.Model):
    CATEGORY_CHOICES = [
        ('stats', 'Stats'),
        ('metrics', 'Performance Metrics'),
        ('image', 'Image Gallery'),
        ('video', 'Video'),
    ]

    sport_portfolio = models.ForeignKey(SportPortfolio, on_delete=models.CASCADE, related_name='items')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=200, blank=True, null=True)
    data = models.TextField(blank=True, null=True) 
    image = models.ImageField(upload_to='portfolio_items/', null=True, blank=True)
    order = models.IntegerField(default=0)

    def get_data_as_dict(self):
        if self.data:
            try:
                return json.loads(self.data)
            except json.JSONDecodeError:
                return None
        return None

    def __str__(self):
        return f"{self.title} ({self.category})" if self.title else f"{self.category}"