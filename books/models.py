from django.db import models

class Genre(models.Model):
    title = models.CharField(max_length=64, primary_key=True)
    genre = models.CharField(max_length=32)


class Book(models.Model):
    title = models.CharField(max_length=32)
    author = models.CharField(max_length=32)
    genre = models.ManyToManyField(Genre)


class Recommendation(models.Model):
    rate = models.FloatField()
    description = models.TextField()
    book = models.ForeignKey('Book', on_delete=models.CASCADE)


class User(models.Model):
    rate = models.FloatField()
    comment = models.TextField
    book = models.ManyToManyField(Book)


class TopTen(models.Model):
    title = models.CharField(max_length=32)
    author = models.CharField(max_length=32)
    rate = models.FloatField()
    description = models.TextField()
