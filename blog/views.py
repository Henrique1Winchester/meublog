from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment, Perfil
from .forms import PostForm, PerfilForm


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

def perfil_list(request):
    perfils = Perfil.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': perfils})


def perfil_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def perfil_new(request):
    if request.method == "POST":
        form = PerfilForm(request.PERFIL)
        if form.is_valid():
            perfil = form.save(commit=False)
            perfil.author = request.user
            perfil.published_date = timezone.now()
            perfil.save()
            return redirect('post_detail', pk=perfil.pk)
    else:
        form = PerfilForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def perfil_edit(request, pk):
    perfil = get_object_or_404(Perfil, pk=pk)
    if request.method == 'Perfil':
        form = PerfilForm(request.PERFIL, instance=perfil)
        if form.is_valid():
            perfil = form.save(commit=False)
            perfil.author = request.user
            perfil.published_date = timezone.now()
            perfil.save()
            return redirect('post_detail', pk=perfil.pk)
    else:
        form = PerfilForm(instance=perfil)
    return render(request, 'blog/post_edit.html', {'form': form})