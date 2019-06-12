from django.db import models
from django.utils import timezone


# Create your models here.


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.title


class Futebol(models.Model):
    jogador = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    time = models.CharField(max_length=200)
    campo = models.TextField()

    def __str__(self):
        return self.time

class Naruto(models.Model):
    ninjas = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    data = models.CharField(max_length=200)
    campo = models.TextField()

    def __str__(self):
        return self.data

class Carro(models.Model):
    pista = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    estrada = models.CharField(max_length=200)
    campo = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.estrada
