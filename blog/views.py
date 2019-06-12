from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment, Futebol, Naruto, Carro
from .forms import PostForm, FutebolForm


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def comment_list(request):
    comment = Comment.objects.all()
    return render(request, 'blog/comment_list.html', {'comment': comment})

def futebol_list(request):
    futebol = Futebol.objects.all()
    return render(request, 'blog/futebol_list.html', {'futebol': futebol})

def futebol_edit(request, pk):
    futebol = get_object_or_404(Futebol, pk=pk)
    if request.method == 'POST':
        form = FutebolForm(request.POST, instance=futebol)
        if form.is_valid():
            futebol = form.save(commit=False)
            futebol.jogador = request.user
            futebol.save()
            return redirect('futebol_detail', pk=futebol.pk)
    else:
        form = FutebolForm(instance=futebol)
    return render(request, 'blog/futebol_edit.html', {'form': form})
def futebol_detail(request, pk):
    futebol = get_object_or_404(Futebol, pk=pk)
    return render(request, 'blog/futebol_detail.html', {'futebol': futebol})


def naruto_list(request):
    naruto = Naruto.objects.all()
    return render(request, 'blog/naruto_list.html', {'naruto': naruto})

def carro_list(request):
    carro = Carro.objects.all()
    return render(request, 'blog/carro_list.html', {'carro': carro})