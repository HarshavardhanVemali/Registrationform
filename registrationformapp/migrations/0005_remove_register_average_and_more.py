# Generated by Django 5.0.7 on 2024-08-08 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrationformapp', '0004_register_average'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='average',
        ),
        migrations.RemoveField(
            model_name='register',
            name='concept_to_present',
        ),
        migrations.RemoveField(
            model_name='register',
            name='evalutor_1',
        ),
        migrations.RemoveField(
            model_name='register',
            name='evalutor_2',
        ),
        migrations.RemoveField(
            model_name='register',
            name='slot_number',
        ),
    ]
