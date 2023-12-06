from django.db import models
from django.urls import reverse
from datetime import datetime

class Categorii (models.Model):
    name=models.CharField(verbose_name="Категории",max_length=100,)
    slug=models.SlugField(max_length=50,unique=True)

    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop_electron_product", kwargs={"slug": self.slug})


class Product (models.Model):
    categorii=models.ForeignKey(Categorii, on_delete=models.SET_DEFAULT,related_name="themes",verbose_name='Категория',default="None")
    name=models.CharField(verbose_name="Название",max_length=100)
    price=models.DecimalField(verbose_name="Цена",max_digits=5,decimal_places=2,default="0")
    description=models.TextField(verbose_name="Описание",default=" ")
    count=models.IntegerField(verbose_name="Количество на остатке",default="0")

    class Meta:
        verbose_name='Товар'
        verbose_name_plural='Товары'
        ordering=['categorii','id']
    def __str__(self):
        return  "{} - {}".format(self.categorii, self.name)

class Photo(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_DEFAULT, related_name="photos", verbose_name="Товар", default="None")
    img=models.ImageField(verbose_name="Фото", default="None",upload_to="upload/product")

    class Meta:
        verbose_name="Фото"
        verbose_name_plural='Фото'

    def __str__(self):
        return "{} - {}".format(self.product,self.img)


# Create your models here.
