# Generated by Django 4.0.3 on 2022-11-28 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0007_remove_training_trainings_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='training_provider',
            field=models.CharField(max_length=140, null=True, verbose_name='Anbieter'),
        ),
    ]
