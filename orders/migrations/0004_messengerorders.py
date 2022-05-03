# Generated by Django 4.0 on 2022-05-02 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_category_status'),
        ('orders', '0003_alter_orders_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessengerOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=255)),
                ('customer_address', models.CharField(max_length=255)),
                ('no_of_order', models.IntegerField()),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_ordered', models.DateField(auto_now_add=True)),
                ('pickup_date', models.DateField()),
                ('processed_by', models.CharField(max_length=255)),
                ('notes', models.TextField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Done', 'Done'), ('Cancelled', 'Cancelled'), ('Late', 'Late')], max_length=255)),
                ('remarks', models.CharField(choices=[('Accept', 'Accept'), ('Decline', 'Decline')], max_length=255)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products')),
            ],
            options={
                'verbose_name': 'MessengerOrders',
            },
        ),
    ]
