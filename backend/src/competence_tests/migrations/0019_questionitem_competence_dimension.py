# Generated by Django 4.0.3 on 2024-05-15 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competence_tests', '0018_remove_chatinterface_chat_interface_identificator_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionitem',
            name='competence_dimension',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='competence_tests.competencedimension', verbose_name='Zugeordnete Kompetenzdimension'),
        ),
    ]