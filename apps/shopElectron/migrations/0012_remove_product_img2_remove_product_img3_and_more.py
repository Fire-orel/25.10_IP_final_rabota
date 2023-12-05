# Generated by Django 4.2.6 on 2023-11-29 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopElectron', '0011_product_count_alter_product_img2_alter_product_img3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='img2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='img3',
        ),
        migrations.AlterField(
            model_name='product',
            name='count',
            field=models.IntegerField(default='0', verbose_name='Количество на остатке'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(default='None', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='product', to='shopElectron.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Фото',
            },
        ),
    ]