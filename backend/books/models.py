from django.db import models


class Publisher(models.Model):
    publisher_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, null=True)

    def __str__(self):
        return self.name

    class Meta:
        # managed = False
        db_table = 'publisher'


class Series(models.Model):
    series_id = models.AutoField(primary_key=True)
    publisher = models.ForeignKey(Publisher, models.CASCADE)
    title = models.CharField(max_length=45, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'series'
        unique_together = (('series_id', 'publisher'),)


class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45, null=True)
    last_name = models.CharField(max_length=45, null=True)
    birthday = models.DateField(null=True)
    sex = models.CharField(max_length=45, null=True)

    def __str__(self):
        return "{} {}".format(self.last_name, self.first_name)

    class Meta:
        db_table = 'author'


class Genres(models.Model):
    genre_id = models.AutoField(primary_key=True)
    genre_name = models.CharField(max_length=45, null=True)

    def __str__(self):
        return self.genre_name

    class Meta:
        db_table = 'genres'


class UserGroup(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=45, null=True)

    class Meta:
        db_table = 'usergroup'


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    publisher = models.ForeignKey('Publisher', models.CASCADE)
    series = models.ForeignKey('Series', models.DO_NOTHING, null=True, blank=True)
    genres = models.ManyToManyField(Genres)
    authors = models.ManyToManyField(Author)
    title = models.CharField(max_length=45, null=True)
    year = models.DateField(null=True)
    num_of_pages = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    url = models.CharField(max_length=45, blank=True, null=True)
    images = models.ImageField(upload_to="images/", blank=True)
    annotation = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'book'
        unique_together = (('book_id', 'publisher', 'series'),)


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    groups = models.ManyToManyField(UserGroup)
    email = models.CharField(max_length=45, blank=True, null=True)
    first_name = models.CharField(max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    nickname = models.CharField(max_length=45, blank=True, null=True)
    sex = models.CharField(max_length=45, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.last_name, self.first_name)

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
    comment_id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, models.DO_NOTHING)
    user = models.ForeignKey(User, models.DO_NOTHING)
    text = models.CharField(max_length=45, blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'comment'
        unique_together = (('comment_id', 'book', 'user'),)
