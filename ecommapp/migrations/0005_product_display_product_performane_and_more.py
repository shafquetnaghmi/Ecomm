# Generated by Django 4.0 on 2022-07-02 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapp', '0004_remove_order_items_remove_order_shipping_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Display',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='performane',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
