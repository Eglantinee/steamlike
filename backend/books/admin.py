from django.contrib import admin
from .models import Publisher, Series, Author, Genres, UserGroup, Book, User, BookHasUser, Comment


admin.site.register(Publisher)
admin.site.register(Series)
admin.site.register(Author)
admin.site.register(Genres)
admin.site.register(UserGroup)
admin.site.register(Book)
admin.site.register(User)
admin.site.register(BookHasUser)
admin.site.register(Comment)