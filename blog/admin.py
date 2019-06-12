from django.contrib import admin
from .models import Post, Comment, Futebol, Naruto, Carro

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Futebol)
admin.site.register(Naruto)
admin.site.register(Carro)

