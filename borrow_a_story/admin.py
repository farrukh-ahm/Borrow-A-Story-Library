from django.contrib import admin
from .models import Author, Book, Issue, User_Detail


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['author']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'author', 'publish_year', 'available', 'shelf']
    list_filter = ['author', 'available']
    search_fields = ['title', 'author']
    actions = ['available']


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ['book', 'issued_to', 'issued_on', 'return_status']
    search_fields = ['book']
    actions = ['return_status']


@admin.register(User_Detail)
class UserDetailAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'contact_no']
    search_fields = ['user']
