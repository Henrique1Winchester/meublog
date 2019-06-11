from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name ='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit', views.post_edit, name='post_edit'),
    path('/comment', views.comment_list, name='comment_list'),
    path('', views.perfil_list, name ='perfil_list'),
    path('perfil/<int:pk>/', views.perfil_detail, name='perfil_detail'),
    path('perfil/new', views.perfil_new, name='perfil_new'),
    path('perfil/<int:pk>/edit', views.perfil_edit, name='perfil_edit'),
]