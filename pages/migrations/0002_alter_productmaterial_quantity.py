# Generated by Django 5.1.2 on 2024-10-27 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmaterial',
            name='quantity',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
