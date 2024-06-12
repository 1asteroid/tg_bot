from django.db import models


class User(models.Model):
    full_name = models.CharField(verbose_name="Full name", max_length=100, null=True, blank=False)
    username = models.CharField(verbose_name="Username", max_length=50, unique=True, null=True)
    telegram_id = models.PositiveBigIntegerField(verbose_name="Telegram ID", unique=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Product(models.Model):
    productname = models.CharField(verbose_name="Maxsulot nomi", max_length=50)
    photo = models.CharField(verbose_name="Rasm file_id", max_length=200, null=True)
    price = models.DecimalField(verbose_name="Narx", decimal_places=2, max_digits=8)
    description = models.TextField(verbose_name="Tavsif", max_length=3000, null=True)
    category_code = models.CharField(verbose_name="Kategoriya kodi", max_length=20)
    category_name = models.CharField(verbose_name="Kategoriya nomi", max_length=30)
    subcategory_code = models.CharField(verbose_name="Ost-Kategoriya nomi", max_length=30)
    subcategory_name = models.CharField(verbose_name="Ost-Kategoriya nomi", max_length=30)

    def __str__(self):
        return self.productname

