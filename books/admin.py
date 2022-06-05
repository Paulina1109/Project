from django.contrib import admin
from books.models import Genre, Book, UserList, TopTen, Recommendation

admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(UserList)
admin.site.register(TopTen)
admin.site.register(Recommendation)

