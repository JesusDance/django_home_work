from django.urls import path, include
from rest_framework.routers import SimpleRouter
from lesson_10 import views
from lesson_10.views import CreateUser, get_time
from lesson_9.views import ProductsViewSet

router = SimpleRouter()
router.register('products', ProductsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.user_login, name='login'),
    path('create-user/', CreateUser.as_view(), name='create_user'),
    path('time/', views.get_time, name='time'),
]