from django.urls import path
from . import  views

urlpatterns = [
    path('', views.post_list, name ='post_list'),
    path('contato', views.post_list_2, name ='post_list_2'),
]