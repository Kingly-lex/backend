# Generated by Django 5.0 on 2023-12-22 05:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_profiles', '0005_alter_profile_verification_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_updated',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='allacountnumbers',
            name='account_no',
            field=models.TextField(blank=True, max_length=25, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='transfer_pin',
            field=models.TextField(default='0000', max_length=4, validators=[
                                   django.core.validators.MinLengthValidator(4)]),
        ),
    ]