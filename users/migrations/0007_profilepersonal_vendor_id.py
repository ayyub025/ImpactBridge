# Generated by Django 5.0 on 2024-05-30 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_profilepersonal_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilepersonal',
            name='vendor_id',
            field=models.IntegerField(default=False, editable=False),
        ),
    ]
