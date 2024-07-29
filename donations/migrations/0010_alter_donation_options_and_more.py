# Generated by Django 5.0 on 2024-06-27 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0009_donation_is_verified'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='donation',
            options={'permissions': [('can_change_is_approved', 'Can change the approval status of donations')]},
        ),
        migrations.RenameField(
            model_name='donation',
            old_name='is_verified',
            new_name='is_approved',
        ),
    ]