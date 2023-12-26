# Generated by Django 5.0 on 2023-12-22 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0004_deposit_withdrawal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='sender',
        ),
        migrations.RemoveField(
            model_name='withdrawal',
            name='account',
        ),
        migrations.RemoveField(
            model_name='withdrawal',
            name='banker',
        ),
        migrations.DeleteModel(
            name='Deposit',
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
        migrations.DeleteModel(
            name='Withdrawal',
        ),
    ]
