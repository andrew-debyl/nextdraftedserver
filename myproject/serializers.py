from rest_framework import serializers
from .models import Athlete, Recruiter

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