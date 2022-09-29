from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from .models import Author, Book, Issue


class BookCatalogue(generic.ListView):
    queryset = Book.objects.order_by('title')
    paginate_by = 9
    template_name = 'index.html'