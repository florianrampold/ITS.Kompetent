# Generated by Django 4.0.3 on 2024-04-23 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competence_tests', '0015_remove_competencetest_threat_vector'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailitem',
            name='email_is_signed_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images', verbose_name='Bild zur Signatur'),
        ),
    ]
