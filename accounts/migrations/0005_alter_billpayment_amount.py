# Generated by Django 5.0.6 on 2024-08-30 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_transaction_options_alter_transaction_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billpayment',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
