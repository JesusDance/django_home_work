from django.urls import path
from .views import *

urlpatterns = [
    path('create-user/', create_user, name='create_user'),
    path('create-product/', create_product, name='create_product'),
    path('get-cheese/', get_cheese, name='get_cheese'),
    path('create-list/', create_list, name='create_list'),
]