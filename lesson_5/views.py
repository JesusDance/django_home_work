from .models import Client, Products, Cheese, ProductListModel
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.files.base import File
from uuid import uuid4
from decimal import Decimal


def create_user(request):
    client = Client.objects.create(**{
        "user": User.objects.get(pk=1),
        "name": "admin",
        "email": "admin@gmail.com",
        "discount_size": Decimal("4.25"),
        "invoice": File(open("requirements.txt", "rb")),
        "user_uuid": uuid4(),
        "client_ip": "192.0.0.2",
    })
    return HttpResponse(client.name)


def create_product(request):
    # gauda = Products()
    # gauda.name = "Dor-Blue"
    # gauda.description = "Dor-Blue is a premium cheese"
    # gauda.wiki_page = "https//www.wikipedia.org/wiki/Dor-Blue"
    # gauda.save()

    product = Products.objects.create(name="Extra Gauda")


    return HttpResponse(product)


def get_cheese(request):
    price = Cheese.shop.get(id=1).price
    return HttpResponse(price)

def create_list(request):
    list1 = ProductListModel(client=Client.objects.get(pk=1))
    list1.save()
    list1.products.set([Products.objects.get(pk=1),
                        Products.objects.get(pk=2),
                        Products.objects.get(pk=3)])

    return HttpResponse(list1)

