# Generated by Django 5.0 on 2024-05-31 08:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0005_donation_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
