# Generated by Django 3.2.9 on 2021-11-25 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_images_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subcategory',
            options={'ordering': ['categoryId']},
        ),
        migrations.AlterField(
            model_name='feedback',
            name='description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=800),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='tags',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]