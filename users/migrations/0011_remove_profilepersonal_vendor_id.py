# Generated by Django 5.0 on 2024-05-30 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_set_vendor_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilepersonal',
            name='vendor_id',
        ),
    ]
