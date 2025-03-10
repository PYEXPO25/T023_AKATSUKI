# Generated by Django 5.1.6 on 2025-02-21 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0005_delete_room_remove_bill_data_food_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=225)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='bill_data',
            name='food',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bill_data',
            name='parking',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bill_data',
            name='electricity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bill_data',
            name='rent',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bill_data',
            name='water',
            field=models.IntegerField(default=0),
        ),
    ]
