# Generated by Django 5.0 on 2023-12-18 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allacountnumbers',
            name='account_no',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
