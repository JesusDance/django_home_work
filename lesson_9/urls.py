from django.urls import path, include
from rest_framework import routers
from .views import ping, PongView, ClientViewSet, ProductsViewSet

router = routers.SimpleRouter()
router.register(r'client', ClientViewSet)
router.register(r'products', ProductsViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth-api/', include('rest_framework.urls', namespace='rest_framework')),
    path('PING/', ping, name='ping-pong'),
    path('class-ping/', PongView.as_view(), name='class-pong'),
]