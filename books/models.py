from django.conf import settings
from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_year = models.IntegerField(blank=True, default=0)
    bio = models.CharField(max_length=400)


class Book(models.Model):
    title = models.CharField(max_length=120)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    page_count = models.IntegerField(default=0)


class ReadProgress(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    progress_page = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    rating = models.IntegerField() # Todo make this an enum from 0-5?
    review = models.CharField(max_length=400)

