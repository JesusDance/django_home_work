from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=64, null=True)
    discount_size = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    email = models.EmailField(unique=True, null=True)
    invoice = models.FileField(blank=True, null=True, upload_to="uploads/%Y/%m/%d")
    user_uuid = models.UUIDField(editable=False, null=True)
    client_ip = models.GenericIPAddressField(blank=True, null=True,
                                             protocol="IPv4")
    birthday = models.DateField(null=True, blank=True)


    def __str__(self):
        return f"{self.id}_{self.name}"


class Products(models.Model):
    name = models.CharField(max_length=64, unique=True, null=True)
    description = models.TextField(blank=True, null=True)
    delivered_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    could_use_for_eating = models.BooleanField(default=True)
    wiki_page = models.URLField(default="https://en.wikipedia.org/",
                                name="wikipedia",
                                blank=True)

    def __str__(self):
        return self.name


class ProductListModel(models.Model):
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING, null=True)
    products = models.ManyToManyField(Products)

    def __str__(self):
        return f"{self.id}_{self.client.name}"


class Cheese(models.Model):
    shop = models.Manager()
    fresh_period = models.DurationField(default=timedelta(days=30),
                                        help_text="Fresh time expiration "
                                                  "of the cheese", null=True)
    photo = models.ImageField(blank=True, null=True)
    price = models.FloatField(default=50.0, null=True)
    cheese = models.ManyToManyField(Products, verbose_name="This cheese is a "
                                                            "product for eating")


class Meat(models.Model):
    fresh_period = models.DurationField(default=timedelta(days=5),
                                        help_text="Fresh time expiration of meat",
                                        null=True)
    photo = models.ImageField(blank=True, null=True)
    price = models.FloatField(default=0.0, null=True)
    meat = models.ManyToManyField(Products)


class Bread(models.Model):
    fresh_period = models.DurationField(default=timedelta(days=3),
                                        help_text="Fresh time expiration of bread",
                                        null=True)
    bread = models.ManyToManyField(Products, verbose_name="This is a bread")
    photo = models.ImageField(blank=True, null=True)
    price = models.FloatField(default=30.0, null=True)


class Sausage(models.Model):
    fresh_period = models.DurationField(default=timedelta(days=15),
                                        help_text="Fresh time expiration "
                                                  "of sausage", null=True)
    photo = models.ImageField(blank=True, null=True)
    price = models.FloatField(default=50.0, null=True)
    sausage = models.ManyToManyField(Products, verbose_name="This is a sausage "
                                                            "from meat")


class Milk(models.Model):
    fresh_period = models.DurationField(default=timedelta(days=20),
                                        help_text="Fresh time expiration for milk",
                                        null=True)
    photo = models.ImageField(blank=True, null=True)
    price = models.FloatField(default=47.0, null=True)
    milk = models.ManyToManyField(Products, verbose_name="This is a milk")






