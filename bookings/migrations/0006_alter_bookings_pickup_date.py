# Generated by Django 4.0 on 2022-05-25 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_rename_product_ordered_bookings_cake_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='pickup_date',
            field=models.CharField(max_length=225),
        ),
    ]
