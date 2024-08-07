# Generated by Django 4.0.3 on 2024-02-01 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competence_tests', '0012_chatinterface_chat_sender_known'),
        ('campagne', '0011_remove_threatsituationscore_competence_dimension_score_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompetenceDimensionScorePerThreat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scoredPoints', models.IntegerField()),
                ('competence_dimension', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competence_tests.competencedimension')),
            ],
        ),
        migrations.AlterField(
            model_name='threatsituationscore',
            name='competence_dimension_score',
            field=models.ManyToManyField(to='campagne.competencedimensionscoreperthreat'),
        ),
    ]
