# Generated by Django 4.0 on 2022-04-05 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='notes',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
