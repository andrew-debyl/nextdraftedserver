# Generated by Django 5.1.7 on 2025-03-12 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0011_remove_recruiter_birth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recruiter',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
