# Generated by Django 4.0.3 on 2022-06-28 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competence_tests', '0005_alter_chatinterface_options_alter_choiceitem_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatinterface',
            name='chat_message_incoming',
            field=models.TextField(verbose_name='Eingehende Nachricht 1'),
        ),
    ]
