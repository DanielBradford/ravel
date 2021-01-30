# Generated by Django 3.1.3 on 2021-01-23 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20201115_1342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.AddField(
            model_name='color',
            name='sku',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='size',
            name='sku',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
