# Generated by Django 4.2.5 on 2023-10-04 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]