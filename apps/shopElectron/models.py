from django.db import models
from datetime import datetime

class Categorii (models.Model):
    name=models.CharField(verbose_name="Категории",max_length=100)

    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'
    def __str__(self):
        return self.name
class Product (models.Model):
    categorii=models.ForeignKey(Categorii, on_delete=models.SET_DEFAULT,related_name="themes",verbose_name='Категория',default="None")
    name=models.CharField(verbose_name="Товары",max_length=100)
    # price=models.

    class Meta:
        verbose_name='Товар'
        verbose_name_plural='Товары'
        ordering=['categorii','id']
    def __str__(self):
        return  "{} - {}".format(self.categorii, self.name)

# Create your models here.
