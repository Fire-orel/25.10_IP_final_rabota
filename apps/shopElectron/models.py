from django.db import models
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User

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
    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter (id__in=ids)

class Photo(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_DEFAULT, related_name="photos", verbose_name="Товар", default="None")
    img=models.ImageField(verbose_name="Фото", default="None",upload_to="upload/product")

    class Meta:
        verbose_name="Фото"
        verbose_name_plural='Фото'

    def __str__(self):
        return "{} - {}".format(self.product,self.img)
class Cart (models.Model):
    user=models.CharField(verbose_name="ID_пользователя",default="None",max_length=50)

    product=models.ForeignKey(Product,verbose_name="ID товара товара", on_delete=models.CASCADE)
    def __str__(self):
        return "{} - {}".format(self.product,self.user)

class Orders (models.Model):
    user=models.CharField(verbose_name="Email",default="None",max_length=50)

    # product=models.ForeignKey(Product,verbose_name="ID товара товара", on_delete=models.CASCADE)
    # quantity=models.IntegerField(verbose_name="Количество")
    # summa=models.DecimalField(verbose_name="Сумма",max_digits=5,decimal_places=2,default="0")
    suma_pokupki=models.DecimalField(verbose_name="Сумма",max_digits=5,decimal_places=2,default="0")

    class Meta:
        verbose_name='Заказ'
        verbose_name_plural='Заказы'
    def __str__(self):
        return "{}-{}-{}".format(self.pk,self.user,self.suma_pokupki)

    def get_id_by_user():
        return Orders.objects.last()

class Orders_detail(models.Model):
    id_orders=models.ForeignKey(Orders, default="None",on_delete=models.CASCADE)
    id_product=models.ForeignKey(Product,verbose_name="ID товара товара", on_delete=models.CASCADE,default="None")
    quantity=models.IntegerField(verbose_name="Количество")
    summa=models.DecimalField(verbose_name="Сумма",max_digits=5,decimal_places=2,default="0")
    class Meta:
        verbose_name_plural='Детали заказа'
    def __str__(self):
        return "{} - {} -{}".format(self.id_orders,self.id_product,self.summa)
class Customers (models.Model):
    last_name=models.CharField(max_length=50,verbose_name="Фамилия")
    first_name=models.CharField(max_length=50,verbose_name="Имя")
    email=models.EmailField()
    password=models.CharField(max_length=50,verbose_name="Пароль")
    date_brith=models.DateTimeField(blank=True, null=True,verbose_name="Дата рождения")

    class Meta:
        verbose_name="Пользователь"
        verbose_name_plural='Пользователи'

    def get_customer_by_email(email):
        try:
            return Customers.objects.get(email= email)
        except:
            return False

    def get_customer_by_email_password(email,password):
        try:
            return Customers.objects.get(email= email,password=password)
        except:
            return False

    def __str__(self):
        return "{}".format(self.email)



# Create your models here.
