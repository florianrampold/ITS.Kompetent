# Generated by Django 4.0.3 on 2022-07-14 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_profiles', '0004_remove_jobprofile_job_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobprofile',
            name='job_description',
            field=models.TextField(verbose_name='Beschreibung'),
        ),
    ]
