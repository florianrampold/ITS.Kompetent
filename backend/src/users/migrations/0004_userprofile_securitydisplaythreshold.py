# Generated by Django 4.0.3 on 2024-05-07 15:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_userprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='securityDisplayThreshold',
            field=models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(5)]),
        ),
    ]
