# Generated by Django 5.0.7 on 2024-08-03 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrationformapp', '0002_register_slot_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='evalutor_1',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='evalutor_2',
            field=models.IntegerField(null=True),
        ),
    ]
