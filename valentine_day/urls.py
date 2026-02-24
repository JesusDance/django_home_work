from django.urls import path
from .views import *

urlpatterns = [
    path('', MyTemplateView.as_view(), name='my-list'),
    path('<int:photo_id>/', get_photo, name='photo'),
]