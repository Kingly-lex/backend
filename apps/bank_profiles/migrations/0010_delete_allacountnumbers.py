# Generated by Django 5.0 on 2023-12-22 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank_profiles', '0009_alter_profile_transfer_pin'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AllAcountNumbers',
        ),
    ]