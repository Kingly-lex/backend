# Generated by Django 5.0 on 2023-12-28 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0009_transfer_deposit_alter_bankchargerevenue_source_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BankChargeRevenue',
        ),
    ]
