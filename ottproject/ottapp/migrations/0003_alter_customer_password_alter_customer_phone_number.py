# Generated by Django 5.0.1 on 2024-01-03 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ottapp', '0002_alter_customer_password_alter_customer_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
    ]
