# Generated by Django 4.0.3 on 2022-11-25 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_profiles', '0005_alter_jobprofile_job_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobprofile',
            name='job_tasks',
            field=models.TextField(null=True, verbose_name='Aufgaben'),
        ),
    ]
