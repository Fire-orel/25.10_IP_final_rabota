# Generated by Django 4.2.6 on 2023-11-08 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopElectron', '0007_categorii_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorii',
            name='url',
            field=models.SlugField(unique=True),
        ),
    ]
