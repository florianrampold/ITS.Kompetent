# Generated by Django 4.0.3 on 2024-04-23 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threats', '0008_alter_threatsituation_threat_vector'),
    ]

    operations = [
        migrations.AddField(
            model_name='threatsituation',
            name='threat_situation_identificator',
            field=models.CharField(blank=True, max_length=140, null=True, verbose_name='Kennung'),
        ),
    ]
