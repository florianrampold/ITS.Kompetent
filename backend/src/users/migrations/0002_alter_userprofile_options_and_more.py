# Generated by Django 4.0.3 on 2024-03-12 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'Kampagnen-Berechtigung', 'verbose_name_plural': 'Kampagnen-Berechtigungen'},
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='is_campagne_manager',
            field=models.BooleanField(default=False, verbose_name='Kampagnen Manager Status'),
        ),
    ]