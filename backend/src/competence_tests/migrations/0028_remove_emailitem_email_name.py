# Generated by Django 4.0.3 on 2024-09-27 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competence_tests', '0027_remove_imageitem_image_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailitem',
            name='email_name',
        ),
    ]