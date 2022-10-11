# Generated by Django 4.1.2 on 2022-10-11 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0007_alter_bookings_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookings',
            name='name_on_cake',
        ),
        migrations.AddField(
            model_name='bookings',
            name='mode_of_payment',
            field=models.CharField(choices=[('GCash', 'GCash'), ('Bank Transfer', 'Bank Transfer')], default=1, max_length=225),
            preserve_default=False,
        ),
    ]
