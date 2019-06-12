from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name ='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit', views.post_edit, name='post_edit'),
    path('/comment', views.comment_list, name='comment_list'),
    path('futebol', views.futebol_list, name ='futebol_list'),
    path('naruto', views.naruto_list, name ='naruto_list'),
    path('carro', views.carro_list, name ='carro_list'),

]