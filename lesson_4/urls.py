from django.urls import path
from .views import *
from .post_view import *

urlpatterns = [
    path('main/', index, name='index'),
    path('main/luc/', luc, name='luc'),
    path('main/leya/', leya, name='leya'),
    path('main/han/', han, name='han'),
    path('people/', PeopleView.as_view(), name='people'),
    path('todo-list/', lets_do_it, name='lets_do_it'),
    path('main/file/', file, name='file'),
    path('main/new-file', new_file, name='new_file'),
    path('post/', MyTemplateView.as_view(), name='post-view'),
    path('post/<int:question_id>/', detail, name='detail'),
]