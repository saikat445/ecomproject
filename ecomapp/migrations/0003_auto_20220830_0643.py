# Generated by Django 2.1.5 on 2022-08-30 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0002_auto_20220828_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomapp.Cart'),
        ),
    ]
