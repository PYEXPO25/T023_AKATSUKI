# Generated by Django 5.1.6 on 2025-02-21 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0003_data_delete_box'),
    ]

    operations = [
        migrations.CreateModel(
            name='bill_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(max_length=100)),
                ('rent', models.IntegerField()),
                ('electricity', models.IntegerField()),
                ('water', models.IntegerField()),
                ('food', models.IntegerField()),
                ('parking', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Data',
        ),
    ]
