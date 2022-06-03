from django.db import models


class Genre(models.Model):
    title = models.CharField(max_length=64, primary_key=True)
    genre = models.CharField(max_length=32)


class Book(models.Model):
    title = models.CharField(max_length=32)
    author = models.CharField(max_length=32)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title + " " + self.author


class Recommendation(models.Model):
    rate = models.FloatField()
    description = models.TextField()
    book = models.ForeignKey('Book', on_delete=models.CASCADE)

    def __str__(self):
        return self.rate + self.description


class UserList(models.Model):
    description = models.TextField(default=None)
    book = models.ManyToManyField(Book)

    def __str__(self):
        return self.comment


class TopTen(models.Model):
    title = models.CharField(max_length=32)
    author = models.CharField(max_length=32)
    rate = models.FloatField()
    description = models.TextField()
