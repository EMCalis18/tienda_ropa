# Generated by Django 3.1.1 on 2020-09-18 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20200917_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.CharField(choices=[('0', 'Talle por numero'), ('1', 'Talle por letra')], max_length=17, verbose_name='Unidad de medida'),
        ),
    ]
