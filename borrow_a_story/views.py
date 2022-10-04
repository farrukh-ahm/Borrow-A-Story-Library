from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from .models import Author, Book, Issue
from .forms import IssueForm


class BookCatalogue(generic.ListView):
    queryset = Book.objects.order_by('title')
    paginate_by = 9
    template_name = 'index.html'


class BookIssue(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Book.objects.all()
        book = get_object_or_404(queryset, slug=slug)
        issue = book.issue.all()
        form = IssueForm()
        context = {
            'book': book,
            'issue': issue,
            'form': form,
        }

        return render(request, 'book_issue.html', context)