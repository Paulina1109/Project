from django.contrib import admin
from books.models import Genre, Book, User, TopTen

admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(User)
admin.site.register(TopTen)

