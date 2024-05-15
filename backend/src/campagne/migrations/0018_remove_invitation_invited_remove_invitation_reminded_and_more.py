# Generated by Django 4.0.3 on 2024-05-13 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campagne', '0017_remove_campagne_security_display_profile_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invitation',
            name='invited',
        ),
        migrations.RemoveField(
            model_name='invitation',
            name='reminded',
        ),
        migrations.AddField(
            model_name='invitation',
            name='usage_active',
            field=models.BooleanField(default=True),
        ),
    ]