# Generated by Django 3.2.9 on 2021-11-27 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_alter_messages_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='messages',
            name='message',
            field=models.TextField(max_length=1000),
        ),
    ]