# Generated by Django 5.0.7 on 2024-07-31 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrationformapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='slot_number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
