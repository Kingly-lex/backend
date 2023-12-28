# Generated by Django 5.0 on 2023-12-27 18:43

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0008_remove_transfer_receiver_remove_transfer_sender_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sender', models.TextField(max_length=20, verbose_name='Sender Account Number')),
                ('receiver', models.TextField(max_length=20, verbose_name='Receiver Account Number')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('charge', models.DecimalField(decimal_places=2, default=0.8, max_digits=10)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('is_successful', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('to_account', models.TextField(max_length=20, verbose_name='Receiver Account Number')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('charge', models.DecimalField(decimal_places=2, default=0.8, max_digits=10)),
                ('comment', models.TextField(blank=True, max_length=200, null=True)),
                ('processed_by', models.ForeignKey(help_text='Staff who proccessed Withdrawal or deposit', on_delete=django.db.models.deletion.DO_NOTHING, related_name='deposit_banker', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='bankchargerevenue',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='bank_revenue', to='transactions.transfer'),
        ),
        migrations.CreateModel(
            name='Withdrawal',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('from_account', models.TextField(max_length=20, verbose_name='Receiver Account Number')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('charge', models.DecimalField(decimal_places=2, default=0.8, max_digits=10)),
                ('comment', models.TextField(blank=True, max_length=200, null=True)),
                ('processed_by', models.ForeignKey(help_text='Staff who proccessed Withdrawal or deposit', on_delete=django.db.models.deletion.DO_NOTHING, related_name='withdrawal_banker', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]
