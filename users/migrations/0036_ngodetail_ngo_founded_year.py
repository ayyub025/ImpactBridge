# Generated by Django 5.0 on 2024-06-07 13:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0035_remove_ngodetail_ngo_founded_year'),
    ]

    operations = [
  
        migrations.AddField(
            model_name='ngodetail',
            name='NGO_founded_year',
            field=models.IntegerField(blank=True,null=True),
        ),
      
    ]