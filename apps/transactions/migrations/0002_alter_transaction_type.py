# Generated by Django 5.0 on 2023-12-22 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='type',
            field=models.CharField(choices=[('Send', 'Send'), ('Receive', 'Receive')], default='Send', max_length=20),
        ),
    ]
