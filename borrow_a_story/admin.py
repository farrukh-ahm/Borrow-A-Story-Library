from django.contrib import admin
from .models import Author, Book, Issue


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['author']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'author', 'publish_year', 'available', 'shelf']
    list_filter = ['author', 'available']
    search_fields = ['title', 'author']


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ['book', 'issued_to', 'issued_on']
    search_fields = ['book']
