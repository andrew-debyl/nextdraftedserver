# Generated by Django 5.1.7 on 2025-03-10 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0004_alter_athlete_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recruiter',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='recruiter',
            name='job_title',
        ),
        migrations.AddField(
            model_name='athlete',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='recruiter',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recruiter',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='recruiter',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='recruiter',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='recruiter',
            name='organization',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='recruiter',
            name='sport',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='recruiter',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
