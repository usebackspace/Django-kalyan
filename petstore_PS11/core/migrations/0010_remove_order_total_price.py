# Generated by Django 5.0.1 on 2024-03-10 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_order_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total_price',
        ),
    ]
