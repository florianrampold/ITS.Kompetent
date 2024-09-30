# Generated by Django 4.0.3 on 2024-08-08 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0022_rename_competence_dimension_training_competence_dimensions'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_category_name', models.CharField(max_length=140, verbose_name='Kategorie')),
                ('training_category_description', models.TextField(verbose_name='Erklärung')),
                ('threat_event', models.ManyToManyField(to='threats.threatevent', verbose_name='Bedrohungsereignisse')),
            ],
            options={
                'verbose_name': 'Training-Modul',
                'verbose_name_plural': 'Training-Module',
            },
        ),
    ]