# Generated by Django 3.1.1 on 2020-09-18 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_auto_20200917_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='gender',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('U', 'Unisex')], max_length=30, verbose_name='Genero'),
        ),
    ]
