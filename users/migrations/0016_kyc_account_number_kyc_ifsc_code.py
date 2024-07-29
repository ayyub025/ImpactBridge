# Generated by Django 5.0 on 2024-06-01 05:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_alter_kyc_pan_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='kyc',
            name='account_number',
            field=models.CharField(max_length=20, null=True, validators=[django.core.validators.RegexValidator('^\\d{9,18}$', 'Invalid account number format')]),
        ),
        migrations.AddField(
            model_name='kyc',
            name='ifsc_code',
            field=models.CharField(max_length=11, null=True, validators=[django.core.validators.RegexValidator('^[A-Z]{4}0[A-Z0-9]{6}$', 'Invalid IFSC code format')]),
        ),
    ]