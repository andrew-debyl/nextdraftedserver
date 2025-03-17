from django.contrib import admin
from .models import Athlete, Recruiter, SportPortfolio, SportPortfolioItem

# Register your models here.
admin.site.register(Athlete)
admin.site.register(Recruiter)
admin.site.register(SportPortfolio)
admin.site.register(SportPortfolioItem)