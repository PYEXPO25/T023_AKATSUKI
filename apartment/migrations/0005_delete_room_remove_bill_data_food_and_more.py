# Generated by Django 5.1.6 on 2025-02-21 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0004_bill_data_delete_data'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Room',
        ),
        migrations.RemoveField(
            model_name='bill_data',
            name='food',
        ),
        migrations.RemoveField(
            model_name='bill_data',
            name='parking',
        ),
    ]
