from django.db import models


class Publisher(models.Model):
    publisher_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'publisher'


class Series(models.Model):
    series_id = models.IntegerField(primary_key=True)
    publisher = models.ForeignKey(Publisher, models.DO_NOTHING)
    title = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'series'
        unique_together = (('series_id', 'publisher'),)


class Author(models.Model):
    author_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'author'


class Genres(models.Model):
    genre_id = models.IntegerField(primary_key=True)
    genre_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'genres'


# class BookAuthor(models.Model):
#     book = models.OneToOneField('Book', models.DO_NOTHING, primary_key=True)
#     author = models.ForeignKey('Author', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'BookAuthor'
#         unique_together = (('book', 'author'),)


# class BookGenre(models.Model):
#     book = models.OneToOneField('Book', models.DO_NOTHING, primary_key=True)
#     genre = models.ForeignKey('Genres', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'BookGenre'
#         unique_together = (('book', 'genre'),)


# class UserGroup(models.Model):
#     user = models.OneToOneField('User', models.DO_NOTHING, primary_key=True)
#     group = models.ForeignKey('UserGroup', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'UserGroup'
#         unique_together = (('user', 'groupe'),)


class UserGroup(models.Model):
    group_id = models.IntegerField(primary_key=True)
    group_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'usergroup'


class Book(models.Model):
    book_id = models.IntegerField(primary_key=True)
    publisher = models.ForeignKey('Publisher', models.DO_NOTHING)
    series = models.ForeignKey('Series', models.DO_NOTHING)
    genres = models.ManyToManyField(Genres)
    authors = models.ManyToManyField(Author)
    title = models.CharField(max_length=45, blank=True, null=True)
    year = models.DateField(blank=True, null=True)
    num_of_pages = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    url = models.CharField(max_length=45, blank=True, null=True)
    images = models.TextField(blank=True, null=True)
    annotation = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'book'
        unique_together = (('book_id', 'publisher', 'series'),)


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    groups = models.ManyToManyField(UserGroup)
    email = models.CharField(max_length=45, blank=True, null=True)
    first_name = models.CharField(max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    nickname = models.CharField(max_length=45, blank=True, null=True)
    sex = models.CharField(max_length=45, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        db_table = 'user'


class BookHasUser(models.Model):
    book = models.ForeignKey('Book', models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)
    price = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'book_has_user'
        unique_together = (('book', 'user'),)


class Comment(models.Model):
    comment_id = models.IntegerField(primary_key=True)
    book = models.ForeignKey(Book, models.DO_NOTHING)
    user = models.ForeignKey(User, models.DO_NOTHING)
    text = models.CharField(max_length=45, blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'comment'
        unique_together = (('comment_id', 'book', 'user'),)
