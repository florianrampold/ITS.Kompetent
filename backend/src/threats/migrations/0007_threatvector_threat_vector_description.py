# Generated by Django 4.0.3 on 2022-11-28 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threats', '0006_alter_threatarea_area_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='threatvector',
            name='threat_vector_description',
            field=models.TextField(null=True, verbose_name='Beschreibung'),
        ),
    ]
