# Generated by Django 5.1.7 on 2025-03-10 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0005_remove_recruiter_company_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruiter',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=15, null=True),
        ),
    ]
