# Generated by Django 4.0.3 on 2022-07-21 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('threats', '0002_alter_threatarea_options_alter_threatevent_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='threatsituation',
            name='threat_vector',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='threats.threatvector', verbose_name='Zugeordneter Bedrohungsvektor'),
        ),
    ]
