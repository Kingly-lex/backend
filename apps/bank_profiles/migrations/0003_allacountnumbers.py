# Generated by Django 5.0 on 2023-12-20 12:35

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_profiles', '0002_alter_profile_city_alter_profile_transfer_pin'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllAcountNumbers',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('account_no', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acct_no', to='bank_profiles.profile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]