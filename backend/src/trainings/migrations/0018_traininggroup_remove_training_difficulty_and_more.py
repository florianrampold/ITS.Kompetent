# Generated by Django 4.0.3 on 2024-02-11 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0017_alter_training_certification_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=140, null=True, verbose_name='Identifizierung der Gruppe')),
            ],
            options={
                'verbose_name': 'Trainings-Gruppe',
                'verbose_name_plural': 'Trainings-Gruppen',
            },
        ),
        migrations.RemoveField(
            model_name='training',
            name='difficulty',
        ),
        migrations.RemoveField(
            model_name='training',
            name='registration',
        ),
        migrations.RemoveField(
            model_name='training',
            name='target_group',
        ),
        migrations.RemoveField(
            model_name='training',
            name='time_invest',
        ),
        migrations.AddField(
            model_name='training',
            name='training_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trainings.traininggroup', verbose_name='Zugeordnete Trainings-Gruppe'),
        ),
    ]
