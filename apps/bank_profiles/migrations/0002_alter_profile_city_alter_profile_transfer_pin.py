# Generated by Django 5.0 on 2023-12-20 11:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='transfer_pin',
            field=models.CharField(default='123456', validators=[django.core.validators.MinLengthValidator(4)]),
        ),
    ]
