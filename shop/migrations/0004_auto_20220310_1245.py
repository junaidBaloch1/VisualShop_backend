# Generated by Django 3.2.9 on 2022-03-10 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_sizes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'ordering': ['categoryId'], 'verbose_name_plural': 'Sub Categories'},
        ),
        migrations.AlterModelOptions(
            name='tags',
            options={'verbose_name_plural': 'Tags'},
        ),
        migrations.AlterField(
            model_name='images',
            name='imageColor',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Color'),
        ),
        migrations.AlterField(
            model_name='images',
            name='productId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shop.product', verbose_name='Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='subCategoryId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.subcategory', verbose_name='Subcategory'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='categoryId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Subcategories', to='shop.category', verbose_name='Category'),
        ),
    ]
