# Generated by Django 3.2.9 on 2021-12-15 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tags',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
