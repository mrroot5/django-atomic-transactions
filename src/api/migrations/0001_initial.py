# Generated by Django 3.2.8 on 2021-10-18 18:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientAccount',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('city', models.CharField(blank=True, help_text='Ex. Aranjuez', max_length=100, null=True)),
                ('postal_code', models.CharField(blank=True, help_text='Ex. 28000', max_length=100, null=True)),
                ('state', models.CharField(blank=True, help_text='Ex. Madrid', max_length=100, null=True)),
                ('public_username', models.CharField(blank=True, help_text='Ex. nickname', max_length=150, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Ex. John', max_length=50)),
                ('surname', models.CharField(help_text='Ex. Doe', max_length=100)),
                ('user_account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClientWallet',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('balance', models.DecimalField(decimal_places=2, default=0, editable=False, help_text='Total ammount of money in this wallet', max_digits=65)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('client_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.clientaccount')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClientWalletTransaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, help_text='Transaction description', max_length=250, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('done', models.BooleanField(default=True, help_text='It check if the transaction was completed')),
                ('transaction_type', models.IntegerField(choices=[('0', 'Error'), ('1', 'Testing'), ('2', 'Deposit'), ('3', 'Withdraw')], default='1', help_text='Add or substract money')),
                ('error_msg', models.CharField(blank=True, help_text='Ex. Transaction error: negative balance', max_length=250, null=True)),
                ('extra_info', models.TextField(blank=True, help_text='Extra info about this transaction', null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('client_wallet_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.clientwallet')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
