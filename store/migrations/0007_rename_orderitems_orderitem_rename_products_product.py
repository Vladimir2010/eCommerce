# Generated by Django 4.1.5 on 2023-07-21 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_rename_orders_order'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderItems',
            new_name='OrderItem',
        ),
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]