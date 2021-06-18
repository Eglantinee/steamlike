from django.contrib import admin
from .models import Publisher, Series, Author, Genres, Book, BookHasUser, Comment

admin.site.register(Publisher)
admin.site.register(Series)
admin.site.register(Author)
admin.site.register(Genres)
admin.site.register(Book)
admin.site.register(BookHasUser)
