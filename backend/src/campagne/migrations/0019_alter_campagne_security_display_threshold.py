# Generated by Django 4.0.3 on 2024-05-15 10:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campagne', '0018_remove_invitation_invited_remove_invitation_reminded_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campagne',
            name='security_display_threshold',
            field=models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(5)], verbose_name='Minimum Teilnehmende für die Datenaggregation'),
        ),
    ]
