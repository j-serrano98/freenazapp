# Generated by Django 5.2 on 2025-04-17 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0006_transaction_description_transaction_ref_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='tax',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12),
        ),
    ]
