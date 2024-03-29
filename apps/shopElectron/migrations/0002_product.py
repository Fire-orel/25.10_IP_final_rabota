# Generated by Django 4.2.6 on 2023-11-07 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopElectron', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Товары')),
                ('categorii', models.ForeignKey(default='None', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='themes', to='shopElectron.categorii', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['categorii', 'id'],
            },
        ),
    ]
