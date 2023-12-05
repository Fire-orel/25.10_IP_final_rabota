# Generated by Django 4.2.6 on 2023-11-22 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopElectron', '0009_rename_url_categorii_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img2',
            field=models.CharField(default=' ', max_length=100, verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='product',
            name='img3',
            field=models.CharField(default=' ', max_length=100, verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default=' ', verbose_name='Описание'),
        ),
    ]