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
        # issue_date = book.issue.all()
        form = IssueForm()
        context = {
            'book': book,
            # 'issue': issue_date,
            'form': form,
        }

        return render(request, 'book_issue.html', context)

    def post(self, request, slug, *args, **kwargs):
        queryset = Book.objects.all()
        book = get_object_or_404(queryset, slug=slug)
        issue = book.issue.all()
        book.available = False
        form_content = IssueForm(request.POST)
        if form_content.is_valid():
            form_content.instance.issued_to = request.user
            issued = form_content.save(commit=False)
            issued.book = book
            issued.save()
            book.save()
        else:
            form_content = IssueForm()
        
        context = {
            'book': book,
            'issue': issue,
            'form': form_content,
        }

        return render(request, 'book_issue.html', context)