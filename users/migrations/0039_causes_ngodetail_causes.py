# Generated by Django 5.0 on 2024-06-12 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0038_auto_20240607_1853'),
    ]

    operations = [
        migrations.CreateModel(
            name='Causes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='ngodetail',
            name='causes',
            field=models.ManyToManyField(related_name='ngos', to='users.causes'),
        ),
    ]