from django import forms

from .models import Post, Perfil


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('title', 'text')

