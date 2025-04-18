# Generated by Django 5.2 on 2025-04-17 15:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0005_transaction_tax_alter_transaction_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='description',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='transaction',
            name='ref',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='related_transaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tax_transactions', to='transactions.transaction'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
