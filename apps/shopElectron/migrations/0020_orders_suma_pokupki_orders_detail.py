# Generated by Django 4.2.6 on 2023-12-20 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopElectron', '0019_orders_summa'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='suma_pokupki',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=5, verbose_name='Сумма'),
        ),
        migrations.CreateModel(
            name='Orders_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('summa', models.DecimalField(decimal_places=2, default='0', max_digits=5, verbose_name='Сумма')),
                ('id_orders', models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, to='shopElectron.orders')),
                ('id_product', models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, to='shopElectron.product', verbose_name='ID товара товара')),
            ],
        ),
    ]
