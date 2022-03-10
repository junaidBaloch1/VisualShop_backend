# Generated by Django 3.2.9 on 2022-03-10 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='provinceId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='customer.province', verbose_name='Province'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cityId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.city', verbose_name='City'),
        ),
    ]
