# Generated by Django 5.1.1 on 2024-10-28 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='selling_price',
            new_name='original_price',
        ),
    ]