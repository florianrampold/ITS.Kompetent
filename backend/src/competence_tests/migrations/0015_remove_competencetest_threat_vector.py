# Generated by Django 4.0.3 on 2024-04-23 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competence_tests', '0014_remove_emailitem_email_button_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competencetest',
            name='threat_vector',
        ),
    ]