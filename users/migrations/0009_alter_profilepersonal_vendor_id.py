# Generated by Django 5.0 on 2024-05-30 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_profilepersonal_vendor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilepersonal',
            name='vendor_id',
            field=models.IntegerField(editable=False),
        ),
    ]