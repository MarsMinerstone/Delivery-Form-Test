# Generated by Django 4.0.4 on 2022-06-09 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_p_image_alter_product_cat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='p_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Image'),
        ),
    ]
