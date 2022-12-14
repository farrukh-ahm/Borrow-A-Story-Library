from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import datetime


class Author(models.Model):
    author = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['author']

    def __str__(self):
        return f"{self.author}"


class Book(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="book_author"
        )
    publish_year = models.DateField()
    slug = models.SlugField(max_length=100, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField()
    bookmarked = models.ManyToManyField(User, related_name="bookmarked")
    available = models.BooleanField(default=True)
    shelf = models.CharField(max_length=10, null=False, default="vault")

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f"{self.title}: {self.author}"

    # Get a list of all the users who bookmarked particular book
    def user_bookmarked(self):
        tests = self.bookmarked.all()
        li = []
        for test in tests:
            li.append(test.id)
        return li


class Issue(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='issue'
        )
    issued_to = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_name"
        )
    issued_on = models.DateTimeField(auto_now=True)
    return_by = models.DateField()
    return_status = models.BooleanField(default=False)

    class Meta:
        ordering = ['issued_on']

    def __str__(self):
        return f"{self.book}: {self.issued_to}"


class User_Detail(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user'
        )
    address = models.TextField()
    contact_no = models.IntegerField()

    def __str__(self):
        return f"{self.user}: {self.contact_no}"
