# Generated by Django 3.1.1 on 2020-09-18 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20200917_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.PositiveIntegerField(default=0, verbose_name='Descuento'),
        ),
    ]
