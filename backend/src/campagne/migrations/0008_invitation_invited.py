# Generated by Django 4.0.3 on 2024-01-29 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campagne', '0007_invitation_email_encrypted'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitation',
            name='invited',
            field=models.BooleanField(default=False),
        ),
    ]
