# Generated by Django 5.0 on 2024-05-31 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0006_alter_blog_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='end_date',
            field=models.DateTimeField(null=True),
        ),
    ]