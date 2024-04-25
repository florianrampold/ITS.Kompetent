# Generated by Django 4.0.3 on 2022-06-29 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competence_tests', '0006_alter_chatinterface_chat_message_incoming'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='choiceitem',
            options={'ordering': ['question'], 'verbose_name': 'Antwort', 'verbose_name_plural': 'Antworten'},
        ),
        migrations.AlterField(
            model_name='chatinterface',
            name='chat_message_incoming_date',
            field=models.TimeField(verbose_name='Datum der 1. eingehenden Nachricht'),
        ),
        migrations.AlterField(
            model_name='choiceitem',
            name='answer_rating',
            field=models.IntegerField(choices=[(0, 'Falsch'), (1, 'Mittel'), (2, 'Richtig')], default=0, verbose_name='Bewertung der Antwortoption'),
        ),
    ]
