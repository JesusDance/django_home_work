from django.urls import path
from lesson_8.views import MyFormView, ClientResponseView, ClientRegisterView, product_view, game_view


urlpatterns = [
    path('', MyFormView.as_view(), name='form-model'),
    path('products/', product_view, name='product-view'),
    path('game-view/', game_view, name='game-view'),
    path('response/', ClientResponseView.as_view(), name='response-view'),
    path('register/', ClientRegisterView.as_view(), name='register-view'),
]