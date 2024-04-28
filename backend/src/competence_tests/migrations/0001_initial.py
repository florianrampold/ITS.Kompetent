# Generated by Django 4.0.3 on 2022-06-09 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('job_profiles', '0001_initial'),
        ('threats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatInterface',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_sender_name', models.CharField(max_length=140)),
                ('chat_sender_image', models.ImageField(upload_to='static/images')),
                ('chat_recipient_name', models.CharField(max_length=140)),
                ('chat_message_incoming', models.CharField(max_length=800)),
                ('chat_message_incoming_date', models.DateField()),
                ('chat_message_outgoing', models.CharField(blank=True, max_length=800)),
                ('chat_message_outgoing_date', models.DateField(blank=True)),
                ('chat_message_incoming_2', models.CharField(blank=True, max_length=800)),
                ('chat_message_incoming_date_2', models.DateField(blank=True)),
            ],
            options={
                'verbose_name': 'Chat Impuls',
                'verbose_name_plural': 'Chat Impulse',
            },
        ),
        migrations.CreateModel(
            name='CompetenceDimension',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dimension_name', models.CharField(max_length=140, verbose_name='Kompetenzdimension')),
                ('dimension_description', models.CharField(max_length=800)),
            ],
            options={
                'verbose_name': 'Kompetenz Dimension',
                'verbose_name_plural': 'Kompetenz Dimensionen',
            },
        ),
        migrations.CreateModel(
            name='EmailItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_name', models.CharField(max_length=140, null=True)),
                ('email_sender', models.CharField(max_length=140, null=True)),
                ('email_recipient', models.CharField(max_length=140, null=True)),
                ('email_regarding', models.CharField(max_length=140, null=True)),
                ('email_content', models.CharField(max_length=800, null=True)),
                ('email_image_sender', models.ImageField(upload_to='static/images')),
                ('email_date', models.DateField()),
                ('email_button_text', models.CharField(blank=True, max_length=140)),
            ],
            options={
                'verbose_name': 'E-Mail',
                'verbose_name_plural': 'E-Mails',
            },
        ),
        migrations.CreateModel(
            name='ImageItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=140, null=True)),
                ('image_field', models.ImageField(upload_to='static/images')),
                ('image_description', models.CharField(blank=True, max_length=800, null=True)),
            ],
            options={
                'verbose_name': 'Bild',
                'verbose_name_plural': 'Bilder',
            },
        ),
        migrations.CreateModel(
            name='Impulse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('impulse_name', models.CharField(max_length=140, null=True)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'Impuls',
                'verbose_name_plural': 'Impulse',
            },
        ),
        migrations.CreateModel(
            name='QuestionItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_name', models.CharField(max_length=140, null=True)),
                ('question', models.CharField(max_length=800)),
                ('type', models.IntegerField(choices=[(1, 'Single Choice Item'), (2, 'Multiple Choice Item'), (3, 'Ranking Item')], default=1)),
            ],
            options={
                'verbose_name': 'Frage',
                'verbose_name_plural': 'Fragen',
            },
        ),
        migrations.CreateModel(
            name='CompetenceTestItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competence_dimension', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competence_tests.competencedimension')),
                ('impulse_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='competence_tests.impulse')),
                ('question_item', models.ManyToManyField(blank=True, to='competence_tests.questionitem')),
                ('threat_situation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='threats.threatsituation')),
            ],
            options={
                'verbose_name': 'Kompetenztest Szenario',
                'verbose_name_plural': 'Kompetenztest Szenarios',
            },
        ),
        migrations.CreateModel(
            name='CompetenceTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='job_profiles.jobprofile')),
                ('threat_vector', models.ManyToManyField(to='threats.threatvector')),
            ],
        ),
        migrations.CreateModel(
            name='ChoiceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=800)),
                ('answer_rating', models.IntegerField(choices=[(0, 'Bad'), (1, 'Intermediate'), (2, 'Good')], default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competence_tests.questionitem')),
            ],
        ),
        migrations.CreateModel(
            name='ImageImpulse',
            fields=[
                ('impulse_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='competence_tests.impulse')),
                ('impulse_text', models.CharField(blank=True, max_length=800, null=True)),
                ('image', models.ManyToManyField(to='competence_tests.imageitem')),
            ],
            options={
                'verbose_name': 'Bild Impuls',
                'verbose_name_plural': 'Bild Impulse',
            },
            bases=('competence_tests.impulse',),
        ),
        migrations.CreateModel(
            name='EmailImpulse',
            fields=[
                ('impulse_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='competence_tests.impulse')),
                ('impulse_text', models.CharField(blank=True, max_length=800, null=True)),
                ('email', models.ManyToManyField(to='competence_tests.emailitem')),
            ],
            options={
                'verbose_name': 'E-Mail Impuls',
                'verbose_name_plural': 'E-Mail Impulse',
            },
            bases=('competence_tests.impulse',),
        ),
        migrations.CreateModel(
            name='ChatImpulse',
            fields=[
                ('impulse_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='competence_tests.impulse')),
                ('impulse_text', models.CharField(blank=True, max_length=800, null=True)),
                ('chat_interface', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='competence_tests.chatinterface')),
            ],
            options={
                'verbose_name': 'Bild Impuls',
                'verbose_name_plural': 'Bild Impulse',
            },
            bases=('competence_tests.impulse',),
        ),
    ]