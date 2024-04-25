# Generated by Django 4.0.3 on 2022-06-09 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competence_tests', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chatimpulse',
            options={'verbose_name': 'Chat Impuls', 'verbose_name_plural': 'Chat Impulse'},
        ),
        migrations.AlterModelOptions(
            name='chatinterface',
            options={'verbose_name': 'Chat Interface', 'verbose_name_plural': 'Chat Interface'},
        ),
        migrations.AlterField(
            model_name='chatinterface',
            name='chat_message_outgoing_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='chatinterface',
            name='chat_sender_image',
            field=models.ImageField(blank=True, upload_to='static/images'),
        ),
    ]
