# Generated by Django 5.0 on 2024-06-27 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0008_alter_donation_goal_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
