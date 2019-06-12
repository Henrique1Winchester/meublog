from django import forms

from .models import Post, Futebol


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')

class FutebolForm(forms.ModelForm):
    class Meta:
        model = Futebol
        fields = ('time', 'campo')



