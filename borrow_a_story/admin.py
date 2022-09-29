from django.contrib import admin
from .models import Author, Book, Issue


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    