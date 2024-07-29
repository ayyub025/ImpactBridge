# Generated by Django 5.0 on 2024-06-07 13:23

from django.db import migrations
from django.db import migrations, models
from django.core.validators import MinValueValidator, MaxValueValidator

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0037_alter_ngodetail_ngo_founded_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngodetail',
            name='NGO_founded_year',
            field=models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2999)], blank=True, null=True),
        ),]