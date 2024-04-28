# Generated by Django 4.0.3 on 2022-03-11 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(max_length=140)),
                ('job_category', models.CharField(max_length=140)),
                ('job_description', models.CharField(max_length=140)),
            ],
            options={
                'ordering': ['job_name'],
            },
        ),
    ]