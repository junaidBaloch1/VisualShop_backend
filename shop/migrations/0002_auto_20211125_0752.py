# Generated by Django 3.2.9 on 2021-11-25 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='url',
        ),
        migrations.AddField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
