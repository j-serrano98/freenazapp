# Generated by Django 5.2 on 2025-04-16 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_alter_transaction_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='type',
            field=models.CharField(choices=[('INCOME', 'Income'), ('EXPENSE', 'Expense'), ('INVESTMENT', 'Investment')], default='EXPENSE', max_length=10),
        ),
        migrations.AlterField(
            model_name='transactioncategory',
            name='type',
            field=models.CharField(choices=[('INCOME', 'Income'), ('EXPENSE', 'Expense'), ('INVESTMENT', 'Investment')], default='EXPENSE', max_length=10),
        ),
    ]
