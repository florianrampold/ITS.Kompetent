# Generated by Django 4.0.3 on 2024-09-27 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competence_tests', '0025_chatinterface_impulse_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionitem',
            name='question_name',
        ),
    ]