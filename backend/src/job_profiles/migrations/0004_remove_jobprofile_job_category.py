# Generated by Django 4.0.3 on 2022-06-28 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_profiles', '0003_jobprofile_job_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobprofile',
            name='job_category',
        ),
    ]
