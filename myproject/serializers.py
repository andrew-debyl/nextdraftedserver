from rest_framework import serializers
from .models import Athlete, Recruiter, SportPortfolio, SportPortfolioItem
import json

class AthleteSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(allow_blank=True, allow_null=True)
    phone_number = serializers.CharField(allow_blank=True, allow_null=True)
    instagram = serializers.URLField(allow_blank=True, allow_null=True)
    linkedin = serializers.URLField(allow_blank=True, allow_null=True)
    youtube = serializers.URLField(allow_blank=True, allow_null=True)
    facebook = serializers.URLField(allow_blank=True, allow_null=True)
    class Meta:
        model = Athlete
        fields = ['first_name', 'last_name', 'sport', 'height', 'weight', 'bio', 'location', 'gender', 'profile_picture', 'birth_date', 'email', 'phone_number', 'instagram', 'linkedin', 'youtube', 'facebook']


class RecruiterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(allow_blank=True, allow_null=True)
    phone_number = serializers.CharField(allow_blank=True, allow_null=True)
    instagram = serializers.URLField(allow_blank=True, allow_null=True)
    linkedin = serializers.URLField(allow_blank=True, allow_null=True)
    youtube = serializers.URLField(allow_blank=True, allow_null=True)
    facebook = serializers.URLField(allow_blank=True, allow_null=True)

    class Meta:
        model = Recruiter
        fields = ['first_name', 'last_name', 'organization', 'title', 'bio', 'location', 'sport', 'gender', 'profile_picture', 'email', 'phone_number', 'instagram', 'linkedin', 'youtube', 'facebook']


class SportPortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportPortfolio
        fields = ['id', 'athlete', 'title', 'description', 'sport', 'team', 'position', 'created_at', 'updated_at', 'portfolio_image', 'email', 'phone_number', 'instagram', 'linkedin', 'youtube', 'facebook']


class SportPortfolioItemSerializer(serializers.ModelSerializer):
    data = serializers.JSONField(required=False) # Important for handling JSON data

    class Meta:
        model = SportPortfolioItem
        fields = ['id', 'sport_portfolio', 'category', 'title', 'data', 'image', 'order']